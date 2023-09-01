import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"


def search_news(query):
    base_url = "https://search.brave.com/news"
    params = {
        "q": query
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    for anchor in soup.find_all("a"):
        title = anchor.get_text()
        link = anchor["href"]

        if link.startswith("http"):
            revised_title = title.replace('\n', ' * ').split(' * ')[-1]
            links.append({"title": revised_title})

    return links


if __name__ == "__main__":
    input_query = input("Enter a search prompt: ")

    prompt_sentiment = analyze_sentiment(input_query)
    print(f"Search prompt sentiment is: {prompt_sentiment}")

    news = search_news(input_query)

    if news:
        num_to_save = min(len(news), 10)
        news_to_save = news[:num_to_save]

        print("Sentiments for the individual titles:")
        for index, item in enumerate(news_to_save, start=1):
            print(news_to_save)
            title_sentiment = analyze_sentiment(item['title'])
            print(f"Title {index}: {title_sentiment}")

    else:
        print("No news have been found!")
