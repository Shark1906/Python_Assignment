from datetime import datetime

class Stopwatch:
    def stopwatch(start, end):
        print('Start time : ', start, ', End time : ', end)
        print('Time elapsed : ', end - start)

input('Press enter to start stopwatch')
start = datetime.now()
input('Press enter to stop stopwatch')
end = datetime.now()
Stopwatch.stopwatch(start, end)