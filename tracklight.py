
import time
class TrafficLight:
    #атрибуты
    color1='красный'
    color2='желтый'
    color3='зеленый'
    #методы
    def running(self):
        print(TrafficLight.color1)
        time.sleep(7)
        print(TrafficLight.color2)
        time.sleep(2)
        print(TrafficLight.color3)
        time.sleep(7)
a=TrafficLight()
print(a.running())

    
