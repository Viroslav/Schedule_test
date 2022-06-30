from datetime import datetime, timedelta

#import pandas as pd


#def task_time(start_time, end_time):
 #   delta = datetime.timedelta(end_time, start_time)
  #  print(delta)


def plan(task: str, start_time: datetime.hour, end_time: datetime.hour):
    print(task, start_time, end_time)
    print(end_time - start_time)


plan(str(input()), input(), input())
