from bs4 import BeautifulSoup as bs
import requests as r

class Scraper():


    def __init__(self):
        self.title, self.artist, self.album  = self.scrape()

    def update(self):
        self.title, self.artist, self.album  = self.scrape()

    """
    return eturns the current playing song as 3 strings.
    format: Title, Artist, Album
    """
    def scrape(self):
        html = r.get("https://www.wrek.org/playlist/").text
        soup = bs(html, 'html.parser')
        output = soup.find_all('td')[1:4]
        for i, j in enumerate(output):
            output[i] = j.text

        return output[0], output[1], output[2]
