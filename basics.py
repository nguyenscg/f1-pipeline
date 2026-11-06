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