from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import config

mail = config.MAIL
password = config.PASSWORD

#get the link to check
URL = "https://www.amazon.com.br/"

#http://myhttpheader.com (link to get language and user-agent)

header = {
    "Accept-Language": "get in the link above",
    "User-Agent": "get in the link above"
}
response = requests.get(URL, headers=header)


soup = BeautifulSoup(response.content, 'lxml')
title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 1000.0
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("R$")[1]
price_as_edit = (price_without_currency.replace('.', ''))
price_as_float = float(price_as_edit.replace(',', '.'))

# Gmail: smtp.gmail.com
#
# Hotmail: smtp.live.com
#
# Outlook: outlook.office365.com
#
# Yahoo: smtp.mail.yahoo.com

#change the SMTP based in your mail choice

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.live.com", port=587) as connection:
        connection.starttls()
        result = connection.login(mail, password)
        connection.sendmail(
            from_addr=mail,
            to_addrs=mail,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode('utf-8')
        )
#
