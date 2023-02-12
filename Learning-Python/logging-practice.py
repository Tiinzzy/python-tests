import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="/home/tina/Downloads/logs/my-pyton-practice.log", 
                    filemode="a")


def process_url(url):
    logging.error(f"someting gone wrong during fetching data from URL: {url}")


if __name__ == "__main__":
    logging.info(f"Just started the process")
    url = 'https://www.cnn.com'    
    process_url(url)
    logging.info(f"Process ended successfully!")
    
