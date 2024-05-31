#!/usr/bin/python3

import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)

def fetch_and_print_posts():

    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        yeison = r.json()

    for i in yeison:
        print(i['title'])


def fetch_and_save_posts():

    if r.status_code == 200:
        yeison = r.json()


        dictio = [{'id': i['id'], 'title': i['title'], 'body': i['body']} for i in yeison]

        print(dictio)

        with open('posts.csv', 'w', newline='\n') as f:
            write = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            write.writeheader()
            write.writerows(dictio)
