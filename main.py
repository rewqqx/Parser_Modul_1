from htmlparser import HTMLparser, pdf2html, doc2html, djvu2txt
from files import txt2json


if __name__ == "__main__":
    HTMLparser(pdf2html('./files/sample.pdf')).save_to_json('./files/sample.json')
    HTMLparser(doc2html('./files/test.doc')).save_to_json('./files/test.json')
    txt2json(djvu2txt('./files/sample1.djvu'), './files/sample1.json')

