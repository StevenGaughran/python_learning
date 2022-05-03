from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

movies = soup.findAll(name="h3", class_="title")

movie_list = []

for i in reversed(movies):
    title = i.getText()
    movie_list.append(title)

with open("movies.txt", "w") as f:
    for i in movie_list:
        f.write(i + "\n")
