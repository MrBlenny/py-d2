# -*- coding: utf-8 -*-
import os


project_root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
project_attachment_dir = os.path.join(project_root_dir, "public/attachments")

demo_pic_pdf_path = os.path.join(project_attachment_dir, "pdf/samplepic.pdf")
demo_txt_pdf_path = os.path.join(project_attachment_dir, "pdf/whatispython.pdf")
demo_txt_pdf2_path = os.path.join(project_attachment_dir, "pdf/whatispython2.pdf")
test_dist_path = os.path.join(project_root_dir, "tests/_cache/pdf_parse")

# if test dist path not exist, create it
if not os.path.exists(test_dist_path):
    os.makedirs(test_dist_path)
