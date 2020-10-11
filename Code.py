'''
Mobile Pricing From Amazon
@author: Suyash Shivaji Phatak
Date: 10/05/2020
'''

# Importing Modules
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request 
# Giving url
url = "https://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty&q=Price%3A10000%2C15000%7C"

# Preventing the 403 error
req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})

# Reading all content
content = urllib.request.urlopen(req).read()

# Passing the content to function
soup = BeautifulSoup(content, features="lxml")

print('_________________________________________________________________________')

# Printing content
print('\nAll contents of Websites')
print(soup.prettify())

# Printing title of website
print('_________________________________________________________________________')
print(soup.find('title'))
print('_________________________________________________________________________')

# Printing all elements of images and their alt text of 250 TV shows
print('These are Names of Mobile which comes in between Rs.10000 to Rs.15000\n')

# Printing all names of mobile phones using image titles
element =[]
for link in soup.find_all('img'):
    element.append(link.get('title'))

# Removing all None values
final =[]
for val in element:
    if val!= None:
        final.append(val)

# Printing Final List
for x in final:
    print(x)
    
print('_________________________________________________________________________')

