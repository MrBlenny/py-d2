# -*- coding: utf-8 -*-
import datetime
import os

import pytest

from pdf_parse import multi_pdf_parse
import test_pdf_parse as tpp


@pytest.fixture(scope="function", autouse=False)
def multi_pdf_parse_function_scope():
    print("multi_pdf_parse before")

    yield

    print("multi_pdf_parse after")


def test_file_not_found():
    pdf_files = [
        "test_multi_pdf_parse.pdf",
    ]
    output_dir = "out_dir"

    with pytest.raises(FileNotFoundError) as e:
        multi_pdf_parse.MultiPDFParse(pdf_files, output_dir).merge()
    exec_msg = e.value.args[0]
    assert exec_msg == "file test_multi_pdf_parse.pdf not found"


def test_file_not_pdf():
    pdf_files = [
        __file__,
    ]
    output_dir = "out_dir"

    with pytest.raises(ValueError) as e:
        multi_pdf_parse.MultiPDFParse(pdf_files, output_dir).merge()
    exec_msg = e.value.args[0]
    assert exec_msg.index("not pdf file") != -1


@pytest.mark.usefixtures("multi_pdf_parse_function_scope")
def test_multi_pdf_parse():
    multi_pdf_parse.MultiPDFParse([tpp.demo_pic_pdf_path, tpp.demo_pic_pdf_path], tpp.test_dist_path).be_multi_layer()


@pytest.mark.usefixtures("multi_pdf_parse_function_scope")
def test_merge_pdf():
    multi_pdf_parse.MultiPDFParse([tpp.demo_pic_pdf_path, tpp.demo_pic_pdf_path], tpp.test_dist_path).merge_pdf()


@pytest.mark.parametrize(
    "output_path",
    [os.path.join(tpp.test_dist_path, f"test_{str(int(datetime.datetime.now().timestamp() * 1000))}"), ""],
)
def test_output_dir_not_exist(output_path):
    multi_pdf_parse.MultiPDFParse(
        [tpp.demo_pic_pdf_path],
        output_path,
    )


def test_multi_pdf_parse_demo_func():
    # test merge pdf def in multi_pdf_parse
    multi_pdf_parse.test_multi_pdf_to_multi_layer()


def test_merge_Pdf():
    # test merge pdf def in multi_pdf_parse
    multi_pdf_parse.test_merge_pdf()


@pytest.mark.test_multi_pdf_parse_main
def test_main():
    pytest.skip("skip test_main")
