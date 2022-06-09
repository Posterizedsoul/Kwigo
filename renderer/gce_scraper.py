import os
import time
import lxml
from regex import A
import requests
import multiprocessing
from typing import Optional

from bs4 import BeautifulSoup

WEB_URL = 'https://papers.gceguide.com/A%20Levels/'

AVAILABLE_SUBJECTS = []
SUBJECT_CODES = []
paper = ''

def subjects(WEB_URL):
    r = requests.get(WEB_URL)
    soup = BeautifulSoup(r.text, 'lxml')
    subject_name= soup.find_all('li', class_ = 'dir')
    for subject in subject_name:
        AVAILABLE_SUBJECTS.append(
            [subject.text, subject.a.get('href').replace(' ', '%20')])    
    #print(AVAILABLE_SUBJECTS)   

def find_paper(subject_code:int, Year:int, PaperVariant: int or None = None,  exam_session= ['s','w','m'], Type= ['sp','ms','qp','er','ir','gt']): 
    '''
    Year: Year | 2002, 2022
    PaperVariant: Paper + Variant | 11, 12 
    Type: Type | MS, QP, ER, GT
    '''
    get_all_subject_codes()
    if subject_code in SUBJECT_CODES:
        try:

            if not Type == 'gt' or not Type == 'er':
                # FORMAT OF PAPER: /2022/9709_m22_ms_12.pdf
                year_code = ''.join(list(str(Year))[:2])
                paper = f'/{Year}/{subject_code}_{exam_session}{year_code}_{Type}_{PaperVariant}.pdf'
            # FORMAT FOR ET AND GT(both are almost same): /9709_m22_gt.pdf
            paper = f'/{subject_code}_{exam_session}{year_code}_{Type}.pdf'
            print(paper)
        except Exception as e:
            print(e)
        return paper 
def get_paper():
    
    pass


def get_all_subject_codes():
    subjects(WEB_URL)
    # print(AVAILABLE_SUBJECTS)
    for subject_code in AVAILABLE_SUBJECTS:
        SUBJECT_CODES.append(int(subject_code[0].split(' ')[-1].replace('(','').replace(')','')))
    print(SUBJECT_CODES.sort())    

find_paper(subject_code = 9702, Year= 2021,exam_session= 'm', Type ='gt')