# -*- coding: utf-8 -*-
"""
Created on Sun May  1 21:37:14 2022

@author: Admin
"""

from flask import Flask,request,jsonify
from flask_cors import CORS
import recommendation_dog


app = Flask(__name__)
        
@app.route('/')
def recommend_dogs():
    res = recommendation_dog.recommend_similar_dogs('Shiba Inu')
    print(res)
    return (res)

if __name__=='__main__':
    app.run(port = 5000, debug = True)
