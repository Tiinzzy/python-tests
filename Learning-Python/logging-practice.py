import logging
import smtplib
from email.mime.text import MIMEText


SENDER_EMAIL = "senders email"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="/home/tina/Downloads/logs/my-pyton-practice.log",
                    filemode="a")


def process_url(url):
    logging.error(f"someting gone wrong during fetching data from URL: {url}")


def send_email(subject, body, to_address):
    logging.info(f"sending email to {to_address}")
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_address
    try:
        smtpObj = smtplib.SMTP_SSL('senders email', 465)
        smtpObj.ehlo()
        smtpObj.login('your own username!', 'password')
        smtpObj.sendmail(SENDER_EMAIL, to_address, msg.as_string())
        smtpObj.close()
        print(msg)
        logging.info(f"email sent successfully")
    except:
        logging.info(f"something gone wrong while sending email!")


def test1():
    logging.info(f"Just started the process")
    url = 'https://www.cnn.com'
    process_url(url)
    logging.info(f"Process ended successfully!")


if __name__ == "__main__":
    # test1()

    send_email("PAY US 100$ AND SUCCESS WILL BE YOURS!",
               "Hi there, ...", "recievers email")
