import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.amazon.in/Bourge-Vega-6-Running-Shoes-7-Vega-6-07/dp/B07TYCDKGT/ref=sr_1_1_sspa?dchild=1&keywords=shoes&qid=1589820631&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHREtWUVVTOFhYSzQmZW5jcnlwdGVkSWQ9QTEwMjU3NDUzTVRYTkwyRjRRUFpaJmVuY3J5cHRlZEFkSWQ9QTEwMjgzMTUzMjRJRUg5REJMR0NNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
def checkPrice():
    page = requests.get(URL,headers=headers)
    soup1 = BeautifulSoup(page.content, "lxml")
    soup = BeautifulSoup(soup1.prettify(),"lxml")
    # print(soup2.prettify())
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    converted_price = price[2:]
    send_mail()
    print(title.strip())
    print(converted_price)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('xxx@gmail.com','password')
    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1589804165&sr=8-1'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'sender@gmail.com',
        'receiver@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')
    server.quit()
while(True):
    checkPrice()
    time.sleep(60)
