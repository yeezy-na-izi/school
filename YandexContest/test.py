from sys import stdin
import datetime

time, count = [int(i) for i in input().split()]
errors = []
for line in stdin:
    message = line.split()
    if message[2] == 'ERROR':
        date = datetime.datetime.fromisoformat(f'{message[0][1:]} {message[1][:-1]}')
        errors.append(date)
        if len(errors) == count:
            if (errors[-1] - errors[0]).total_seconds() < time:
                print(errors[-1])
                break
            errors.pop(0)
else:
    print(-1)
