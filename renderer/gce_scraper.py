import os
import time
import lxml
import requests
from bs4 import BeautifulSoup
import urllib.request

class PaperNotFound(Exception):
    pass

WEB_URL = 'https://papers.gceguide.com/A%20Levels/'
AVAILABLE_SUBJECTS, SUBJECT_URL = [], []
SUBJECT_CODES = []
paper = ''

def subjects(WEB_URL):
    r = requests.get(WEB_URL)
    soup = BeautifulSoup(r.text, 'lxml')
    subject_name= soup.find_all('li', class_ = 'dir')
    for subject in subject_name:
        AVAILABLE_SUBJECTS.append(subject.text)
        SUBJECT_CODES.append(subject.text.split(' ')[-1].replace('(','').replace(')','')) 
        SUBJECT_URL.append(subject.a.get('href').replace(' ', '%20'))
    subject_dict = zip(SUBJECT_CODES, SUBJECT_URL)
    # pprint.pprint(dict(subject_dict))
    #print(AVAILABLE_SUBJECTS)   
    return dict(subject_dict)


def find_paper(subject_code:int, Year:int, PaperVariant: int or None = None,  exam_session= ['s','w','m'],Type= ['sp','ms','qp','er','ir','gt']): 
    '''
    Year: Year | 2002, 2022
    PaperVariant: Paper + Variant | 11, 12 
    Type: Type | MS, QP, ER, GT
    '''
    subjects_ = subjects(WEB_URL)
    if str(subject_code) in SUBJECT_CODES:
        try:
            if not Type == 'gt' or not Type == 'er':
                # FORMAT OF PAPER: /2022/9709_m22_ms_12.pdf
                year_code = ''.join(list(str(Year))[:2])
                paper = f'/{Year}/{subject_code}_{exam_session}{year_code}_{Type}_{PaperVariant}.pdf'
                
            # FORMAT FOR ET AND GT(both are almost same): /9709_m22_gt.pdf
            else:
                paper = f'/{subject_code}_{exam_session}{year_code}_{Type}.pdf'

        except PaperNotFound:
            return
        # FORMAT OF PAPER URL: https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/2021/9701_m21_qp_42.pdf
        paper_url = f"{WEB_URL}{subjects_[f'{subject_code}']}{paper}"
        # print(paper_url)
        # Expected output  find_paper(9702, 2020, PaperVariant=12, exam_session= 's', Type= 'qp')
        #                : https://papers.gceguide.com/A%20Levels/Physics%20(9702)/2020/9702_s20_qp_12.pdf
        return paper_url, paper
# find_paper(9702, 2020, PaperVariant=12, exam_session= 's', Type= 'qp')

def download_paper(subject_code:int, Year:int, PaperVariant: int or None = None, exam_session= ['s','w','m'], Type= ['sp','ms','qp','er','ir','gt']):
    try:
        start_time = time.time()
        paperurl, paper = find_paper(subject_code, Year, PaperVariant, exam_session, Type)
        response = requests.get(f"{paperurl}")
        with open(f"renderer\paper_cache\pdf\{paper.split('/')[2]}", "wb") as file:
            file.write(response.content)
            file.close()
        print("--- %s seconds ---" % (time.time() - start_time))
    except PaperNotFound:
        return PaperNotFound
download_paper(9706, 2020, 12, 's', 'ms')
