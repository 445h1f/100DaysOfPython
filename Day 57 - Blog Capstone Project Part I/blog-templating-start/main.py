from flask import Flask, render_template
from dotenv import load_dotenv
from post import Post
import requests
import os


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
        blog = Post(id=p['id'], title=p['title'], subtitle=p['subtitle'], body=p['body'])
        blogs.append(blog)

    return blogs


allBlogs = getAllBlogs()


app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template("index.html", blogs=allBlogs)

@app.route('/blog/<int:id>')
def getBlog(id):
    blog = allBlogs[id-1]
    return render_template('post.html', title=blog.title, subtitle=blog.subtitle, body=blog.body)

if __name__ == "__main__":
    app.run(debug=True)
