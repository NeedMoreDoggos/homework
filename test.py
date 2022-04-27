from time import *
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds, end='')
            sleep(1)
            print(end='\r')
