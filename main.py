from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"
blog_data = requests.get(URL).json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_data)

@app.route('/post/<int:id_num>')
def blog_post(id_num):
    return render_template("post.html", all_posts=blog_data, index=id_num)

if __name__ == "__main__":
    app.run(debug=True)
