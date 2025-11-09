name=input("Name of the passenger: ")
distance=float(input("Distance to travel(in kilometres ): "))
vehicle=int(input("Enter your vehicle type(1:Bike, 2:Car, 3:Bus): "))
def type_of_vehicle(vehicle):
    if(vehicle==1):
        return "Bike"
    elif(vehicle==2):
        return "Car"
    else:
        return "Bus"
    

def fare(vehicle,distance):
    if (vehicle==1):
        if (0<distance<50):
           return 5*distance
        elif (distance>=50)and (distance<=200):
           return 4*distance
        else:
           return 3*distance    
    elif(vehicle==2):
        if (0<distance<50):
           return 10*distance   
        elif (distance>=50)and (distance<=200):
           return 9*distance
        else:
           return 8*distance
    else:
        if (distance<50):
           return 8*distance
        elif (distance>=50) and (distance<=200):
           return 7*distance
        else:
           return 6*distance
        
if (fare(vehicle, distance)>=1500):
    discount=fare(vehicle, distance)*0.05
    t_fare=fare(vehicle, distance) - discount
else:
    discount=0
    t_fare=fare(vehicle, distance)

if distance>=500:
    suggestions= "It's better to travel by train or flight for long distances."
else:
    suggestions="You can proceed with your current vehicle choice."


print("Passenger Name:",name)
print("Vehicle Type:",type_of_vehicle(vehicle))
print("Distance traveled:", distance, "km")
print("Base fare:₹",fare(vehicle, distance))
print("Discount applied:₹",discount)
print("Full amount payable:₹",t_fare)
print("Any travel suggestions:",suggestions)

    
    
        
    
        
