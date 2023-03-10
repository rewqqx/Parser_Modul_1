from htmlparser import HTMLparser, pdf2html, doc2html, djvu2txt
from files import txt2json

if __name__ == "__main__":
    HTMLparser(pdf2html('../files', 'sample')).save_to_json('sample', '../files')
    HTMLparser(doc2html('../files', 'test')).save_to_json('test', '../files')
    txt2json(djvu2txt('E:\Projects\\test\\files', 'sample1'), 'E:\Projects\\test\\files', 'sample1')
