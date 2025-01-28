import sys
import webbrowser
import urllib3

from pathlib import Path
from datetime import datetime, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def display_webpage(urlDate, website):
    full_website = website + urlDate
    print(full_website)
    resp = urllib3.request("GET", full_website)
    if resp.status == 200:
        webbrowser.open(full_website)
    else:
        print(full_website + " doesn't exist")


daily_websites = ["https://gocomics.com/9chickweedlane/",
                  "https://gocomics.com/arloandjanis/",
                  "https://gocomics.com/brewsterrockit/",
                  "https://gocomics.com/doonesbury/",
                  "https://gocomics.com/getfuzzy/",
                  "https://gocomics.com/libertymeadows/",
                  "https://gocomics.com/luann/",
                  "https://gocomics.com/nonsequitur/",
                  "https://gocomics.com/peanuts/",
                  "https://gocomics.com/meaningoflila/",
                  "https://gocomics.com/fowl-language/",
                  "https://gocomics.com/sarahs-scribbles/"]

sunday_websites = ["https://gocomics.com/foxtrot/"]

monday_websites = ["https://gocomics.com/lay-lines/"]

file_path = Path('tempDate.tmp')
urlDate = ''
start_date = datetime.today()

if file_path.is_file():
    with open(file_path, 'r') as file:
        file_date = file.readline().strip()
        print('file_date:' + file_date)

    if not file_date == '':
        start_date = datetime.strptime(file_date, "%Y-%m-%d")
        start_date = start_date + timedelta(days=1)

for single_date in daterange(start_date, (datetime.today()+timedelta(days=1))):
    urlDate = single_date.strftime("%Y/%m/%d")
    print('urlDate:' + urlDate)

    for website in daily_websites:
        display_webpage(urlDate, website)

    if single_date.weekday() == 6:
        for website in sunday_websites:
            display_webpage(urlDate, website)

    if single_date.weekday() == 0:
        for website in monday_websites:
            display_webpage(urlDate, website)

today = datetime.today()
with open(file_path, 'w') as file:
    file.write(today.strftime("%Y-%m-%d"))
