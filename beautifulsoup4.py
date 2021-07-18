import bs4
import requests

res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922')
res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922', headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
}) #Pretending to be a real browser by providing a User-Agent header
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
elems = soup.select('#rentAccordionRow_263333 > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last')
print(soup.select('#rentPrice'))
