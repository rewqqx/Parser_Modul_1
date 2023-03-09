import re
import aspose.words as aw


def pdf2html(path_to_file, file):
    doc = aw.Document(f"{path_to_file}/{file}.pdf")
    doc.save(f"{path_to_file}/{file}.html")
    file = open("../files/output.html")
    return clean_ad(file.read())


def doc2html(path_to_file, file):
    doc = aw.Document(f"{path_to_file}/{file}.doc")
    doc.save(f"{path_to_file}/{file}.html")
    file = open(f"{path_to_file}/{file}.html")
    return clean_ad(file.read())


def clean_ad(text):
    text = text.replace('Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.', '')
    text = text.replace(
        'Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/',
        '')
    return text


def clean_text(raw_text):
    clean = re.compile('<.*?>')
    result = re.sub(clean, '', raw_text)
    return result
