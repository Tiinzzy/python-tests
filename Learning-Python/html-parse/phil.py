import sys
import re
from database import Database
import ssl
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import collections
collections.Callable = collections.abc.Callable


WIKI_BASE_URL = 'https://en.wikipedia.org'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def check_for_paragraph(element):
    if str(element).startswith('<p'):
        for aTag in element:
            if str(aTag).startswith('<a'):
                return str(aTag)
    return None


def check_for_parser_output(element, all_links):
    if element.name == 'div':
        good_div = len(element.attrs) > 0 and 'class' in element.attrs.keys() and len(
            element.attrs['class']) > 0 and element.attrs['class'][0] == 'mw-parser-output'
        if good_div:
            for ch in element:
                aTag = check_for_paragraph(ch)
                if aTag is not None:
                    all_links.append(str(aTag))
                    return all_links
    return all_links


def get_link(start_link):
    all_links = list()
    html = None
    try:
        html = urllib.request.urlopen(start_link, context=ctx).read()
        soup = BeautifulSoup(html, 'lxml')
    except:
        return None

    link = None

    for child in soup.recursiveChildGenerator():
        all_links = check_for_parser_output(child, all_links)
        if len(all_links) > 0:
            link = all_links[0]
            break

    if link is not None:
        left_key = 'href="'
        link = link[link.find(left_key)+6:]
        final_link = link[:link.find('"')]
        wikipedia_link = WIKI_BASE_URL + final_link
        return wikipedia_link
    else:
        return None


def get_wiki_title(start_link):
    link = str(start_link)
    return link[link.find('org/wiki/')+9:]


def add_to_database(from_title, to_title):
    if not link_already_exist(from_title, to_title):
        db = Database()
        con, cur = db.open_database()
        sql = "INSERT INTO tests.wiki_articles_relations (from_title, to_title) VALUES (%s, %s)"
        cur.execute(sql, (from_title, to_title))
        con.commit()
        db.close_database()


def link_already_exist(from_title, to_title):
    db = Database()
    con, cur = db.open_database()
    sql = "select count(*) from tests.wiki_articles_relations  where from_title = %s and to_title = %s"
    cur.execute(sql, (from_title, to_title))
    rows = cur.fetchall()
    alread_exist = (rows[0][0] == 1)
    db.close_database()
    return alread_exist


def do_search(start_link):
    for i in range(100):
        from_title = get_wiki_title(start_link)
        start_link = get_link(start_link)
        to_title = get_wiki_title(start_link)
        if len(from_title) > 0 and len(to_title) > 0:
            add_to_database(from_title, to_title)
            print(from_title, '--->', to_title)
            if re.search('Philosophy_of_logic', start_link):
                break


def get_all_data():
    db = Database()
    con, cur = db.open_database()
    sql = 'SELECT from_title, to_title FROM tests.wiki_articles_relations'
    cur.execute(sql)
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(
            {'from_title': row[0], 'to_title': row[1]})
    db.close_database()
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_link = sys.argv[1]
    else:
        start_link = input('Please enter a wikipedia link: ')

    do_search(start_link)
