class Reflex_Agent:
    def __init__(self, desired_temp):
        self.desired_temp=desired_temp
        self.status="off"
        
    def Action(self, current_temp):
        self.current_temp = current_temp
        
        if self.current_temp>self.desired_temp and self.status=="on":
            self.status="off"
            return "Turn off the Heater"
        elif self.current_temp<self.desired_temp and self.status=="off":
            self.status="on"
            return "Turn o the Heater"
        else:
            return "no action needed"
        
# implementation:
rooms={
    "living room": 18,
    "bedroom": 22,
    "kitchen":20,
    "bathroom":24
} 

desired_temp=22
agent=Reflex_Agent(desired_temp)
for room, temp in rooms.items():
    action = agent.Action(temp)
    print(f"{room}: current_temperature = {temp} Degree Celsius {action}")