import pip._vendor.requests 
from pprint import pprint
import json
import sys
import numpy as np
import pandas as pd
import random as rd


modes = ["driving", "walking", "bicycling", "transit"]

def get_directions(origin, destination, modes):
    results = []
    for mode in modes:
        API_KEY = "AIzaSyBFAku7ADesqHQxOfdXRdSzkivQztMTWlY"
        if mode == "driving":
            url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={mode}&key={API_KEY}&routeLabels=ECO_FRIENDLY"
        else:
            url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={mode}&key={API_KEY}"
        results.append(pip._vendor.requests .get(url).json())
    return results