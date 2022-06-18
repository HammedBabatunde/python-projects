import time

class Timer:
    def __init__(self, t):
        self.time = t
    
    def increase_time(self):
        add_time = int(input('How much time do you want: '))
        self.time = add_time

    def countdown(self):
       
        while self.time:
            mins, secs = divmod(self.time, 60)
            # print(mins, secs) ## To print minutes and seconds
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            self.time -=1

            


def run_countdown():
    print("Welcome")
    start_time = int(input('Please input the time in seconds: '))

    while True:
        user = Timer(start_time)
        user.countdown()
        ext_time = input("Do you want more time(Yes or No): ")
        if ext_time == 'Yes':
            user.increase_time()
            continue
        elif ext_time == "No":
            print('Well done')
            break



run_countdown()