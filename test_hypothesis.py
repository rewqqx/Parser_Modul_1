import random

import filecmp
import aspose.words as aw
from pathlib import Path

import unittest
from hypothesis import given, settings
import hypothesis.strategies as st

from files import clean_ad, clean_text, pdf2html, doc2html, djvu2txt
from htmlparser import HTMLparser


class StaffTestCases(unittest.TestCase):
    ads = ['Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.',
           'Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/']

    bad_simbols = ['.', '*', '?']

    def get_random_bad_substr(self):
        variants = self.bad_simbols.copy()
        variants.append('')
        return f"<{random.choice(variants)}{random.choice(variants)}{random.choice(variants)}>"

    def get_random_mixed_text(self, text):
        return text + self.get_random_bad_substr() + text + self.get_random_bad_substr()

    @given(st.text())
    def test_clean_ad(self, initial_text):
        test_text_value = initial_text + self.ads[0] + initial_text + self.ads[1]
        expected_result = initial_text + initial_text
        self.assertEqual(clean_ad(test_text_value), expected_result)

    @given(st.text())
    def test_clean_text(self, initial_text):
        for i in range(10):
            self.assertEqual(clean_text(self.get_random_mixed_text(initial_text)),
                             clean_text(self.get_random_mixed_text(initial_text)))


class PdfTestCases(unittest.TestCase):
    base_file_name = './test_files/test_pdf.pdf'
    expected_file_name = './test_files/expected_pdf.html'

    empty_text_file_name = './test_files/empty_pdf.pdf'

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_base_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(empty_text_file_name))
    @settings(deadline=None)
    def test_empty_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(empty_text_file_name))
    @settings(deadline=None)
    def test_empty_file_empty_content(self, test_file_name):
        html = HTMLparser(pdf2html(test_file_name))
        self.assertEqual(html.clean_text.replace('\xa0', ''), '')

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_correct_processing(self, test_file_name):
        HTMLparser(pdf2html(test_file_name))

        filename = Path(test_file_name)
        result = filecmp.cmp(str(filename.with_suffix(".html")), self.expected_file_name)
        self.assertTrue(result)


class DocTestCases(unittest.TestCase):
    base_file_name = './test_files/test_doc.doc'
    expected_file_name = './test_files/expected_doc.html'

    empty_text_file_name = './test_files/empty_doc.doc'

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_base_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(empty_text_file_name))
    @settings(deadline=None)
    def test_empty_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(empty_text_file_name))
    @settings(deadline=None)
    def test_empty_file_empty_content(self, test_file_name):
        html = HTMLparser(doc2html(test_file_name))
        self.assertEqual(html.clean_text.replace('\xa0', ''), '')

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_correct_processing(self, test_file_name):
        HTMLparser(doc2html(test_file_name))

        filename = Path(test_file_name)
        result = filecmp.cmp(str(filename.with_suffix(".html")), self.expected_file_name)
        self.assertTrue(result)


class DjvuTestCases(unittest.TestCase):
    base_file_name = './test_files/test_djvu.djvu'
    expected_file_name = './test_files/expected_djvu.txt'

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_base_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_correct_processing(self, test_file_name):
        djvu2txt(test_file_name)

        filename = Path(test_file_name)
        result = filecmp.cmp(str(filename.with_suffix(".txt")), self.expected_file_name)
        self.assertTrue(result)


class HtmlTestCases(unittest.TestCase):
    base_file_name = './test_files/test_html.html'
    empty_text_file_name = './test_files/empty_html.html'

    @given(st.just(base_file_name))
    @settings(deadline=None)
    def test_base_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(empty_text_file_name))
    @settings(deadline=None)
    def test_empty_file_opening(self, test_file_name):
        self.assertIsNotNone(aw.Document(test_file_name))

    @given(st.just(empty_text_file_name))
    @settings(deadline=None)
    def test_empty_file_empty_content(self, test_file_name):
        with open(test_file_name) as f:
            html = HTMLparser(f.read())
        self.assertEqual(clean_ad(html.clean_text).replace('\xa0', ''), '')


if __name__ == '__main__':
    unittest.main()
