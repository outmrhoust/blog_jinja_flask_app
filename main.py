import requests
from flask import Flask, render_template

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
response.raise_for_status()
blog_data = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_data=blog_data)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    one_blog = [data for data in blog_data if data["id"] == blog_id]
    return render_template("post.html", one_blog=one_blog[0])


if __name__ == "__main__":
    app.run(debug=True)
