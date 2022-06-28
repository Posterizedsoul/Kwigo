from gce_scraper import *
import fitz
from typing import Tuple
import os
import requests
import glob, sys, fitz


# print(find_paper(9702, 2020, PaperVariant=12, exam_session= 's', Type= 'qp'))
url, name = find_paper(9702, 2020, PaperVariant=12, exam_session= 's', Type= 'qp')

def downloader(PDF_NAME=name.split('/')[2], PDF_LINK=url):
    try:
        with open(PDF_NAME, 'r') as pdf:
            print('File is already there')
            return 1
    except Exception:
        print('New PDF')
        with open(PDF_NAME, 'wb') as pdf:
            r = requests.get(PDF_LINK)
            pdf.write(r.content)
            print('Downloaded')
            return 0
    except Exception:
        print('Cannot download the PDF {}'.format(PDF_NAME))
downloader()


# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

path = '../data/in/'
all_files = glob.glob(path + "*.pdf")

for filename in all_files:
    doc = fitz.open(filename)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        pix.save("../data/out/page-%i.png" % page.number)  # store image as a PNG