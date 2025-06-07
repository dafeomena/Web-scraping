import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/'

response = requests.get(url)
response.status_code

soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all('a', class_='title')
movies

movie_list = []
for movie in movies:
    movie_list.append(movie.text)

movie_list

release = soup.find_all('span', class_='year')
release

Year = []
for movie in release:
    Year.append(movie.text)

Year = [item.strip("()") for item in Year]
Year

Rating = soup.find_all('span', class_='score')
Rating

Ratings = []
for rating in Rating:
    Ratings.append(rating.text)

Ratings

Top_300_movies = {
    'Title' : movie_list,
    'Year' : Year,
    'Rating' : Ratings
}

df = pd.DataFrame(Top_300_movies)

df.index = df.index + 1
df.to_csv('Top_300_movies.csv', index=True)

df