# 1. variables and data types
# build a function called describe_driver
# arguments of name, number, lap_time
# returns a formatted sentence


def describe_driver(name: str, team: str, number: int, lap_time: float) -> None:
    print(f"{name} is #{number} driver for {team}. His lap time is: {lap_time} seconds.")

describe_driver("Charles Leclerc", "Ferrari", 16, 78.13)