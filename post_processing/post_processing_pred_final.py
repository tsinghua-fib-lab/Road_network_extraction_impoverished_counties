import pandas as pd
import numpy as np
from shapely.geometry import Point
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = None
from skimage import morphology,draw
import cv2
import matplotlib.pyplot as plt
import os

district_list = ['XixiangCounty'] # an example

for city in district_list:
    if os.path.exists('skeleton_file_final_d300/pred_skeleton_'+city+'_'+str(2021)+'_2.png'):
        continue
    print(city)

    if not os.path.exists('combine_lable_final/'+city+'_pred_'+str(2021)+'_divide_inhabited2.png'):
        continue
    print('reading '+'combine_lable_final/'+city+'_pred_'+str(2021)+'_divide_inhabited2.png')
    road2017 = Image.open('combine_lable_final/'+city+'_pred_'+str(2021)+'_divide_inhabited2.png')
    #road2017 = road2017.resize((int(np.array(road2017).shape[1]),int(np.array(road2017).shape[0])))
    road2017_arr = np.array(road2017)
    # print(road2017_arr.shape)
    road2017 = None

    road_tmp = road2017_arr
    
    road_seg = np.array(road_tmp) #[512:-512*5,1024:-512*4]
    road_idx = np.where(road_seg > 0)

    print(2017,len(road_idx[0]))

    bin_image = np.zeros((road_seg.shape[0],road_seg.shape[1]))
    bin_image[road_idx[0],road_idx[1]] = 1

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11,11))
    bin_image = cv2.morphologyEx(bin_image, cv2.MORPH_CLOSE, kernel)

    bin_image = np.uint8(bin_image)

#print(np.sum(np.array(test_img)))

#     image = test_img

#     print(image.shape)
# #skeleton
    skeleton =morphology.skeletonize(bin_image)

    road_seg = np.uint8(np.array(skeleton)) #[512:-512*5,1024:-512*4]
    road_idx = np.where(road_seg > 0)
    print(2017,len(road_idx[0]),'  skeleton')

    # skeleton = Image.fromarray(skeleton)
    # skeleton.convert('L').save('skeleton_file_final/pred_skeleton_'+city+'_'+str(2017)+'_2_tmp.png')  #xiaoxian

    road_seg[road_idx] = 1

    # bin_image = np.uint8(road_seg)

    _, labels, stats, centroids = cv2.connectedComponentsWithStats(road_seg)
# print(centroids)
# print("stats",stats)
#print('len(stats): ',len(stats))
    i=0
    for istat in stats:
        if istat[4]<300 and istat[4]>0:  #skeleton_file_final_d300
        # print(i, istat[4])
        # print(istat[0:2])
        # if istat[3]>istat[4]:
        #     r=istat[3]
        # else:r=istat[4]
            if istat[0]<=100 and istat[1]<=100 and istat[0]+istat[2]>=road_seg.shape[0]-20 and istat[1]+istat[3]>=road_seg.shape[1]-20: #road2017_arr
                print(tuple(istat[0:2]),tuple(istat[0:2]+istat[2:4]))
                continue
            cv2.rectangle(road_seg,tuple(istat[0:2]),tuple(istat[0:2]+istat[2:4]) , 0,thickness=-1)  # 26  #test_img
            i=i+1

    road_idx = np.where(road_seg > 0)
    road_seg[road_idx] = 255
    print(2017,len(road_idx[0]),'  skeleton')

    skeleton = Image.fromarray(road_seg) #test_img
    skeleton.convert('L').save('skeleton_file_final_d300/pred_skeleton_'+city+'_'+str(2021)+'_2.png')  #save file

