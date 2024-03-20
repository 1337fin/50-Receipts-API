import requests

url = "http://api.50receipts.com/api/nike"


data = {
    "discordId": "YOUR DISCORD ID",
    "apiKey": "YOUR API KEY",
    "product_link": prl,
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
    "receipt_type": 3, # 1 = Nike.com | 2 = Nike SNKRS | 3 = Nike You Got 'Em
    "order_date": "01/01/2024",
    "estimated_date": "07/01/2024",
}

# Receipt Type 1 = Nike.com
# Receipt Type 2 = Nike SNKRS
# Receipt Type 3 = Nike You Got 'Em

r = requests.post(url, data=data)
print(r.text)
