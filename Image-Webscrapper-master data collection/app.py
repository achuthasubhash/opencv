# -*- coding: utf-8 -*-
"""
@author: Krish Naik
"""
# Importing the necessary Libraries
from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify  #render_template for display html, (request,jsonify ) scrab images from interet
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer
import os


# import request
app = Flask(__name__) # initialising the flask app with the name 'app'

#response = 'Welcome!'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages(): #display all images from staic
    list_images=os.listdir('static') #going to folder and extract images
    print(list_images) #printing
    
    try: #if no images then exception handling
        if(len(list_images)>0):
            return render_template('showImage.html',user_images=list_images) #give html file
        else: #not found
            return "Images are not present"
    except Exception as e: 
        print("No images found",e)
        return "Please try with a different search keyword"
    
@app.route('/searchImages',methods=['Get','POST']) #search corr req images from google url,create new folder
def searchImage():
    if request.method=="POST": #take req from post
        search_term=request.form['keyword'] # assigning the value of the input keyword to the variable keyword
        #take i/p
    else:
        print("Please enter something")
    
    imagescrapperutil=BusinessLayer ## Instantiate a object for ScrapperImage Class #take keywords
    imagescrapper=ScrapperImage()
    list_images=os.listdir('static') #listing
    imagescrapper.delete_downloaded_images(list_images)## Delete the old images before search
    
    image_name=search_term.split()
    image_name="+".join(image_name)
    
    ## We need to add the header metadata
    #from ur browser it is unique from browser
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            
            }
    lst_images=imagescrapperutil.downloadImages(search_term,header) 
    
    return displayImages() # redirect the control to the show images method
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000) # port to run on local machine
   #app.run(debug=True) # to run on cloud
