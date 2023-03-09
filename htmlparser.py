import json

from bs4 import BeautifulSoup
from files import clean_text, pdf2html, doc2html


class HTMLparser():
    def __init__(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self.links = self.get_links(soup)
        self.raw_text = soup.get_text()
        self.clean_text = clean_text(self.raw_text)
        self.soup = soup

    def get_links(self, soup):
        links = []
        for link in soup.findAll(['a', 'link']):
            links.append(link.extract().get('href'))
        return links

    def save_to_json(self, filename, output):
        json_data = {"raw_text": self.raw_text, "links": self.links,
                     "soup_str": str(self.soup)}
        with open(f"{output}/{filename}.json", "w", encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)


file = open("../files/output.html")

HTMLparser(pdf2html('../files', 'sample')).save_to_json('sample', '../files')
