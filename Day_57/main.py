from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url).json()
    return render_template("index.html", blogs=blog_response)


@app.route('/post/<blog_id>')
def blogpost(blog_id):
    bid = int(blog_id)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_response.raise_for_status()
    all_blogs = blog_response.json()
    return render_template("post.html", id_num=bid, blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
