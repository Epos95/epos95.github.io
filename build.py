#!/usr/bin/env python3

from jinja2 import Template
import sys
import json
import os

with open("data.json", "r") as f:
    DATA = json.load(f)

def get_html(fname):

    with open(f"templates/{fname}", "r") as f:
        file_contents = f.read()

    # Create Template Object
    template = Template(file_contents)

    return template.render(data = DATA)

def populate_articles():
    DATA["articles"] = []

    a = os.listdir("templates")
    a.remove("index.html")

    for article in a:
        name = article.replace("_", " ").replace(".html", "")
        art = {
            "link" : article,
            "name" : name
        }

        DATA["articles"].append(art)

if __name__ == "__main__":

    populate_articles()
    print(f"Found articles: {DATA['articles']}")

    # Create html for the articles
    articles = os.listdir("templates")
    for article in articles:
        html = get_html(article)

        with open(article, "w+") as f:
            f.write(html)
            print(f"Created {article}")
