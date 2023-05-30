import sys
import webbrowser
from pathlib import Path
from datetime import datetime, timedelta

file_path = Path('tempDate.tmp')
urlDate = ''
if file_path.is_file():
    with open(file_path, 'r') as file:
        file_date = file.readline().strip()
        print('file_date:' + file_date)
        file.close()
    if not file_date == '':
        date = datetime.strptime(file_date, "%Y-%m-%d")
        new_date = date + timedelta(days=1)
        urlDate = new_date.strftime("%Y/%m/%d")
    print('urlDate:' + urlDate)

if urlDate == '':
    print('In No File Exists/Empty area')
    today = datetime.today()
    if len(sys.argv) == 2:
        satDate = datetime.today() - timedelta(days=int(sys.argv[1]))
        urlDate = satDate.strftime("%Y/%m/%d")
    else:
        urlDate = today.strftime("%Y/%m/%d")
    print('today:' + today)
    print('urlDate:' + urlDate)

webbrowser.open("https://gocomics.com/9chickweedlane/" + urlDate)
webbrowser.open("https://gocomics.com/arloandjanis/" + urlDate)
webbrowser.open("https://gocomics.com/brewsterrockit/" + urlDate)
webbrowser.open("https://gocomics.com/dicktracy/" + urlDate)
webbrowser.open("https://gocomics.com/doonesbury/" + urlDate)
webbrowser.open("https://gocomics.com/getfuzzy/" + urlDate)
webbrowser.open("https://gocomics.com/libertymeadows/" + urlDate)
webbrowser.open("https://gocomics.com/luann/" + urlDate)
webbrowser.open("https://gocomics.com/nonsequitur/" + urlDate)
webbrowser.open("https://gocomics.com/peanuts/" + urlDate)
webbrowser.open("https://gocomics.com/meaningoflila/" + urlDate)
webbrowser.open("https://gocomics.com/bloom-county/" + urlDate)
webbrowser.open("https://gocomics.com/fowl-language/" + urlDate)
webbrowser.open("https://gocomics.com/foxtrot/" + urlDate)
webbrowser.open("https://gocomics.com/lay-lines/" + urlDate)
webbrowser.open("https://gocomics.com/pigborn/" + urlDate)
webbrowser.open("https://gocomics.com/redmeat/" + urlDate)
webbrowser.open("https://gocomics.com/sarahs-scribbles/" + urlDate)

today = datetime.today()
with open(file_path, 'w') as file:
    file.write(today.strftime("%Y-%m-%d"))
    file.close()


