#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

iheight = input('Entype your height(ex 1.75): ')
iweight = input('Entype your weight(ex 80.5): ')

#height = int(iheight)
#weight = int(iweight)
height = 1.78
weight = 96.5

bmi = weight/height/height

if bmi < 18.5 :
    print('Your bmi is %.1f,Tai qing'%(bmi))
elif ((bmi >= 18.5) & (bmi < 25)) :
    print('Your bmi is %.1f,Nomal'%(bmi))
elif ((bmi >= 25) & (bmi < 28)) : 
    print('Your bmi is %.1f,Guo zhong'%(bmi))
elif ((bmi >= 28) & (bmi <32)) :
    print('Your bmi is %.1f,Fat'%(bmi))
else :
    print('Your bmi is %.1f,Fat too much'%(bmi))
