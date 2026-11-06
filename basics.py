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