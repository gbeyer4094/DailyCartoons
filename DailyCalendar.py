import webbrowser
import datetime
from datetime import date
from datetime import timedelta

today = date.today()
if today.strftime("%A") == 'Monday':
    satDate = date.today() -timedelta(days=3)
    urlDate = satDate.strftime("%Y/%m/%d")

else:
    urlDate = today.strftime("%Y/%m/%d")

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
