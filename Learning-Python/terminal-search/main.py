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
            links.append({"title": title, "link": link})

    return links


def save_news_to_file(news, filename):
    with open(filename, "w") as file:
        for index, item in enumerate(news, start=1):
            file.write(f"Index: {index}\n")
            file.write(f"Title: {item['title']}\n")
            file.write(f"Link: {item['link']}\n")
            file.write("\n")


if __name__ == "__main__":
    input_query = input("Enter a search prompt: ")
    prompt_sentiment = analyze_sentiment(input_query)
    print(f"Sentiment is: {prompt_sentiment}")

    news = search_news(input_query)

    if news:
        num_to_save = min(len(news), 10)
        news_to_save = news[:num_to_save]

        save_filename = "news_results.txt"
        save_news_to_file(news_to_save, save_filename)

        print("News results saved!")
    else:
        print("No news have been found!")
