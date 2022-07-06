# -*- coding: utf-8 -*-



import base64 
import json
import os 
#convert image to byte type
a = os.path.basename(__file__)
b = os.path.abspath(__file__).replace(a, '')
name = input('Название картинки в этой же дирректории: ')
with open(b + name, "rb") as image_file:
    encoded_string1 = base64.b64encode(image_file.read())

#convert byte to string
encoded_string = encoded_string1.decode("utf-8")
jsn = {'img':encoded_string}
with open(b + name + '.json','w') as file:
    json.dump(jsn, file)