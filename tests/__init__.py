# -*- coding: utf-8 -*-
import pytest

from pdf_parse import single_pdf_parse
import test_pdf_parse as tpp


def test_pdf_file_not_found():
    with pytest.raises(FileNotFoundError) as e:
        extract_pdf_images.ExtractPdfImages("test_extract_pdf_images.pdf")
    exec_msg = e.value.args[0]
    assert exec_msg == "file test_extract_pdf_images.pdf not found"


def test_not_pdf_file():
    with pytest.raises(ValueError) as e:
        extract_pdf_images.ExtractPdfImages(__file__)
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


@pytest.mark.test_extract_pdf_images
@pytest.mark.parametrize("output_path", [tpp.test_dist_path, ""])
def test_extract_pdf_images(output_path):
    # extract pdf images
    extract_pdf_images.ExtractPdfImages(tpp.demo_pic_pdf_path, output_path).extract()


def test_extract_demo():
    """Test extract demo."""
    extract_pdf_images.test_extract_pdf_images()
