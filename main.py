from datetime import datetime, timedelta,date
from datetime import time

FORMAT = "{hours}:{minutes}"
# Use {days}, {hours}, {minutes}, {seconds}

SLEEPMSG = "zzz"

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

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
],
[
    time(hour=8,minute=40),
    time(hour=9,minute=35),
    time(hour=10,minute=30),
    time(hour=10,minute=55),
    time(hour=11,minute=50),
    time(hour=12,minute=45),
    time(hour=13,minute=30),
    time(hour=15,minute=30)
],
[
    time(hour=8,minute=40),
    time(hour=9,minute=40),
    time(hour=10,minute=40),
    time(hour=11,minute=5),
    time(hour=11,minute=20),
    time(hour=12,minute=25),
    time(hour=13,minute=25),
    time(hour=14,minute=15),
    time(hour=15,minute=15),
]
]

def main():
    if today.weekday() == 5 or today.weekday() == 6:
        return SLEEPMSG
    
    if today.time() > periods[today.weekday()][-1]:
        return SLEEPMSG

    for times in periods[today.weekday()]:
        if times < today.time():
            nextPeriod = times
        else: break

    delta = (today - datetime.combine(today.date(),nextPeriod))
    return strfdelta(delta,FORMAT)
    

print(main())