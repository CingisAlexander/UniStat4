# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 14:02:01 2017

@author: Cingis Alexander
"""
import numpy as np
data = open("vers.dat","r") 
data =None
prep_data = data.read()
print(prep_data)
pr_data = np.array(prep_data) 
print(pr_data)
type(pr_data[1])
np.shape(pr_data)

import csv
with open("vers.csv") as csvfile:
    #it will be readed as string
    readCSV = csv.reader(csvfile, delimiter=" ")
    out = readCSV
    col0 = []
    col1 = []
    col2 = []
    ct = 0
    for row in readCSV:
        if ct ==0:
            ct =1 
        else:
            cole0 = row[0]
            cole1 =row[1]
            cole2 = row[2]
            col0.append(cole0)
            col1.append(cole1)
            col2.append(cole2)
            
            
col0 = list(map(int,col0)) 
col1 = list(map(int,col1))
col2 = list(map(float,col2))  
