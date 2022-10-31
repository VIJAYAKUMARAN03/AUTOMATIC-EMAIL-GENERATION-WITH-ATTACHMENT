# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:29:01 2022

@author: DELL
"""

from PIL import ImageDraw, ImageFont, ImageColor, Image
def image(name):
    img = Image.open('temp.jpg')
    
    draw = ImageDraw.Draw(img)
    f = ImageFont.truetype('Candarai.ttf',size=65)
    l=(2000-(34*len(name)))//2
    draw.text((l,750),name,fill=(2512,175,55),font=f)
    img.save('draw.jpg')
image('VIJAYAKUMARAN')
    