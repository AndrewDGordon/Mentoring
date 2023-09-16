# my experiments on Saturday 16 September
# in terminal say, OPENAI_KEY=sk-..., followed by export OPENAI_KEY

import json
import pandas as pd
import numpy as np
import requests
import os

# need to do "pip install openai" in the terminal
import openai

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

print("Hello there!")

# Get the value of the environment variable named OPENAI_KEY
openai_key = os.environ.get("OPENAI_KEY")

# Check if the environment variable exists and has a valid value
if openai_key:
    # Set the openai.api_key attribute to the value of the environment variable
    openai.api_key = openai_key

    # Print a success message
    print("OpenAI key loaded successfully")
else:
    # Print an error message
    print("OpenAI key not found or invalid")

# Define the url of the html page to download
url1 = "https://www.thenational.scot/news/23299549.posie-parker-anti-trans-founder-standing-women/"
url2 = "https://www.independent.co.uk/arts-entertainment/books/news/graham-linehan-book-richard-ayoade-jonathan-ross-b2411390.html"
url = "https://www.telegraph.co.uk/news/2023/09/14/trans-activists-cancel-ayoade-backing-linehan/"

# Send a GET request to the url and store the response object
response = requests.get(url)

print(response)

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# Check if the response status code is 200 (OK)
if response.status_code == 200:

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, "html.parser")

    texts = soup.findAll(string=True)
    visible_texts = filter(tag_visible, texts)
    text = " ".join(t.strip() for t in visible_texts)

else:
    # Print an error message if the response status code is not 200
    print(f"Error: Could not download the html page from {url}")

# Print the main body string
print(text)

completion = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[{"role":"user", "content": "Make a JSON array of strings where each string is a description of the protagonist in the following. Each description should be the exact words from the text.  Be scrupulous. "+text}])

# Print the first generated text from the completion object
print(completion.choices[0])

json_text = completion.choices[0]["message"]["content"]
#print(json_text)
data = json.loads(json_text)
for text in data:
    print(text)