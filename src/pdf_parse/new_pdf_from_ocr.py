# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-07
# license: MIT
# description:  new pdf from ocr result
# usage:
# notes:

from datetime import datetime
from decimal import Decimal
import json
import os
from pathlib import Path
from typing import List

from borb.license.usage_statistics import UsageStatistics  # type: ignore [import]
from borb.pdf import PDF  # type: ignore [import]
from borb.pdf import Alignment
from borb.pdf import Document
from borb.pdf import HexColor
from borb.pdf import Image
from borb.pdf import Page
from borb.pdf import Paragraph
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont  # type: ignore [import]
from borb.pdf.canvas.geometry.rectangle import Rectangle  # type: ignore [import]
from requests import get as requests_get  # type: ignore [import]


# from borb.pdf.canvas.layout.annotation.square_annotation import SquareAnnotation


class NewPdfFromOcr:
    doc: Document = Document()
    font = None
    font_color = "#ffffff"
    page_ratio = Decimal(1.0)

    time_start = datetime.now()

    def __init__(
        self,
        page_datas: List[dict],
        options: dict = None,
        output_path=None,
    ) -> None:
        """New pdf from ocr result.

        :param page_datas: ocr result page info data, page_datas is list, each item is dict,
        dict keys is: origin_img, json_path.
        :param options: options, dict, keys is: font_link, font, font_color, page_ratio.
        :param output_path: the output path of new pdf file.
        """
        self.output_path = output_path
        self.page_datas = page_datas
        self.options = options

        UsageStatistics.disable()

        if not self.options:
            self.options = {}

        if self.options.get("font_link") in ["", None]:
            self.options["font_link"] = (
                "https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts"
                + "/master/chinese/%E6%A5%B7%E4%BD%93/Kaiti.ttf"
            )

        if self.options.get("page_ratio") and isinstance(self.options.get("page_ratio"), Decimal):
            self.page_ratio = self.options["page_ratio"]

        self.check_page_datas()
        self.check_out_path()

    def add_page(self, page_data: dict) -> None:
        self.check_page_datas()
        self.check_out_path()
        self.page_datas.append(page_data)

    def set_font(self, font_path: str) -> None:
        """Set font. font_path is font file path or font downlink."""
        self.options["font_link"] = font_path  # type: ignore

    def set_output_path(self, output_path: str) -> None:
        self.output_path = output_path
        self.check_out_path()

    def set_page_ratio(self, page_ratio: Decimal) -> None:
        self.page_ratio = page_ratio

    def set_page_datas(self, page_datas: List[dict]) -> None:
        self.page_datas = page_datas
        self.check_page_datas()

    def process(self) -> str:
        """Process all pages and export pdf file."""
        self.time_start = datetime.now()

        print("Start time: ", self.time_start)

        output_pdf_path = os.path.join(self.output_path, f"ocr_pdf_{str(int(datetime.now().timestamp() * 1000))}.pdf")

        # print process info
        print("Total pages: ", len(self.page_datas))
        print("Output pdf path: ", output_pdf_path)

        print("\nStart process all pages.\n")

        self.doc = Document()

        for page_data in self.page_datas:
            self.process_single_page(page_data)

        # store
        with open(output_pdf_path, "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, self.doc)
            # Display the PDF path with color.
            print("The output pdf path is -> ", f"\033[1;32m{output_pdf_path}\033[0m")

        print(f"End process all pages. \n\nEnd time: {datetime.now()} \nTotal time: ", datetime.now() - self.time_start)

        return output_pdf_path

    def process_single_page(self, page_data: dict) -> None:
        """Process single page and add to doc."""
        ocr_result_json = None

        json_path = str(page_data.get("json_path"))
        origin_img = str(page_data.get("origin_img")) if page_data.get("origin_img") else None

        # read json file from ocr result
        with open(json_path, "r") as f:
            ocr_result_json = json.load(f)

        if not ocr_result_json or not ocr_result_json.get("chars"):
            return

        pdf_size_ratio = self.page_ratio

        page_width = Decimal(ocr_result_json.get("width")) * pdf_size_ratio
        page_height = Decimal(ocr_result_json.get("height")) * pdf_size_ratio

        # Create Page.
        page: Page = Page(width=page_width, height=page_height)

        # Add Page to Document.
        self.doc.add_page(page)

        # Add pic to page.
        if origin_img and os.path.exists(origin_img):
            bg_img_position: Rectangle = Rectangle(
                0,
                0,
                page_width,
                page_height,
            )

            # add an Image
            Image(
                Path(origin_img),
                width=page_width,
                height=page_height,
                padding_bottom=0,
                padding_top=0,
                padding_left=0,
                padding_right=0,
                margin_bottom=0,
                margin_top=0,
                margin_left=0,
                margin_right=0,
            ).paint(page, bg_img_position)

        def_char = "|"

        for _index, _word in enumerate(ocr_result_json["chars"]):
            ocr_char = _word["ocr_txt"]
            char_pos_x = Decimal(_word["x"]) * pdf_size_ratio
            char_pos_y = Decimal(_word["y"]) * pdf_size_ratio
            char_width = Decimal(_word["w"]) * pdf_size_ratio
            char_height = Decimal(_word["h"]) * pdf_size_ratio

            char_pdf_position: Rectangle = Rectangle(
                Decimal(char_pos_x),
                page_height - Decimal(char_pos_y) - Decimal(char_height),
                Decimal(char_width),
                Decimal(char_height),
            )

            # page.add_annotation(SquareAnnotation(char_pdf_position, stroke_color=HexColor("#ff0000")))

            p_font_size = (char_width if char_width > char_height else char_height) * Decimal(0.97)

            def paint_char(_ocr_txt, _char_pdf_position, _p_font_size):
                Paragraph(
                    _ocr_txt,
                    horizontal_alignment=Alignment.CENTERED,
                    vertical_alignment=Alignment.MIDDLE,
                    text_alignment=Alignment.CENTERED,
                    font=self.font,
                    font_color=HexColor(self.font_color) if self.font_color else HexColor("#ffffff"),
                    font_size=_p_font_size,
                ).paint(page, _char_pdf_position)

            try:
                paint_char(ocr_char, char_pdf_position, p_font_size)
            except Exception as e:
                print(f"paint char {ocr_char} error: ", e)
                print(f"will paint default char {def_char} replace {ocr_char}")
                paint_char(def_char, char_pdf_position, p_font_size)

    def check_page_datas(self) -> None:
        """Check page_datas."""
        if not isinstance(self.page_datas, List):
            raise Exception("page_datas is not list.")
        if len(self.page_datas) == 0:
            raise Exception("page_datas is empty.")
        for page_data in self.page_datas:
            if not isinstance(page_data, dict):
                raise Exception("page_data is not dict.")
            if not page_data.get("json_path"):
                raise Exception("page_data json_path is empty.")
            if not os.path.exists(str(page_data.get("json_path"))):
                raise Exception("page_data json_path not exist.")

    def load_font(self) -> None:
        """Custom font setting.

        Font download link:https://fonts.google.com/.
        Font Link Example: 宋体 https://github.com/google/fonts/raw/main/ofl/msmadi/MsMadi-Regular.ttf
        https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts/master/chinese/%E5%AE%8B%E4%BD%93/STSong.ttf
        楷体： https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts/master/chinese/%E6%A5%B7%E4%BD%93/Kaiti.ttf

        :return: None
        """
        if not self.options or not isinstance(self.options, dict) or not self.options.get("font_link"):
            return

        font_link = str(self.options.get("font_link"))

        print("Start load custom font.")
        # If font_link is not empty, then download font and set font.
        if font_link and isinstance(font_link, str) and font_link.startswith("http"):
            # Set font download path.
            font_path = os.path.join(os.path.dirname(__file__), "_cache", "fonts")
            if not os.path.exists(font_path):
                os.makedirs(font_path)
            # Font file save name.
            font_file_name = os.path.join(font_path, font_link.split("/")[-1])

            can_load = True
            if not os.path.exists(font_file_name):
                print(f"Start download font file: {font_link}.")

                with open(font_file_name, "wb") as font_file_handle:
                    _reponse = requests_get(font_link, stream=True)
                    if _reponse.status_code == 200:
                        font_file_handle.write(_reponse.content)
                    else:
                        print(
                            f"Download font file {font_link} error. Status code: {_reponse.status_code}. pass download."
                        )
                        can_load = False
            self.font = TrueTypeFont.true_type_font_from_file(Path(font_file_name)) if can_load else self.font
        elif os.path.exists(font_link):
            self.font = TrueTypeFont.true_type_font_from_file(Path(font_link))
        print("Load custom font done.")

    def check_out_path(self) -> None:
        if not self.output_path:
            self.output_path = os.path.join(
                os.path.dirname(__file__), "_cache", str(int(datetime.now().timestamp() * 1000))
            )
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


def test_new_pdf_from_ocr():  # pragma: no cover
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    json_path = os.path.join(root_dir, "public/attachments/pdf/ocr/ocr_result.json")
    origin_img_path = os.path.join(root_dir, "public/attachments/pdf/ocr/test2.jpeg")

    page_datas = [{"json_path": json_path, "origin_img": origin_img_path}]
    pdf_ocr = NewPdfFromOcr(
        page_datas=page_datas,
        options={
            "page_ratio": Decimal(3.0),
        },
    )
    pdf_ocr.load_font()
    pdf_ocr.process()


if __name__ == "__main__":  # pragma: no cover
    test_new_pdf_from_ocr()
