import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import time

URL = 'https://www.amazon.com/-/zh_TW/dp/B084ZTV3QK/ref=sr_1_3?keywords=fujifilm&qid=1584169005&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.130 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    title = soup.find(id="productTitle").get_text("|", strip=True)
    # print(title)
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[3:8]
    converted_price = float(converted_price.replace(',', '.'))

    if converted_price < 1.700:
        send_mail()

    print(price)
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pwh2230@gmail.com', 'qlmuvchsruvgefzs')

    subject = 'price fell down'
    body = 'Check the amazon link: ' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pwh2230@gmail.com',
        'pakwing13579@yahoo.com.hk',
        msg
    )
    print('email has been sent!')

    server.quit()


while True:
    check_price()
    time.sleep(3600)
