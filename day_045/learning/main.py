from bs4 import BeautifulSoup
import requests

# Local HTML File
file_path = "day_045/learning/website.html"

with open(file_path) as fn: 
    contents = fn.read()

soup = BeautifulSoup(contents, 'html.parser')
#print(soup.title)
#print(soup.title.string)

#print(soup.a)

all_anchors = soup.find_all(name="a")

for elem in all_anchors:
    #print(elem.getText())
    #print(elem.get("href"))
    pass

heading = soup.find_all(name="h1", id="name")

company_url = soup.select_one(selector="p a")
#print(company_url)

# Scraping Y Combinator
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

titles = soup.select(".storylink")
print(titles)

article_texts = []
article_links = []

for title in titles:
    article_texts.append(title.getText())
    article_links.append(title.get("href"))

article_points = [int(score.getText().split()[0]) for score in soup.select(".score")]
print(article_points)

index_of_highest_value = article_points.index(max(article_points))


print("Most popular article: ")
print(article_texts[index_of_highest_value])
print(article_links[index_of_highest_value])