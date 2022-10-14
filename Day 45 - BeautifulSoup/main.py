from bs4 import BeautifulSoup


# reading html file
with open('website.html', encoding='utf-8') as file:
    content = file.read()

# parsing the html raw content to beautifulsoup
soup = BeautifulSoup(content, "html.parser")

# prints the html in formatted way
# print(soup.prettify())

# get title element of page
# print(soup.title)

# print string between title tag
# print(soup.title.string)

print(soup.a) # returns first a (anchor) tag in html

elementList = soup.find_all(name='a') # returns list of all a tag
# print(elementList)

for tag in elementList:
    # print(tag.string) # returns text enclosed in tag | similar to element.name

    # to get value of any attribute (if attribute is not in tag None will be returned)
    value = tag.get('hrefs')
    print(value)

# find element with more details
heading = soup.find(name='h1', id='name') # finds element with h1 tag having id 'name'

sectionHeading = soup.find(name='h3', class_="heading") #finds element with h3 tag having class 'heading'

#class_ is used because class is reserved keyword in python so cannot be used


# using css selector to select elements
aInP = soup.select_one(selector='p a') # returns first anchor tag which is in p tag (pass any other css selection method like id, class etc)

listHeadings = soup.select(selector=".heading") # returns list of all elements having class heading