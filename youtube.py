import re #This module will help us to fetch the link from html text
import requests #This module will help us to fetch the html text from search webpage
import webbrowser as wb #This will open our url automatically

video_name = input("Enter a video name:")
web_url = "https://www.youtube.com/results?search_query=" + "+".join(video_name.split())

html_content = requests.get(web_url)

content = html_content.text

link = re.findall("videoId\":\"(.{11})",content)
final_link = "https://www.youtube.com/watch?v=" + link[0]
wb.open(final_link)
