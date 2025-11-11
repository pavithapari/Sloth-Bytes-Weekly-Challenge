"""bedTime(["07:50", "07:50"])
output = ["00:00"]

bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
output = ["20:15", "22:00", "23:30"]


bedTime(["05:45", "04:00"], ["07:10", "04:30"])
output = ["01:45", "02:40"] """

def bedTime(*args):
    results = []
    for arr in args:
        wake = arr[0]
        sleep = arr[1]

        wake_h = int(wake[:2])
        wake_m = int(wake[3:])
        sleep_h = int(sleep[:2])
        sleep_m = int(sleep[3:])

        minutes = wake_m - sleep_m
        hours = wake_h - sleep_h

        if minutes < 0:
            minutes += 60
            hours -= 1
        if hours < 0:
            hours += 24

        results.append(f"{hours:02d}:{minutes:02d}")
    return results

print("output =",bedTime(["07:50", "07:50"]))
print("output =",bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]))
print("output =",bedTime(["05:45", "04:00"], ["07:10", "04:30"]))

