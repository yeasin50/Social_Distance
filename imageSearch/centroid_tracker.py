#!/usr/bin/env python
# coding: utf-8

# # import the necessary packages

# In[1]:

from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np


# In[2]:


class CentroidTracker():
    def __init__(self, maxDisappeared= 50, maxDistance=50):
        self.nextObjectID = 0 #A counter used to assign unique IDs to each object 
        self.objects = OrderedDict() #utilizes the object ID as the key and the centroid (x, y)-coordinates as the value
        self.disappeared = OrderedDict()# consecutive frames (value) a particular object ID (key) has been marked as “lost
    
        # object is allowed to be marked as "disappeared" until we
        # need to deregister the object from tracking
        self.maxDisappeared = maxDisappeared
        
        
        # store the maximum distance between centroids to associate
        # an object -- if the distance is larger than this maximum
        # distance we'll start to mark the object as "disappeared"
        self.maxDistance = maxDistance
    
    
    # when registering an object we use the next available object
    # ID to store the centroid
    def register(self, centroid):
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] =0
        self.nextObjectID +=1
      
    #simply delete 
    def deregister(self, objectID):
        del self.objects[objectID]
        del self.disappeared[objectID]
    


# In[4]:


    def update(self, bbox):

        #If there are no detections, 
        #we’ll loop over all object IDs and increment their disappeared  count
        if len(bbox)==0:
            for objectID in list(self.disaappeared.keys()):
                self.disaappeared[objectID] +=1

                # if we have reached a maximum number of consecutive
                # frames where a given object has been marked as
                # missing, deregister it
                if self.disaappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)
                    
            return self.objects

        # if we have detected objs
        inputCentroids = np.zeros((len(bbox), 2), dtype='int')

        # 0 means startPoint and 1 means endPoint
        for (i, (x0, y0, x1, y1)) in enumerate(bbox):
            #calculate center of bounding box and return as int 
            cX = int((x0 + x1) /2.0)
            cY = int((y0 + y1) /2.0)
            inputCentroids[i] = (cX, cY)


        # If there is no Track of objects, register with centroid
        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i])

        # Otherwise update our exits object centroids
        #that minimizes the Euclidean distance between them
        else:
            #Grab objectIDs  and objectCentroid  values
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())

            # compute the distance between each pair of object
            distanceMap = dist.cdist(np.array(objectCentroids), inputCentroids)

            # smallest at front
            rows = distanceMap.min(axis =1).argsort()
            cols = distanceMap.argmin(axis=1)[rows]

           #use distanceMap, set() contains only unique values
            usedRows = set()
            usedCols = set()

            for(row, col) in zip(rows, cols):

                #skip if it's already calculated
                if row in usedRows or col in usedCols:
                    continue

                # if the distance between centroids is greater than
				# the maximum distance, do not associate the two
				# centroids to the same object
                if distanceMap[row, col] > self.maxDistance:
                    continue
                    
                #else we need set new centroid and reset disappeared counter
                objID = objectIDs[row]
                self.objects[objID] = inputCentroids[col]
                self.disappeared[objID] = 0

                #update with cords
                usedRows.add(row)
                usedCols.add(col)
                

            # there could be not examined value , let;s examined them as well
            unUsedRows = set(range(0, distanceMap.shape[0])).difference(usedRows)
            unUsedCols = set(range(0, distanceMap.shape[1])).difference(usedCols)


            if distanceMap.shape[0] >= distanceMap.shape[1]:
                for row in unUsedRows :
                    objID = objectIDs[row]
                    self.disappeared[objID] += 1

                if self.disappeared[objID] > self.maxDisappeared:
                    self.deregister(objID)
                else:
                    for col in unUsedCols:
                        self.register(inputCentroids[col])

            #set of trackable objects
        return self.objects



# #  Jupyter Runtime you will get an error, because we dont have any objects yet
