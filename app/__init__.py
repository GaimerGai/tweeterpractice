# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from .form.form import TweetForm
import random
# !!START SILENT
from datetime import date
# !!END

app = Flask(__name__)

@app.route("/")
def index():

  random_tweet = random.choice(tweets)

  return render_template("index.html", tweet = random_tweet)

@app.route("/feed")
def feed():

  return render_template("feed.html", tweets = tweets)

@app.route("/new", methods=["GET", "POST"])
def new_tweet_form():
    """
    Displays the Tweet form on GET requests, and then
    validates and creates a new Tweet on POST requests
    """
    form = TweetForm()
    # !!START SILENT
    if form.validate_on_submit():
        new_tweet = {
            'id': len(tweets),
            'author': form.data['author'],
            'tweet': form.data['tweet'],
            'date': date.today(),
            'likes': 0,
        }
        print(new_tweet)
        tweets.append(new_tweet)
        return redirect("/feed", 302)

    if form.errors:
        return form.errors
    # !!END
    return render_template("new_tweet.html", form=form)


app.config.from_object(Config)
# !!END
