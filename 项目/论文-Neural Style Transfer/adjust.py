import os
import cv2

NAME = 'Asagri'

img1 = os.listdir('./contents/')
img2 = os.listdir('./styles/')

cnt = 1
for idx in img1:
    img = cv2.imread('./contents/'+idx)
    dst = cv2.resize(img,(256,256))
    cv2.imwrite('./contents1/'+NAME+'_' +'sim'+ '_' +str(cnt)+'.jpg',dst)
    cnt += 1

cnt = 1
for idx in img2:
    img = cv2.imread('./styles/'+idx)
    dst = cv2.resize(img,(256,256))
    cv2.imwrite('./styles1/'+NAME+'_' +'real'+ '_' +str(cnt)+'.jpg',dst)
    cnt += 1