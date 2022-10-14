import requests
from bs4 import BeautifulSoup


# getting html text by requesting the website
response = requests.get('https://news.ycombinator.com/front')
response.raise_for_status()

html = response.text


# parsing got html to beautifulsoup
soup = BeautifulSoup(html, "html.parser")
# print(soup.title)

# getting all titles
newsHeadings = soup.select(selector=".titleline > a")
articleUpvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(len(newsHeadings), len(articleUpvotes))
# print(newsHeadings, articleUpvotes)

'''
for index, news in enumerate(newsHeadings):
    newsTitle = news.getText()
    newsLink = news.get('href')
    newsUpvotes = articleUpvotes[index]
    print(f'Title: {newsTitle}\nLink: {newsLink}\nUpvotes: {newsUpvotes}\n\n')
'''

maxUpvotes = max(articleUpvotes)
indexOfMax = articleUpvotes.index(maxUpvotes)
titleOfMax = newsHeadings[indexOfMax].getText()
linkOfMax = newsHeadings[indexOfMax].get('href')
print(f'Article with Maximum Upvote ({maxUpvotes}):\nTitle: {titleOfMax}\nLink: {linkOfMax}')
