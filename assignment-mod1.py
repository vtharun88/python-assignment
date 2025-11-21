'''Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. if they want to travel three hundred miles or more tell them to drive Super-Car'''
a=float(input("how far do you want to go??"))
if a<3:
    print("you can walk that distance.")
elif a>3 and a<100 :
    print("you can ride Bicycle..")
elif a>=100 and a<300:
    print("you can take a bike and ride..")
else :
    print("take your car and drive the distance..")