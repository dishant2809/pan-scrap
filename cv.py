# -*- coding: utf-8 -*-

import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
from matplotlib import pyplot as plt
import os
import re

path = 'C:/Users/my_wo/ML&AI/Dishant/opencv scraper/'



img_arr=[]
for i in os.listdir(path):
    if i[-3:] == 'jpg':
        a = cv2.imread(i)
        a = cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
        ret,thresh = cv2.threshold(a,100,255,cv2.THRESH_BINARY)
        img_arr.append(thresh)


text = []
for i in img_arr:
    b = pytesseract.image_to_string(i)
    b = b.split("\n")
    b = b.split(' ')
    text.append(b)



for i in text:
    for j in i:
        b = re.search([0-9], j)



fnl=[]
for i in text:
    a = re.search([0-9], i)
    fnl.append(a)


for i in text[0]:
    print(i)


no = [0,1,2,3,4,5,6,7,8,9]


for i in text:
   if i in no:
       print(i)
