import requests

url = "http://api.50receipts.com/api/adwysd"

data = {
    "discordId": "YOUR DISCORD ID",
    "apiKey": "YOUR API KEY",
  
    "product_link": "YOUR PRODUCT LINK",
    "email": "test@example.com",
    "size": "YOUR SIZE",
    "price": 100.00,
    "shipping_fee": 10.00,
    "tax_fee": 1.00,
    "currency": "£",
    "currency_tag": "GBP",
    "full_name": "50 Receipts",
    "address": "YOUR ADDRESS",
    "city": "YOUR CITY",
    "postal_code": "YOUR POSTAL CODE",
    "country": "YOUR COUNTRY",
}

r = requests.post(url, data=data)
print(r.text)
