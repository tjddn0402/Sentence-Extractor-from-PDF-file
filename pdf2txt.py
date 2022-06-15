from pdfminer import high_level as H
from pathlib import Path
import re
import sys, os
from tkinter import messagebox, filedialog

pdf = filedialog.askopenfilename(initialdir='./',\
                                    title="select pdf file",\
                                    filetypes = [("pdf", "*.pdf")])
text = H.extract_text(pdf)
"""
FF : 아스키넘버 12 (0x0C) - 새로운 페이지 의미
어떻게 처리할지 생각하기
regex 로 \x0C 임.
"""
text = text.replace('\n\n','bunriza')
text = text.replace('-\n', '')
text = text.replace('\n', ' ')
text = text.replace('. ', '.\n')
text = text.replace('bunriza','\n\n')
with open(f'{Path(pdf).stem}.txt', 'w', encoding='utf8') as f:
    f.writelines(text)