from bs4 import BeautifulSoup as bs
import requests as r

class Scraper():


    def __init__(self):
        self.title, self.artist, self.album, self.show  = self.scrape()

    def update(self):
        self.title, self.artist, self.album, self.show  = self.scrape()

    """
    return eturns the current playing song as 3 strings.
    format: Title, Artist, Album, Show
    """
    def scrape(self):
        html = r.get("https://www.wrek.org/playlist/").text
        soup = bs(html, 'html.parser')
        output = soup.find_all('td')[1:4]
        for i, j in enumerate(output):
            output[i] = j.text

        output.append(self.specialtyscrape())
        print(output)
        return output[0], output[1], output[2], output[3]

    def schedule(self):
        html = r.get('https://www.wrek.org/schedule/').text
        soup = bs(html, 'html.parser')
        sched = []
        for t in soup.select(".schedule-list"):
            sched.append(t.select(".schedule-entry"))
        out= [[], [], [], [], [], [], []]
        for i, c in enumerate(sched[:-1]):
            for j in c:
                type = ''
                if 'schedule-specialty' in j['class']:
                    type = 'Speciaty Show'
                elif 'schedule-oto' in j['class']:
                    type = 'Sports'
                elif 'schedule-block' in j['class']:
                    type = 'Block'
                elif 'schedule-pubaff' in j['class']:
                    type = 'Public Affairs'
                else:
                    type = '???'
                out[i].append({'type':type,
                               'time':str(j.select(".schedule-time")[0].string),
                               'name':str(j.a.string)})
        return out

    def specialtyscrape(self):
    	html = r.get('https://www.wrek.org/').text
    	soup = bs(html, 'html.parser')
    	show = soup.find(id='current')
    	return show.a.text
