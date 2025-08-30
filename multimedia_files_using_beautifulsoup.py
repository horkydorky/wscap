
#import modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

#get page content
url='https://www.thehindu.com/news/national/coronavirus-live-updates-may-29-2021/article34672944.ece?homepage=true'

page=requests.get(url)

#display page content
page.content

#parse the data
soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

#find the img source link
img_tag=soup.find('source')
img_tag['srcset']

img_url=img_tag['srcset']

#download image from url
image=requests.get(img_url)

#store the image in file
with open('image.png','wb') as file:
  for chunk in image.iter_content(chunk_size=1024):
    file.write(chunk)

ppt = requests.get('http://www.howtowebscrape.com/examples/media/images/SampleSlides.pptx')
with open('sample.pptx','wb') as file:
  for chunk in ppt.iter_content(chunk_size=1024):
    file.write(chunk)

ppt = requests.get('http://www.howtowebscrape.com/examples/media/images/BigRabbit.mp4')
with open('video.mp4','wb') as file:
  for chunk in ppt.iter_content(chunk_size=1024):
    file.write(chunk)