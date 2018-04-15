import connexion
import six

from swagger_server.models.download import Download  # noqa: E501
from swagger_server.models.iris_categories import IrisCategories  # noqa: E501
from swagger_server.models.iris_display import IrisDisplay  # noqa: E501
from swagger_server import util

import urllib2
from os.path import expanduser
import pandas as pd
import os
import flask
import json
from flask import jsonify
import operator



url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
filePath = 'iris.data'
categoryList = []

def categories_categoryname_get(categoryname):  # noqa: E501
    
    if os.path.exists(filePath):
        irisData = pd.read_csv(filePath, names=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Name"])
        print(irisData.head())
        print(categoryname)

        category_data = irisData.loc[irisData['Name'] == categoryname]
        print(category_data.head())
        for (idx, row) in category_data.iterrows():
            #IrisDisplay.petallength = row.PetalLength
            #IrisDisplay.petalwidth = row.PetalWidth
            #IrisDisplay.sepallength = row.SepalLength
            #IrisDisplay.sepalwidth = row.SepalWidth
            #IrisDisplay.name = row.Name
            idisp=IrisDisplay(row.PetalLength,row.PetalWidth,row.SepalLength,row.SepalWidth,row.Name)
            categoryList.append(idisp)          
       
        return (categoryList)
        #return json.dumps(dict(categoryList.items(),key=operator.itemgetter(1)))
    else:
        return "File Not Present"
    
    """categories_categoryname_get

    Display data for a specific Iris flower category # noqa: E501

    :param categoryname: Data of Flower category to be fethced
    :type categoryname: str

    :rtype: List[IrisDisplay]
    """
    


def categories_get():  # noqa: E501
    """categories_get

    Displays different categories of Iris Dataset # noqa: E501


    :rtype: List[IrisCategories]
    """
    if os.path.exists(filePath):
        irisData = pd.read_csv(filePath, names=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Name"])
        categories = irisData['Name'].unique()
        return categories.tolist()
    else:
        return "File not found"


def download_get():  # noqa: E501
    """Iris Dataset

    Downloads Iris dataset from Web # noqa: E501


    :rtype: Download
    """
    newfile = open('iris.data','w')
    response = urllib2.urlopen(url)
    data = str(response.read())
    lines = data.split("\\n")
    for line in lines:
        newfile.write(line + "\n")
    newfile.close()
    return "File Downloaded"
