import cv2
import os, pickle,sys
import numpy as np
import re
from glob import glob
from tqdm import tqdm
from collections import Iterable
from datatools.mechanic.facerec import load_erjin_info, dump_erjin_info
from datatools.imgproc import imshow, im2Dlist, imlist, imdecode, imwrite, jpeg_encode
from datatools.logproc import pbar
from datatools.mechanic.utils import run_command, generate_path
from datatools.dataiter import MultiHandler, JsonListHandler, LMDBHandler, NoriHandler,TarHandler,VideoHandler,MSGPackNoriHandler

# nr = MSGPackNoriHandler.open('/unsullied/sharefs/wangfeihong/facerec/hankou/track/track-0.nori')

file = open('/unsullied/sharefs/liyang/facerec-raw-data/hankou-subway/KP00000000000000002017101801.txt')
time = []
stime = []
minustime = []
maxminustime = 0;
line = file.readline()
while line:
	re1 = re.compile('2017.*\t')
	# print(re1.findall(line)[0].split('\t')[0].split('20171018')[1])
	if line.find('102700057119') != -1:			#zhajihao
		time.append(re1.findall(line)[0].split('\t')[0].split('20171018')[1])
	line = file.readline()
# print(len(time))
for t in time:
	h = int(t[0]+t[1])*3600
	m = int(t[2]+t[3])*60
	s = int(t[4]+t[5])
	stime.append(h+m+s)

for i in range(len(stime)-1):
	minustime.append(stime[i+1]-stime[i])
	if stime[i+1]-stime[i] < 0:
		maxminustime = stime[i+1]-stime[i]
		
stime.sort()

for i in range(0,len(stime)-1):
	j = i+1
	while -(stime[i] - stime[j])<5779:
		j = j+1
	print(j-i)
	
	

# print(stime)
# video = cv2.VideoCapture('/unsullied/sharefs/liyang/facerec-raw-data/hankou-subway/100.2.43.8-10171235.mp4')
# while(video.isOpened()):
# 	ret,frame = video.read()
# 	rect = frame[130:500,200:550]
# 	cv2.waitKey(1)