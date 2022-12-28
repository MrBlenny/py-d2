# -*- coding: utf-8 -*-
from datetime import datetime
import os

from PyPDF2.generic import AnnotationBuilder
import pytest

from pdf_parse import single_pdf_parse
import test_pdf_parse as tpp


def test_pdf_file_not_found():
    with pytest.raises(FileNotFoundError) as e:
        single_pdf_parse.SinglePdfParse("test_single_pdf_parse.pdf")
    exec_msg = e.value.args[0]
    assert exec_msg == "file test_single_pdf_parse.pdf not found"


def test_not_pdf_file():
    with pytest.raises(ValueError) as e:
        single_pdf_parse.SinglePdfParse(__file__)
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


@pytest.mark.test_extract_pdf_images
@pytest.mark.parametrize("output_path", [tpp.test_dist_path, ""])
def test_extract_pdf_images(output_path):
    # extract pdf images
    single_pdf_parse.SinglePdfParse(tpp.demo_pic_pdf_path, output_path).extract_images()


def test_export_as_images():
    single_pdf_parse.SinglePdfParse(tpp.demo_pic_pdf_path).export_as_images()


def test_export_as_images_demo():
    single_pdf_parse.test_export_as_images()


# test add annotation
def test_add_annotation():
    output_pdf = os.path.join(tpp.test_dist_path, f"test_add_annotation_{str(int(datetime.now().timestamp() * 1000 ))}")

    free_txt = AnnotationBuilder.free_text(
        "Hello World!",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )

    assert os.path.exists(
        single_pdf_parse.SinglePdfParse(tpp.demo_pic_pdf_path, output_pdf).add_annotation(
            [
                {
                    "page": 0,
                    "annotation": free_txt,
                },
                {
                    "page": 3,
                    "annotation": free_txt,
                },
            ]
        )
    )


def test_extract_images_demo():
    single_pdf_parse.test_extract_images()


def test_add_annotation_demo():
    single_pdf_parse.test_add_annotation()
