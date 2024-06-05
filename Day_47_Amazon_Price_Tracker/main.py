from bs4 import BeautifulSoup
import requests
import smtplib
import ssl

LOWEST_PRICE = 400
MY_EMAIL = "popww619@gmail.com"
MY_PASSWORD = "vfyuqrhmwxtlsdwb"

response = requests.get("https://www.amazon.in/PLUMBURY%C2%AE-Womens-Padded-Racerback-Sports/dp/B09BDB6KY5/ref=sr_1_5?crid=2UNSAIRD66FQK&keywords=sports+bra&psr=EY17&qid=1683399074&s=todays-deals&sprefix=sports%2Ctodays-deals%2C2975&sr=1-5")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
tag = soup.find(name="span", class_="a-price-whole")
current_price = int(tag.getText())

if current_price < LOWEST_PRICE:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=context) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, "bikram1209@gmail.com", "Subject:PRICE DROP\n\nPrice less that lower Price")
