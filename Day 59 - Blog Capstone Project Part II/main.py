from flask import Flask, render_template
from dotenv import load_dotenv
from post import Post
import requests
import os
from datetime import datetime


blogTitle = 'Bob\'s Blog'
copyrightYear = datetime.now().year

# getting blogs api endpoint
load_dotenv()
BLOG_API = os.getenv('BLOG_API')


def getAllBlogs():
    """Returns all blog as Post object."""

    blogs = []
    response = requests.get(url=BLOG_API)
    response.raise_for_status()
    posts = response.json()

    for p in posts:
        blog = Post(id=p['id'], title=p['title'], subtitle=p['subtitle'], body=p['body'], author=p['author'], date=p['date'])
        blogs.append(blog)

    return blogs

allBlogs = getAllBlogs()

app = Flask(__name__)


# response for home route
@app.route('/')
def home():
    return render_template('index.html', title=f'Home | {blogTitle}', blogs=allBlogs, copyrightYear=copyrightYear)

# response from blog number
@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    if blog_id > len(allBlogs):
        return render_template('404.html', title=f'404 | {blogTitle}', copyrightYear=copyrightYear)
    blog = allBlogs[blog_id - 1]
    return render_template('post.html', title=f'{blog.title} | {blogTitle}', blog=blog, copyrightYear=copyrightYear)

# response for contact route
@app.route('/contact')
def contact():
    return render_template('contact.html', title=f'Contact | {blogTitle}', copyrightYear=copyrightYear)


# response for about route
@app.route('/about')
def about():
    return render_template('about.html', title=f'About | {blogTitle}', copyrightYear=copyrightYear)


# response for invalid route 404
@app.errorhandler(404)
def error404(error):
    return render_template('404.html', title=f'404 | {blogTitle}', copyrightYear=copyrightYear)

if __name__ == "__main__":
    app.run(debug=True)