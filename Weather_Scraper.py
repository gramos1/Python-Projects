# REQUIREMENT: BeautifulSoup module is needed in order to run this scraper.

from bs4 import BeautifulSoup
import requests
import time
import subprocess

subprocess.call(["cmd","/c", "color 0f"]) 

source = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8861&lon=-87.6216#.XJT7DChKiCg').text
soup = BeautifulSoup(source, 'lxml')

mainpage = soup.find("div", class_="panel panel-default")

city = mainpage.h2.text
sky = mainpage.p.text

ftemp = soup.find('p', class_='myforecast-current-lrg').text # temp in Fahrenheit
ctemp = soup.find('p', class_='myforecast-current-sm').text # temp in celsius
tonight = soup.find(class_='col-sm-10 forecast-text').text # here we are getting the forecast for the night

# Here is the main loop set to True
Refresh = True 

while Refresh:
    t = time.asctime()
    print()
    print("Real-time weather for Chicago brought to you by Giovanny!".center(100, ' '))
    print()


    # if temperature is above 79
    if int(ftemp[:-2]) > 79:
        print(''' Temperature is {}. It's kinda hot. Walk in the shade and use sunblock. {}'''.format(ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    # if temperature is between 60 and 79
    if int(ftemp[:-2]) < 79 and int(ftemp[:-2]) > 60:
        print('''The temperature is {}. It's nice and warm. Enjoy the day and make the most it! {}'''.format(ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    # if temperature is between 48 and 60
    if int(ftemp[:-2]) < 60 and int(ftemp[:-2]) > 48:
        print("The temperature is at {} right now, seems just right (to me at least).\nMight be a good idea to wear a light sweater if going outside, just in case. {}".format(ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    # if temparature is between 42 and 48
    elif int(ftemp[:-2]) < 48 and int(ftemp[:-2]) > 42:
        print('''The temperature is {} right now, it's kinda cold.
You'll need to wear a jacket if you'll be going out for a walk. 
BUT you can go outside in a t-shirt if you're feeling tough. {}'''.format(ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    # if temperature is between 27 and 42
    elif int(ftemp[:-2]) < 42 and int(ftemp[:-2]) > 27:
        print('''It's cold. Its {}, this is the type of temperature all we Chicagoans are used to so
it shouldn't surprise you. Make sure to take your good coat, scarf etc. You know the drill. {}'''.format(ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    # if temperature is between 15 and 27
    elif int(ftemp[:-2]) < 27 and int(ftemp[:-2]) > 15:
        print('''Its {}.
Yep.. {}. It's cold so bundle up and stay warm. {}'''.format(ftemp, ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    # if temperature is below 15
    elif int(ftemp[:-2]) < 15:
        print("Temperature is {}. Stay at home if you can. {}".format(ftemp, sky))
        print()
        print("Tonight's forecast:")
        print(tonight)

    print()
    print()
    print("Information scraped on {}".format(t))
    print()
    print("Weather information will be scraped every 5 minutes.")
    print()
    time.sleep(300) # Here I anm setting the refresh time to 5 minutes
    subprocess.call(['cmd','/c', 'cls'])








