import click
from pathlib import Path
from htmlparser import HTMLparser, pdf2html, doc2html, djvu2txt
from files import txt2json


def edit_path(path):
    return path.replace('/' + Path(path).name, '')


@click.command()
@click.option('--path_input', prompt='Path to file input')
@click.option('--path_output', prompt='Path to file output')
def run(path_input, path_output):
    if Path(path_input).suffix == '.pdf':
        HTMLparser(pdf2html(edit_path(path_input), Path(path_input).stem)).save_to_json(Path(path_output).stem,
                                                                                          edit_path(path_output))

    elif Path(path_input).suffix == '.doc' or Path(path_input).suffix == '.docx':
        HTMLparser(doc2html(edit_path(path_input), Path(path_input).stem)).save_to_json(Path(path_output).stem,
                                                                                          edit_path(path_output))

    elif Path(path_input).suffix == '.djvu':
        txt2json(djvu2txt(edit_path(path_input), Path(path_input).stem), path_output, edit_path(path_output))

    elif Path(path_input).suffix == '.html':
        HTMLparser(open(f"{path_input}").read()).save_to_json(Path(path_output).stem, edit_path(path_output))


run()
