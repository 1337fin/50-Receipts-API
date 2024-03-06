import requests

url = "https://50receipts.com/api/stockx"

data = {
    "discordId": "YOUR_DISCORD_ID",
    "apiKey": "YOUR_API_KEY",

    "product_link": "https://stockx.com/en-gb/air-jordan-4-retro-metallic-gold-womens",
    "email": "test@example.com",
    "size": "M",
    "price": 90,
    "processing_fee": 1.23,
    "shipping_fee": 10,
    "tax_fee": 1.12,
    "tax_boolean": True,
    "currency": "£",
    "delivered_on": "12/12/23",
    "receipt_type": 3   # Delivered

}

# Receipt Type 1 = StockX Ordered
# Receipt Type 2 = StockX Verified & Shipped
# Receipt Type 3 = StockX Delivered
# Receipt Type 4 = StockX Refunded

r = requests.post(url, data=data)

print(r.text)
