import requests

url = "http://api.50receipts.com/api/adwysd"

data = {
    "discordId": "YOUR DISCORD ID",
    "apiKey": "YOUR API KEY",

    # All data additions will be shown to you when you run the file.
}

r = requests.post(url, data=data)
print(r.text)


# Receipt Type 1 = StockX Ordered
# Receipt Type 2 = StockX Verified & Shipped
# Receipt Type 3 = StockX Delivered
# Receipt Type 4 = StockX Refunded
