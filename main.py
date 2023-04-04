import requests as r
import json
import csv
from datetime import date


def get_most_relevant_items():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1577#json'
    response = r.get(url).text
    response = json.loads(response)
    data = response['results']

    with open('microwave.csv','w') as file:
        for item in data:
            _id = item.get('id')
            site_id = item.get('site_id')
            title = item.get('title')
            price = item.get('price')
            sold_quantity = item.get('sold_quantity')
            thumbnail = item.get('thumbnail')
            created_date = date.today()
            file.write(f"{_id},{site_id},{title},{price},{sold_quantity},{thumbnail},{created_date}\n")
