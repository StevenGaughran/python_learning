from flask import Flask, render_template
import requests
# API: https://api.npoint.io/c790b4d5cab58020d391

# Blog Data from API
blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

# FLASK Stuff
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
