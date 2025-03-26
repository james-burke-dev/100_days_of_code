import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, 'html.parser')

titles = soup.select("h3.title")

movie_list = []

for title in titles:
    if title.getText()[0] in "0123456789":
        movie_list.append(title.getText())

movies = movie_list[::-1]

with open("movies.txt", mode="w") as fn:
    for movie in movies:
        fn.write(f"{movie}\n")