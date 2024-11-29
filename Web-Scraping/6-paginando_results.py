import requests
from collections import Counter
import pandas as pd

# 1 - Utilizando Access Token
access_token = '' # token gerado pelo github
headers = {'Authorization': 'Bearer ' +access_token,
           'X-GitHub-Api-Version': '2022-11-28'
           }