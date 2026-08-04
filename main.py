import feedparser
import requests
import xml.etree.ElementTree as ET
from pprint import pprint
#
# source_list = []
# with open("source.txt", "r") as source_file:
#     for line in source_file:
#         source_list.append(line)

# response = requests.get('https://www.reddit.com/r/jeeneeTards.rss')
# tree = ET.fromstring(response.content)
# for child in tree.iter():
#     print(child.tag, '\n', "-"*20)


# pprint(tree)

def get_feed_info(url):
    d = feedparser.parse(url)
    print("Source link: ",d.feed.link)
    print("Source details: ", d.feed.subtitle)
    print("Source name: ", d.feed.title)
    print("Source type: ", d.feed.links[0].type)
    print("Updated: ", d.feed.updated)
    print("-"*40)
    for item in d.entries:
        print(item.title, "\n", item.link, "\n", )
        try:
            print(item.content)
        except:
            print(item.link)


url_list = ['https://reddit.com/r/jeeneetards.rss', 'https://www.sebi.gov.in/sebirss.xml']

get_feed_info(url_list[0])
get_feed_info(url_list[1])