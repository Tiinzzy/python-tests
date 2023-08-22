import requests
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def find_a_tag(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a', href=True)
    for link in links:
        absolute_link = urljoin(url, link['href'])
        print(absolute_link)

        # return absolute_link


def traverse(given_urls):
    for url in given_urls:
        derived_urls = find_a_tag(url)
        # print(derived_urls)
        # traverse(derived_urls)


if __name__ == "__main__":
    # if len(sys.argv) > 1:
    #     start_link = sys.argv[1]
    # else:
    #     start_link = input('Please enter a Wikipedia link: ')

    start_link = ['https://cnn.com']
    traverse(start_link)
