# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-02
# license: MIT
# description: Multi pdf parse.
# usage: poetry run python src/pdf_parse/multi_pdf_parse.py
# notes:

import argparse
from datetime import datetime
import os
import random

from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter


class MultiPDFParse:
    """Multi pdf parse class."""

    def __init__(self, pdf_files, output_path=None) -> None:
        """Pass pdf files to be some parse and output dir.

        :param pdf_files: pdf files to be some parse
        :param output_path: parse files output path
        """
        self.pdf_files = pdf_files
        self.output_path = output_path

        self.check_file()
        self.check_out_path()

    def merge_pdf(self) -> str:
        """Merge pdf files."""
        merger = PdfMerger()
        merge_pdf_path = os.path.join(self.output_path, f"merge_{str(int(datetime.now().timestamp() * 1000))}.pdf")

        for pdf_file in self.pdf_files:
            input_file = open(pdf_file, "rb")
            merger.append(input_file)

        merger.write(merge_pdf_path)
        merger.close()

        print(f"\033[1;32mmerge pdf files to {merge_pdf_path}\033[0m")

        # return merge pdf file path
        return merge_pdf_path

    def be_multi_layer(self) -> str:
        """Merge pdf_files be multi-layer pdf file."""
        multi_layer_pdf_path = os.path.join(
            self.output_path, f"multi_layer_dist_{str(int(datetime.now().timestamp() * 1000))}.pdf"
        )

        print("Strat merge pdf files to multi layer pdf file...")

        # clone first pdf file as base multi layer pdf file
        base_pdf = PdfReader(self.pdf_files[0])
        # under pdf page num
        base_pdf_page_num = len(base_pdf.pages)

        pdf_write = PdfWriter()

        # foreach pdf_files to be multi layer
        for pf_index, pdf_file in enumerate(self.pdf_files):
            # if first pdf file, skip
            if pf_index == 0:
                continue

            # read pdf file
            cur_pdf_reader = PdfReader(pdf_file)
            # get page count
            cur_pdf_page_count = len(cur_pdf_reader.pages)

            # foreach page to be multi layer
            for pdf_page_index in range(0, base_pdf_page_num, 1):
                base_page = base_pdf.pages[pdf_page_index]

                # if current pdf page less then current pdf page count, merge page
                if pdf_page_index < cur_pdf_page_count:
                    base_page_mediabox = base_page.mediabox
                    top_page = cur_pdf_reader.pages[pdf_page_index]
                    base_page.merge_page(top_page)
                    base_page.mediabox = base_page_mediabox

                pdf_write.add_page(base_page)

        with open(multi_layer_pdf_path, "wb") as fp:
            pdf_write.write(fp)
            print(f"\033[1;32mmultipdf file to {multi_layer_pdf_path}\033[0m")

        return multi_layer_pdf_path

    def check_file(self) -> None:
        for pdf_file in self.pdf_files:
            if not os.path.exists(pdf_file):
                raise FileNotFoundError(f"file {pdf_file} not found")
            if not pdf_file.endswith(".pdf"):
                raise ValueError(f"file {pdf_file} is not pdf file")

    def check_out_path(self):

        if self.output_path in ["", None]:
            self.output_path = os.path.join(
                os.path.dirname(__file__), "_cache", str(int(datetime.now().timestamp() * 1000))
            )
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


# get path top level directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
attachment_dir = os.path.join(root_dir, "public/attachments/pdf")
txt_pdf_path = os.path.join(attachment_dir, "whatispython.pdf")
pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")


def test_merge_pdf() -> None:
    """Test merge pdf files."""
    # fill pdf files
    pdf_files = []
    for _item in range(random.randint(3, 12)):
        pdf_files.append(txt_pdf_path)
        if random.randint(0, 1) == 1:
            pdf_files.append(pic_pdf_path)  # pragma: no cover
    # shuffle pdf files
    random.shuffle(pdf_files)

    # merge pdf files
    merge_pdf = MultiPDFParse(pdf_files)
    merge_pdf.merge_pdf()


def test_multi_pdf_to_multi_layer() -> None:
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments/pdf")
    txt_pdf_path = os.path.join(attachment_dir, "whatispython.pdf")
    pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")

    # fill pdf files
    pdf_files = [pic_pdf_path, txt_pdf_path]

    # merge pdf files
    multi_pdf = MultiPDFParse(pdf_files)
    multi_pdf.be_multi_layer()


def main() -> None:  # pragma: no cover
    # use "-i" got pdf files, use "-o" got output directory
    parser = argparse.ArgumentParser(description="Multi pdf parse.")
    parser.add_argument("-m", "--mode", help="Mode: merge-pdf、multi-pdf", default="merge-pdf")
    parser.add_argument("-i", "--input", help="input pdf files", nargs="+", required=False)
    parser.add_argument("-o", "--output", help="output directory", required=False)

    args = parser.parse_args()

    mode = args.model if not args.mode and args.mode in ["merge-pdf", "multi-pdf"] else "merge-pdf"
    pdf_files = args.input
    output_dir = args.output

    # if args not set, use stdin to get pdf files and output directory
    if pdf_files is None:
        pdf_files = input("input pdf files path, split by space: ").split(" ")
    if output_dir is None:
        output_dir = input("input output directory: ")

    merge_pdf = MultiPDFParse(pdf_files, output_dir)
    if mode == "merge-pdf":
        merge_pdf.merge_pdf()
    elif mode == "multi-pdf":
        merge_pdf.be_multi_layer()


if __name__ == "__main__":
    main()  # pragma: no cover
