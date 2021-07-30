from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://s3.us-east-2.amazonaws.com/johnvold.com-public/giphy.gif",
    "https://s3.us-east-2.amazonaws.com/johnvold.com-public/giphy1.gif",
    "https://s3.us-east-2.amazonaws.com/johnvold.com-public/giphy2.gif",
    "https://s3.us-east-2.amazonaws.com/johnvold.com-public/giphy3.gif",
    "https://s3.us-east-2.amazonaws.com/johnvold.com-public/giphy4.gif"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
