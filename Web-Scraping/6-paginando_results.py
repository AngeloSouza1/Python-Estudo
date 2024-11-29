import requests
from collections import Counter
import pandas as pd

# 1 - Utilizando Access Token
access_token = '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' # token gerado pelo github
headers = {'Authorization': 'Bearer ' +access_token,
           'X-GitHub-Api-Version': '2022-11-28'
           }