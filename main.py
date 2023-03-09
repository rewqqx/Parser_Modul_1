from htmlparser import HTMLparser, pdf2html, doc2html

if __name__ == "__main__":
    HTMLparser(pdf2html('../files', 'sample')).save_to_json('sample', '../files')
    HTMLparser(doc2html('../files', 'test')).save_to_json('test', '../files')