#!/usr/bin/env python
# coding: utf-8

# # OpenCV Social Distancing Detector

# In[1]:


# base path to YOLO directory
MODEL_PATH = "YOLO_DB"

# threshold and non-maxima suppression
MIN_CONF = 0.3
NMS_THRESH = 0.3   # higher means lower optimization


# In[5]:


#NVIDIA CUDA GPU should be used
USE_GPU = False
# safe distance in pixel
MIN_DISTANCE = 50


# In[6]:


import numpy as np
import cv2


# In[8]:


def detectPeople(image, net, layerName, personIdx=0):
    height, weidth,_ = image.shape
    results = []
    
    blob = cv2.dnn.blobFromImage(image, 1/255.0,(416, 416), swapRB= True, crop= False)
    net.setInput(blob)
    layerOutputs = net.forward(layerName)
    
    boxes = []
    centroids = []
    confidences = []
    
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            clsID = np.argmax(scores)
            conf = scores[clsID]
            
            if clsID== personIdx and conf > MIN_CONF:
                box = detection[0:4] * np.array([weidth, height, weidth, height])
                (cX, cY, w, h)= box.astype("int")
                
                #left corner
                x = int(cX - (w/2))
                y = int(cY - (h/2))
                
                boxes.append([x, y, int(w), int(h)])
                centroids.append((cX, cY))
                confidences.append(float(conf))
    
    
    # apply non-maxima suppression to suppress weak, overlapping
    bboxes = cv2.dnn.NMSBoxes(boxes, confidences, MIN_CONF, NMS_THRESH)
    
    if len(bboxes) > 0:
        for i in bboxes.flatten():
            #bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            r = (confidences[i], (x, y, x+w, y+h), centroids[i])
            results.append(r)
    return results


# In[ ]:




