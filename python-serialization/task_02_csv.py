#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):

    try:
        with open(csv_filename, mode='r') as f:
            csv_read = csv.DictReader(csv_filename)
            csv_data = [row for row in csv_read]

        with open('data.json', mode='w') as json_f:
            json.dump(csv_data, json_f)

        return True

    except FileNotFoundError:
        print(f"File {csv_filename} not found")
        return False

    except Exception as e:
        print(f"An error ocurred: {e}.")
        return False
