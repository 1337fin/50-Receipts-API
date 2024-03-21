import requests

url = "http://api.50receipts.com/api/louisvuitton"

data = {
    "discordId": "YOUR DISCORD ID",
    "apiKey": "YOUR API KEY",
    "gender": "male", # male or female
    "size": "nothing" # type nothing in size if there isn't a size

    # All data additions will be shown to you when you run the file.
}

r = requests.post(url, data=data)
print(r.text)
