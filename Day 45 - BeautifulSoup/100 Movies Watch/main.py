import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
html = response.text

# parsing html to beautifulsoup
soup = BeautifulSoup(html, "html.parser")

# scraping all movie titles
movies = soup.find_all(name="h3", class_="title")
movieNames = [movie.getText() for movie in movies]
# print(movieNames)

# reversing movieNames list so that counting starts from 1 as original is from 100)
movieNames.reverse()

# writing movie names in movies.txt file
with open('movies.txt', 'w+', encoding="utf-8") as file:
    for name in movieNames:
        file.write(f'{name}\n')







