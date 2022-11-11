from flask import Flask, render_template, request
from dotenv import load_dotenv
from post import Post
import requests
import os
from datetime import datetime
import smtplib


blogTitle = 'Bob\'s Blog'
copyrightYear = datetime.now().year

# getting envs
load_dotenv()
BLOG_API = os.getenv('BLOG_API')
EMAIL = os.getenv('EMAIL')
SYSTEM_EMAIL = os.getenv('SYSTEM_EMAIL')
PASSWORD = os.getenv('PASSWORD')

# creating smtlib connection
print(f'Logging to email...')
connection = smtplib.SMTP('smtp.office365.com', port=587)
connection.starttls() # starting tls encryption
connection.login(user=EMAIL, password=PASSWORD) # logging to email
print(f'Successfully logged in!')


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
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    # checking what type of request is
    if request.method == 'POST': # if POST type
        h1 = 'Successfully sent your message' # h1 text after submitting form in contact.html

        # getting submitted form data
        name = request.form['name'] # submitted name
        email = request.form['email'] # submitted email
        phone = request.form['phone'] # submitted phone
        message = request.form['message'] # submitted message

        # sending email to system email for contact message
        emailSubject = f'Contact request from {name}'
        emailBody = f'Name: {name}\nE-Mail: {email}\nPhone: {phone}\nMessage: {message}'

        print(f'Sending email to system...')
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=SYSTEM_EMAIL,
            msg=f'Subject:{emailSubject}\n\n{emailBody}'.encode('utf-8')
        )
        print(f'Email sent to system!')

        # sending email to user for contact confirmation
        userEmailSubject = f'Thanks for Contacting {blogTitle}'
        userEmailBody = f'We\'ve recieved your request and will revert back to you as soon as possible.\n\nSubmitted Details: \n{emailBody}'

        print(f'Sending email to submitted user email...')
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=email,
            msg=f'Subject:{userEmailSubject}\n\n{userEmailBody}'.encode('utf-8')
        )
        print(f'Email sent to user email!')
    else:
        h1 = 'Contact Me' # h1 text for normal get request


    return render_template('contact.html', title=f'Contact | {blogTitle}', h1=h1, copyrightYear=copyrightYear)


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