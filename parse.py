import click
from pathlib import Path
from htmlparser import HTMLparser, pdf2html, doc2html, djvu2txt
from files import txt2json


@click.command()
@click.option('-i', '--path_input', prompt='Path to input file', type=Path)
@click.option('-o', '--path_output', prompt='Path to output file', type=Path)
def run(path_input: Path, path_output: Path):
    match path_input.suffix:
        case '.pdf':
            html_text = pdf2html(path_input)
            HTMLparser(html_text).save_to_json(path_output)
        case ('.docx', '.doc'):
            html_text = doc2html(path_input)
            HTMLparser(html_text).save_to_json(path_output)
        case '.djvu':
            txt_text = djvu2txt(path_input)
            txt2json(txt_text, path_output)
        case '.html':
            with open(path_input, mode="r", encoding="utf-8") as html_file:
                html_text = html_file.read()
                HTMLparser(html_text).save_to_json(path_output)
        case _:
            raise ValueError("Not pdf/djvu/doc(x)/html file. Unable to parse")


if __name__ == "__main__":
    run()
