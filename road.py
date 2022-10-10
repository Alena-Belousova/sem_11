#from tkinter import *
#import time
from socket import IPPROTO_GGP


class Road:
    #атрибуты
    length=10
    width=5  
    
    #методы
    def mas_of_asphalt_for_all_road_long(self):
       asphalt_for_1m2= 25
       asphalt_thickness =5
       itog=Road.length*Road.width*asphalt_thickness*asphalt_for_1m2
       print (itog)

a=Road() 
print(a.mas_of_asphalt_for_all_road_long())   
     


    
