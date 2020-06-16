# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:51:15 2020

@author: krish.naik
"""

from bs4 import BeautifulSoup as bs #for web crsb
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

class ScrapperImage:
    
    ## Create  Image URl
    def createImageUrl(searchterm):  #just keep search term 
        searchterm=searchterm.split()
        searchterm="+".join(searchterm) #space b/w 2 words replace by +
        web_url="https://www.google.co.in/search?q=" + searchterm + "&source=lnms&tbm=isch"
        return web_url
    
   # get Raw HTML
    def scrap_html_data(url,header):  #take url & header
        request=urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)
        responseData = response.read()
        html = bs(responseData, 'html.parser')
        return html
    
    # contains the link for Large original images, type of  image
    def getimageUrlList(rawHtml): #rawhtml have list of images url
        imageUrlList = []
        for a in rawHtml.find_all("div", {"class": "gb_Zd"}): #rgmeta is have content in this have url
            link, imageExtension = json.loads(a.text)["ou"], json.loads(a.text)["ity"] #extract link,ou have link image
            imageUrlList.append((link, imageExtension)) #crreate list

        print("there are total", len(imageUrlList), "images")
        return imageUrlList
    
    def downloadImagesFromURL(imageUrlList,image_name, header): #download
        masterListOfImages = []
        count=0
        ###print images
        imageFiles = []
        imageTypes = []
        image_counter=0
        for i, (img, Type) in enumerate(imageUrlList):  #img is link,type is format
            try:
                if (count > 100): #here only 5 #if what x keep x
                    break
                else:
                    count = count + 1
                req = urllib.request.Request(img, headers=header)
                try:
                    urllib.request.urlretrieve(img,"./static/"+image_name+str(image_counter)+".jpg") #where download and type of image
                    image_counter=image_counter+1
                except Exception as e:
                    print("Image write failed:  ",e)
                    image_counter = image_counter + 1
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()
                # soup = bs(respData, 'html.parser')

                imageFiles.append(raw_img)
                imageTypes.append(Type)

            except Exception as e:
                print("could not load : " + img)
                print(e)
                count = count + 1
        masterListOfImages.append(imageFiles)
        masterListOfImages.append(imageTypes)

        return masterListOfImages
    
    def delete_downloaded_images(self,list_of_images): #to not collide
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting:  ',e)
        return 0
    
   
    
    
    
    