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
from datatools.dataiter import MultiHandler, JsonListHandler, LMDBHandler, NoriHandler,TarHandler,VideoHandler
video = cv2.VideoCapture('/unsullied/sharefs/liyang/facerec-raw-data/hankou-subway/100.2.43.8-10171235.mp4')
while(video.isOpened()):
	ret,frame = video.read()
	imshow(frame[130:500,650:950])


# vr = VideoHandler.open('/unsullied/sharefs/liyang/facerec-raw-data/hankou-subway/100.2.43.8-10171524.mp4')
# for idx,frame in vr.scan_with_data():
# 	# print(idx)
# 	cv2.imshow("",frame)
# 	break
	# print(vr.size())
# frames = []
# i = 0
# video = cv2.VideoCapture('/unsullied/sharefs/wangfeihong/facerec/zip/Albina/1.mp4')
# while(video.isOpened()):
# 	ret,frame = video.read()
# # # print(type(frame))
# 	cv2.imshow("video",frame)

	# box = (193, 438, 493, 248)
	# pic = frame1.crop(box)
	# pic = pic.transpose(Image.ROTATE_180)
	# frame.paste(pic, box)
	# frame.show()


# file = open('/unsullied/sharefs/liyang/facerec-raw-data/hankou-subway/KP00000000000000002017101801.txt')
# line = file.readline()
# while line:
# 	print(line)
# 	line = file.readline()
# 	break