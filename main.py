from datetime import datetime
from datetime import time

today = datetime.today()
periods = [
[
    time(hour=8,minute=40),
    time(hour=9,minute=40),
    time(hour=11,minute=5),
    time(hour=11,minute=35),
    time(hour=12,minute=40),
    time(hour=13,minute=40),
    time(hour=14,minute=30),
    time(hour=15,minute=30),
],
[
    time(hour=8,minute=40),
    time(hour=9,minute=40),
    time(hour=10,minute=40),
    time(hour=11,minute=5),
    time(hour=12,minute=10),
    time(hour=13,minute=10),
    time(hour=2,minute=0),
    time(hour=3,minute=0),
]
]

def main():
    if today.weekday() == 5 or today.weekday() == 6:
        return "zzz"
    
    if today.time() > periods[0][-1]:
        return "zzz"

    

print(main())