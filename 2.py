import cv2
import os, pickle,sys
import numpy as np
import json
from glob import glob
from tqdm import tqdm
from collections import Iterable
from datatools.mechanic.facerec import load_erjin_info, dump_erjin_info
from datatools.imgproc import imshow, im2Dlist, imlist, imdecode, imwrite, jpeg_encode
from datatools.logproc import pbar
from datatools.mechanic.utils import run_command, generate_path
from datatools.dataiter import MultiHandler, JsonListHandler, LMDBHandler, NoriHandler,TarHandler,VideoHandler,MSGPackNoriHandler
import array

def inrect(rect,face):
	rright = rect[1]
	rleft = rect[0]
	rtop = rect[2]
	rbottom = rect[3]
	fright = face['right']
	fleft = face['left']
	ftop = face['top']
	fbottom = face['bottom']
	if rright>fright and rleft<fleft and rtop<ftop and rbottom>fbottom:
		return True
	else:
		return False


info = [] 
tracks_str_list = []
with open('/unsullied/sharefs/wangfeihong/facerec/hankou/track2/0c7272af2b79e56286cbb82d47a43c66.tracks','r') as fp:
	for line in fp:
		tracks_str_list.append(line)
			

tracks_list = []
print('json loads now....')


for str_track in tqdm(tracks_str_list):
	tracks_list.append(json.loads(str_track))

videotime = len(tracks_str_list)/25
frame = 0
people = []

for i in tqdm(tracks_list):
	# print(len(i['items']))
	frame = frame+1
	time = int(frame/25)
	if frame%25 == 0:
		people = []
	for it in i['items']:
		# print(it['track_id'])
		people.append({'id':'id_'+str(it['track_id']),'rect':it['rect']})
	if len(info) == 0:
		info.append({'time(second)':time,'people':people})

	elif time != info[len(info)-1]['time(second)']:
		info.append({'time(second)':time,'people':people})
	else:	
		info[len(info)-1]['people'] = people


n = []
rect = [130,500,200,550]
rect2 = [130,500,650,950]
for _info in info:
	p1 = []
	people = _info['people']
	for p in people:
		# print(type(rect),type(p['rect']))
		try: 
			# print(p['rect'])
			if inrect(rect,p['rect']):
				p1.append(p['id'])
		except:
			pass
	if(len(p1) != 0):
		n.append({'time':_info['time(second)'],'id':p1[0]})



# for _info in info:
# 	_time = _info['time(second)']
# 	people = _info['people']
# 	for person in people:
# 		# print(type(rect),type(p['rect']))
# 		try: 
# 			for p in person:
# 				if inrect(rect,p['rect']):
# 					n.append(p['id'])
# 		except:
# 			pass 
# n = set(n)
tep = []
temp = []
for i in n[::-1]:
	if i['id'] not in temp:
		tep.append(i['time'])
		temp.append(i['id'])

tep.sort()
data = []
for i in range(0,len(tep)-2):
	data.append(tep[i+1]-tep[i])

print(data)
print('seconds:',videotime)
print('people:',len(n))