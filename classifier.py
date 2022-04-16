import imp
from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
 
 def get_prediction(image):
     im_pil = Image.open(image)
     image_bw = im_pil.convert('L')
     image_bw_resized = image_bw.resize((22,30), Image.ANTIALIAS)
     pixel_filter = 20
     min_pixel = np.recentile(image_bw_resized, pixel_filter)
     image_bw_resized_inverted_scaled = np.clip(image_bw_resized-min_pixel, 0, 255)
     max_pixel = np.max(image_bw_resized)

     image_bw_resized_inverted_scaled = np.asarray(image_bw_resized_inverted_scaled)/max_pixel
     test_smaple = clf.predict(test_sample)
     return test_pred[0]