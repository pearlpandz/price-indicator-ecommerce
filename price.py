import requests
from bs4 import BeautifulSoup
import smtplib
import config
import time

def sendemail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    print(server);
    server.login(config.from_address, config.password)
    subject = config.subject
    body = f"Check amazon link {config.URL}"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(config.from_address,config.to_address,msg)
    print(config.successMsg)
    server.quit()

def checkprice():
    page = requests.get(config.URL, headers=config.headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:].replace(",", ""))

    if(converted_price > config.expected_price):
        print('yes')
        sendemail()
    else:
        print('no')


while True:
    checkprice()
    # time.sleep(60) # this loop excecute 1 time/1 min