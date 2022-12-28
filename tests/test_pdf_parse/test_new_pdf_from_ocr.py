# -*- coding: utf-8 -*-
import datetime
from decimal import Decimal
import os

import pytest

from pdf_parse import new_pdf_from_ocr
import test_pdf_parse as tpp


DEF_PAGE_DATA = dict(
    {
        "json_path": os.path.join(tpp.project_root_dir, "public/attachments/pdf/ocr/ocr_result.json"),
        "origin_img": os.path.join(tpp.project_root_dir, "public/attachments/pdf/ocr/test2.jpeg"),
    }
)


def test_new_pdf_from_ocr_with_option_page_ratio():
    page_datas = [DEF_PAGE_DATA]
    new_pdf_from_ocr.NewPdfFromOcr(
        page_datas=page_datas,
        options={
            "page_ratio": Decimal(2.0),
        },
    )


@pytest.mark.parametrize(
    "page_datas",
    [[], "", [DEF_PAGE_DATA, ""], [DEF_PAGE_DATA, {}], [DEF_PAGE_DATA, {"json_path": "test.json"}]],
)
def test_new_pdf_from_ocr_p3(page_datas):
    with pytest.raises(Exception) as e:
        new_pdf_from_ocr.NewPdfFromOcr(page_datas=page_datas)
    exec_msg = e.value.args[0]
    assert len(exec_msg) > 0


def test_new_pdf_from_ocr():
    page_datas = [DEF_PAGE_DATA]
    new_ocr = new_pdf_from_ocr.NewPdfFromOcr(page_datas=page_datas)

    new_ocr.add_page(DEF_PAGE_DATA)
    new_ocr.set_output_path(os.path.join(tpp.test_dist_path, "test_new_pdf_from_ocr"))
    new_ocr.set_page_ratio(Decimal(2.0))
    new_ocr.set_page_datas(page_datas)

    new_ocr.set_font(
        "https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts"
        + f"/master/chinese/%E5%AE%8B%E4%BD%93/STSong{str(datetime.datetime.now().timestamp())}.ttf"
    )
    new_ocr.load_font()

    new_ocr.set_font(
        "https://raw.githubusercontent.com/Haixing-Hu/latex-chinese-fonts"
        + "/master/chinese/%E5%AE%8B%E4%BD%93/STSong.ttf"
    )

    new_ocr.load_font()

    new_ocr.process()
