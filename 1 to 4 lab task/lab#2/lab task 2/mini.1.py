
class Fizz_buZZ:
    def __init__(self, num):
        self.num=num
        
    def conditions(self):
        for i in range(1, self.num+1):
            if i%3==0 and i%5==0:
                print("Fizz_Buzz")
                
            elif i%3==0:
                print("Fizz")
                
            elif i%5==0:
                print("Buzz")
                
            else:
                print(i)
                
obj1=Fizz_buZZ(15)
obj1.conditions()
            