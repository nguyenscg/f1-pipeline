# store driver information in variables, print 
driver = "Max Verstappen"
team = "Red Bull"
number = 3
print(driver)
print(team)
print(number)
print(f"{driver} is part of {team} and his number is {number}")

# lap time in seconds
laps = [60, 10, 30, 45, 600]
print(laps)

count = 0
fastest = laps[0]
position = 11
points = 0
for lap in laps:
    count += 1
    print(lap) # print 60, 10, 30, 45, individually
    print(count)
    print(f"Lap {count}: {lap}s")
    if lap < fastest:
        fastest = lap
    print(f"The fastest lap is {fastest}s")

# if/elif/else for position, podium, points
# if position is 1 -> podium 1st
# 25, 18, 15, 12, 10, 6, 4, 2, 1, 0 (11+)

# if the position is 1, 2, or 3, print Podium
if position < 4:
    print("Podium")
# if the position is 4, 5, 6, 7, 8, 9, 10, print Points
elif position < 11:
    print("Points")
# else, anything after 10 is no points
else:
    print("No points")