import sys, fitz  
import os

fname = '9706_s20_ms_12.pdf'  

base_img_dir = "src\paper_cache\images/"
base_pdf_dir = "src\paper_cache\pdf/"

'''
Also note to self: I'll prolly add some intelligent way to pdf manage 
'''

def convert_to_png(file_name):    
    
    raw_name = file_name.split('.')[0]
    pdf_dir = f'{base_pdf_dir}{file_name}'
    img_dir = f'{base_img_dir}{raw_name}/'

    if not os.path.exists(img_dir):
        print(f"Dir not found {raw_name}...")
        print(f'making dir {raw_name} ...')
        os.mkdir(img_dir)

    else:
        print('Dir already exists')
        img_dir = img_dir 

    doc = fitz.open(pdf_dir)  
    for page in doc:  
        pix = page.get_pixmap(matrix= fitz.Matrix(2.0, 2.0)) 
        pix.save(f"{img_dir}page-%i.png" % page.number)

convert_to_png(fname)