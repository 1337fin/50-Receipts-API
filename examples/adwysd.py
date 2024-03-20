import requests

url = "http://api.50receipts.com/api/adwysd"

data = {
    "discordId": "YOUR DISCORD ID",
    "apiKey": "YOUR API KEY",

    # All data additions will be shown to you when you run the file.
}

r = requests.post(url, data=data)
print(r.text)
