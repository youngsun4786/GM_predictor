import pip._vendor.requests 
from pprint import pprint
import json
import sys
import numpy as np
import pandas as pd
import random as rd

def call_API(request_route):
    API_KEY = 'jvbN3Ulbl7Z4XNdpD1zJR3CGb70V49yrH1B9nWU4'
    API_URL = f'https://developer.nrel.gov/api/routee/v2/route?api_key={API_KEY}'
    # POST to the API
    headers = {'content-type': 'application/json'}
    response = pip._vendor.requests.post(API_URL,  json=request_route, headers=headers)
    # response code -> 200 OK
    if response.status_code == 200:
        print('Metadata: \n')
        pprint(response.json()['output_metadata'])
        print('Data: ')
        new_df = pd.DataFrame(response.json()['route'])
        print(new_df.head())
    else:
        print(response.text)

# convert km to miles 
def km_to_miles(input):
    return float(input) * 0.621371


def response_from_user(answers):
    ids = []
    speeds = [int(km_to_miles(answers[0]))]
    distances = [km_to_miles(answers[1])]
    grades = []
    energy_mode = answers[2]
    
    net_id = rd.randint(1, 1000000)
    grade_new = float(0)
    ids.append(int(net_id))
    grades.append(grade_new)

    request_route_data = {
    "segment_ids": ids,
    "lengths_miles": distances,
    "speeds_mph": speeds,
    "grades_percent": grades,
    "model": energy_mode, 
    }
    call_API(request_route=request_route_data)

if __name__ == "__main__":
    answer = ['72', '13', 'electric']
    # retrieve the API key from the website
    response_from_user(answer)


