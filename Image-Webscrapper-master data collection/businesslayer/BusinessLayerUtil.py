# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:24:49 2020

@author: krish.naik
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    #variables
    keyword=""
    fileLoc=""
    image_name=""
    header=""
     
    def downloadImages( keyWord, header): #searched word,
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyWord) #get image url
        rawHtml = imgScrapper.scrap_html_data(url, header) #scrap images(have all images ,imageurl)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        
        return masterListOfImages    
   
    
    