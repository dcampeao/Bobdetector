import cv2
import os

allpics = [p for p in os.listdir('.') if p.endswith('.jpg')]
count = 0
for p in allpics:
    img = cv2.imread(p)
    img = cv2.resize(img, (0,0), fx=0.3, fy=0.3) 
    xc = int(img.shape[1]/2)
    yc = int(img.shape[0]/2)
    halfsize = 50
    crop_img = img[yc-halfsize:yc+halfsize,xc-halfsize:xc+halfsize]
    #crop_img = cv2.resize(crop_img, (0,0), fx=0.2, fy=0.2)
    cv2.imwrite('0/'+p,crop_img)
    count+=1
    print('{} % complete...'.format(round(count/len(allpics)*100,2)))

    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)