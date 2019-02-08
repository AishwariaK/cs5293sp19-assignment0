import json
import random
import urllib.request
from random import *

# Python3 type hints
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"


def download():
    """ This function downloads the json data from the url."""
    r=urllib.request.urlopen(url)
    d=r.read()
    return d
   

def extract_requests(text: str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    d=json.loads(text)
    prom=d['promises']
    return prom


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    title = [d['title'] for d in promises]
    return title
   

def random_title (titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    n=len(titles)
    r=randint(1, n)
    t=titles[r]
    return t

reqst = extract_requests(download())
tle = extract_titles(reqst)
rndm = random_title(tle)
