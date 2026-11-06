# 1. variables and data types
# build a function called describe_driver
# arguments of name, number, lap_time
# returns a formatted sentence


def describe_driver(name: str, team: str, number: int, lap_time: float) -> str:
    return(f"{name} is #{number} driver for {team}. Lap time: {lap_time} seconds.")

# check / test
assert describe_driver("Charles Leclerc", "Ferrari", 16, 78.13) == \
    "Charles Leclerc is #16 driver for Ferrari. Lap time: 78.13 seconds."

print(describe_driver("Charles Leclerc", "Ferrari", 16, 78.13))

# check / test
assert describe_driver("Max Verstappen", "Redbull", 3, 55.34) == \
    "Max Verstappen is #3 driver for Redbull. Lap time: 55.34 seconds."

print(describe_driver("Max Verstappen", "Redbull", 3, 55.34))

# check / test
assert describe_driver("Alex Albon", "Williams", 23, 100.22) == \
    "Alex Albon is #23 driver for Williams. Lap time: 100.22 seconds."

print(describe_driver("Alex Albon", "Williams", 23, 100.22))

# count the items by looping
def len(items):
    count = 0

    for item in items:
        count += 1
    return count

print(len(items=["Charles Leclerc", "Max Verstappen", "Alex Albon", "Carlos Sainz", "Kimi Antonelli"]))

# keep a running total
def sum(items):
    total = 0

    for item in items:
        total += item
    return total

print(sum(items=[78.13, 55.34, 100.22]))

# start with the first item, compare each one
def min(items):
    lowest = items[0]

    for item in items:
        if lowest > item:
            lowest = item
    return(f"{lowest} is the minimum.")

print(min(items=[78.13, 55.34, 100.22]))
    

# same, opposite comparison
def max(items):
    highest = items[0]

    for item in items:
        if highest < item:
            highest = item
    return(f"{highest} is the max.")

print(max(items=[78.13, 55.34, 100.22]))