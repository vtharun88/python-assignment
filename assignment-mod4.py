speeds = []
for i in range(1, 13):
    while True:   
        try:
            speed = float(input(f"Enter speed for hour {i}: "))
            speeds.append(speed)
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
avgspeed = sum(speeds) / 12
print(f"Average speed: {avgspeed}")
if avgspeed < 40:
    print("Traffic Flow: Slow")
elif 40 <= avgspeed <= 80:
    print("Traffic Flow: Normal")
else:
    print("Traffic Flow: Fast")