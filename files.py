import re
import os

import aspose.words as aw

import json
from pathlib import Path


def pdf2html(filename: str | Path):
    filename = Path(filename)
    doc = aw.Document(str(filename.with_suffix(".pdf")))
    doc.save(str(filename.with_suffix(".html")))
    with open(filename.with_suffix(".html"), "r", encoding='utf-8') as f:
        return clean_ad(f.read())


def doc2html(filename: str | Path):
    filename = Path(filename)
    doc = aw.Document(str(filename.with_suffix(".doc")))
    doc.save(str(filename.with_suffix(".html")))
    with open(filename.with_suffix(".html"), "r", encoding='utf-8') as f:
        return clean_ad(f.read())


def djvu2txt(filename: str | Path):
    filename = Path(filename)
    s = f"djvused {filename.with_suffix('.djvu')} -e print-pure-txt > {filename.with_suffix('.txt')}"
    os.system(s)
    with open(filename.with_suffix(".txt"), "r") as f:
        return clean_ad(f.read())


def txt2json(text, filename: str | Path):
    filename = Path(filename)
    json_data = {"raw_text": text}
    with open(filename.with_suffix(".json"), "w", encoding='utf-8') as f:
        json.dump(json_data, f)


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
