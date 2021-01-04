from gensim.summarization.summarizer import summarize
from tika import parser
from bs4 import BeautifulSoup
import requests
import re
import sys

# Check file type
source = input("Source from file or webpage: ")

if source == "file":
    filename = input("Enter filename (txt or pdf): ")
elif source == "webpage":
    url = input("Enter the url: ")
else:
    print("input not recognized, closing executable")
    input('Press ENTER to exit')
    sys.exit()

# Length of desired summary
num = int(input("Length of desire summary: "))


def parsefromfile(filename):
    extension = re.findall("\.[a-z]*", filename)[0][1:]
    if extension == "pdf":
        raw = parser.from_file(filename)["content"]
    elif extension == "txt":
        raw = open(filename, "r").read()
    else:
        print("file extension not recognized")
        input('Press ENTER to exit')
        sys.exit()

    return summarize(raw, word_count=num)


def parsefromurl(url):
    html = requests.get(url).text
    raw = BeautifulSoup(html,'html.parser').get_text()

    return summarize(raw, word_count=num)


if source == "file":
    summary = parsefromfile(filename)
elif source == "webpage":
    summary = parsefromurl(url)

with open('output.txt', 'w') as f:
    f.write(summary)

print("File generated")

input('Press ENTER to exit')