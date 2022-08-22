from flask import Flask, render_template
import requests

# The Blog Data API
api_data = requests.get("https://api.npoint.io/26fbf7293417c3006449").json()


# The Server
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=api_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post(index):
    for i in api_data:
        if i["id"] == index:
            requested_posts = i
    return render_template("post.html", the_post=requested_posts)


if __name__ == "__main__":
    app.run(debug=True)
