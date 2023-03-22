from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    response.raise_for_status()
    posts = response.json()
    return render_template("home.html", posts=posts)

@app.route('/blog/<int:id>')
def post_page(id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    response.raise_for_status()
    posts = response.json()
    particular_post = posts[id-1]
    return render_template("post.html", post=particular_post)

if __name__ == "__main__":
    app.run(debug=True)
