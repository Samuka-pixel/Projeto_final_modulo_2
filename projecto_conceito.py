import tkinter as tk
from tkinter import messagebox
import requests

Api_chv = "blah blah blah"
url = "blahblahblah.com"
icon_url = "blahiconblah.com"

def dado_meteorologicos(city):
    params = {
        'q': city,
        'appid': Api_chv,
        'units': 'metric',
        'lang': 'pt'
    }
    response = requests.get(url, params=params)
    return response.json()