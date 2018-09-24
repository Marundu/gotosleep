import os
import schedule
import time

def gotosleep():
    #print('Go to sleep!')
    schedule.every().day.at('22:00').do(os.system('shutdown -h 0'))

if __name__=='__main__':
    gotosleep()
