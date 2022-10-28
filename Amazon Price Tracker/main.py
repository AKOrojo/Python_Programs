from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

AMAZON_URL = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Sterilizer/dp/B083KM6BZS/ref=sr_1_1?keywords=Instant+Pot+Duo+Evo+Plus+10-in-1+Pressure+Cooker%2C+Rice+Cooker%2C+Slow+Cooker%2C+Yogurt+Maker%2C+Sous+Vide%2C+Saut%C3%A9%2C+Food+Warmer%2C+Bake%2C+Stock+Pot%2C+Steamer%2C+Cookware+Grade+Stainless+Steel+Inner+Pot%2C+6+Quart&qid=1666952483&qu=eyJxc2MiOiIxLjE3IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sr=8-1"
HEADER = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
BUY_PRICE = 100
YOUR_SMTP_ADDRESS = ""
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

response = requests.get(url=AMAZON_URL, headers=HEADER)
response.raise_for_status()
amazon_webpage = response.content

soup = BeautifulSoup(amazon_webpage, "lxml")

price = soup.find("span", class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addr=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
