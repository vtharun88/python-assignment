end = int(input("Enter end of range: "))

odd_cubes = {n: n**3 for n in range(1,end+1) if n % 2 != 0}

print(odd_cubes)

