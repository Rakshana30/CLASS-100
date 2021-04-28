class cars(object):
    def  __init__ (self,number,colour,model,brand):
        self.number = number
        self.colour = colour
        self.model = model
        self.brand = brand

    def start(self):
        print("start")

    def stop(self):
        print("stop")

BMW = cars("TN 24 B 1001","white","BMW M8","BMW")
BMW.start() 
BMW.model   
BMW.colour
BMW.stop()