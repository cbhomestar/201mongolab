from bs4 import BeautifulSoup
import requests
import json

r = requests.get('https://www.airbnb.com/s/Paris--France?guests=&checkin=11%2F16%2F2015&checkout=11%2F20%2F2015&ss_id=zru0ehp2&source=bb')

airbnbSoup = BeautifulSoup(r.content)

prices = airbnbSoup.find_all("span", {"class": "price-amount"})
names = airbnbSoup.find_all("h3", {"class": "listing-name"})

pricesText = [];
namesText = [];
data = [];

index = 0;
for p in prices:
    pricesText.append(p.text.strip())
    namesText.append(names[index].find('a').text.strip())
    data.append({'price': p.text.strip(), 'description': names[index].find('a').text.strip()})
    index += 1




with open("parisText", "w") as outfile:
    json.dump({'data': data}, outfile, indent=4)