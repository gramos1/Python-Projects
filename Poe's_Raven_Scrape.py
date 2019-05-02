# BeautifulSoup module is needed in order to run this scraper

from bs4 import BeautifulSoup
import requests
import time
import os
import random
os.system('color 0c') # Setting the mood.
os.system('cls')

source = requests.get('http://www.gutenberg.org/files/17192/17192-h/17192-h.htm').text
soup = BeautifulSoup(source, 'lxml')

poem = soup.find_all('div', class_='poem') # Here we are capturing the whole poem
stanzas = soup.find_all('div', class_='stanza') # Here we are capturing the stanzas

def RandomStanza():
    print()
    print("""This program will scrape Gutenberg.org and get a random stanza from Edgar Alan Poe's poem 'The Raven.' """.center(100, ' '))
    print(random.choice(stanzas).text) # Here we are printing the random stanza
    print()
    ans = input("Would you like a new stanza (y/n)? ")
    ans = ans.lower()
    
    if ans == 'y':
        os.system('cls')
        RandomStanza()
    else:
        exit()
        

RandomStanza() # Calling the function

