import random
import calendar
import datetime
import os
from os import listdir
from os.path import join, isfile
import pathlib

#a function that returns the name of all directory that start with deep in the path he get
def list_dir_start_with_deep(path):
     return [ file for file in listdir(path) if file.startswith('deep') and os.path.isdir(os.path.join(path, file))]


def  print_random_date(s_date, e_date):
    """
    A function that prints a random date in range and if the date Monday prints I do not have a vinaigrette
    :param s_date: s_date:start date (format YYYY-MM-DD)
    :param e_date: e_date:end date (format YYYY-MM-DD)
    """
    random_date = get_random_date_in_range(s_date, e_date)
    print(random_date)
    if get_if_is_tuesday(random_date): print("I don't have vinaigrette!")

def get_random_date_in_range(s_date,e_date):
    """
    A function that receives a range and returns a random date in the range
    :param s_date:start date (format YYYY-MM-DD)
    :param e_date:end date (format YYYY-MM-DD)
    :return:random date
    """
    days_between_dates = (e_date - s_date).days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = s_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def get_if_is_tuesday(random_date):
    """
    check if the random day is Monday
    :param random_date:
    :return:true if it's Monday Otherwise false
    """
    return calendar.day_name[random_date.weekday()] == 'Tuesday'



if __name__== '__main__':
    #Select dates in the format YYYY-MM-DD
    s_date = datetime.date(2010, 3, 1)
    e_date = datetime.date(2012, 3, 1)
    print_random_date(s_date, e_date)
    path = 'C:\\Users\\user\\Desktop\\ortalYatzkan'
    print(list_dir_start_with_deep(path))