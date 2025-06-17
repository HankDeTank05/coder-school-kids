import datetime

feed_times = [
    datetime.time(hour = 7, minute = 45),
    datetime.time(hour = 12, minute = 30),
    datetime.time(hour = 18, minute = 30)
]

def feed_fishy(amount):
    print(f"The fish has been fed {amount} food")

while True:
    now = datetime.now()

    if now == feed_times[0]:
        print("Happy breakfast")
        feed_fishy(2)
    elif now == feed_times[1]:
        print("Lunchtime! :)")
        feed_fishy(2)
    elif now == feed_times[2]:
        print("Dinnnerrtiiiiiiimmmmmmmeeee")
        feed_fishy(2)