

from pydoc import classname
from xmlrpc.client import ResponseError
import requests 
from bs4 import BeautifulSoup as bs

def get_github_user_info():
    try:
        github_user = input('Input your Github Username: ')
        url = f"https://github.com/{github_user}"
        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        username = soup.find('span', {'class': 'vcard-username'}).text.strip()
        name = soup.find('span', {'class': 'p-name'}).text.strip()
       
    except ResponseError:
        print("Please input a valid Github Username")
    
    else: 
        print(f"Hello {name}, I know your GitHub username is {username}")   


get_github_user_info()
