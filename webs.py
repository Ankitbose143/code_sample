import requests
import urllib
from bs4 import BeautifulSoup
import re
# import beautifulsoup
# import scrapy.

url = 'https://www.geeksforgeeks.org/python-web-scraping-tutorial/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
             "X-Amzn-Trace-Id": "Root=1-63cf0052-760b19697375364569cfc0d0"}

# d = requests.get(urllib.urlopen(url).read(), 'html')
# d = requests.get(url,headers=headers,params={'url': url, 'wait': 2})
d = requests.get(url)
print("ddd",d)
print("ddd---text",d.text)

red = BeautifulSoup(d.text, 'html.parser')
# print(red)
# print("red.prettify()",red.prettify())
# print("red.title",red.title, "--", red.title.name)
# print(red.find_all('a'))
print("red.get_tex",red.get_text(), type(red.get_text()))
d1 = red.get_text()
print("9999",red.find_all('Languages'))
# print("0000", d1.findAll("Languages"))
strings=[d1, 'Language' ]
lt= []
lt2 = []
lt3 = []
match2 = strings[1]
# for match2 in strings[1]:
#     lt = []
# count()
print("count-----",sum([1 for re in re.finditer(match2, strings[0])]))
for match in re.finditer(match2, strings[0]):
    print("match", match, "0000",match.group())
    print("match.string",match.start(),match.end())
    lt3.append([match.start(),match.end()])
    lt.append(match.start())
    print("dfg",match2,match.start(), lt)
lt2.append(lt)
print(lt2, lt3)
soup = red
reviewlist= []

reviews = soup.find_all('div', {'data-hook': 'review'})
print("REviews", reviews)
try:
    for item in reviews:
        review = {
        'Reviews': item.find('span', {'data-hook': 'review-body'}).text.strip(),
        }
        reviewlist.append(review)
except:
    pass
print("RE", reviewlist)