from urllib import request

import bs4  # Beautiful Soup for Web Scraping
from win10toast import ToastNotifier

toaster = ToastNotifier()

url = "http://www.cricbuzz.com/cricket-match/live-scores"

sauce = request.urlopen(url).read()
soup = bs4.BeautifulSoup(sauce, "lxml")

score = []
results = []

for div_tags in soup.find_all('div', attrs={"class": "cb-lv-scrs-col text-black"}):
    score.append(div_tags.text)
for result in soup.find_all('div', attrs={"class": "cb-lv-scrs-col cb-text-complete"}):
    results.append(result.text)

print(score[0], results[0])
toaster.show_toast(title=score[0], msg=results[0])


# Polyline drawing in codeskulptor

import simplegui

polyline = []


def click(pos):
    global polyline
    polyline.append(pos)


def clear():
    global polyline
    polyline = []


def draw(canvas):
    if len(polyline) == 1:
        canvas.draw_point(polyline[0], "White")
    for i in range(1, len(polyline)):
        canvas.draw_line(polyline[i - 1], polyline[i], 2, "White")


frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

frame.start()