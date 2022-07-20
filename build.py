#!/usr/bin/env python3

from jinja2 import Template
import sys
import json
import os

# Populate DATA with the predetermined data from data.json
with open("data.json", "r") as f:
    DATA = json.load(f)

# Read header into DATA
with open("utils/header.html") as f2:
    DATA["header"] = f2.read()
    #DATA["HEADER"] = DATA["header"].replace("{{data['date']}}", "TEST")


# Gets the rendered html string from a html document
def get_html(fname):
    with open(f"templates/{fname}", "r") as f:
        file_contents = f.read()

    # Create Template Object
    template = Template(file_contents)

    return template.render(data = DATA)

# Puts data regarding all the articles into DATA
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

    # Print the articles we are about to publish
    print("Found articles:")
    for article in DATA["articles"]:
        print(f" * href: {article['link']}\n   name: {article['name']}\n")

    # Create html for the articles and write it too disk for easy access when publishing
    articles = os.listdir("templates")
    for article in articles:
        html = get_html(article)

        with open(article, "w+") as f:
            f.write(html)

        print(f"Created {article}")
