import random
import calendar
import datetime


def  print_random_date(start_date:datetime.date, end_date:datetime.date)-> None:
    """
    A function that prints a random date in range and if the date Monday prints :"I do not have a vinaigrette".
    :param start_date: start_date:Start date of the range(format YYYY-MM-DD).
    :param end_date: end_date:End date of the range (format YYYY-MM-DD).
    """
    random_date = get_random_date_in_range(start_date, end_date)
    print(random_date)
    if get_if_is_monday(random_date):
        print("I don't have vinaigrette!")


def get_random_date_in_range(start_date:datetime.date,end_date:datetime.date)->datetime.date:
    """
    A function that receives a range and returns a random date in the range.
    :param start_date:Start date (format YYYY-MM-DD).
    :param end_date:End date (format YYYY-MM-DD).
    :return:Random date.
    """
    days_between_dates = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def get_if_is_monday(random_date:datetime.date)->bool:
    """
    Check if the random day is Monday.
    :param random_date:Random date to check.
    :return:True if it's Monday Otherwise false.
    """
    return calendar.day_name[random_date.weekday()] == 'Monday'


if __name__== '__main__':
    #Select dates in the format YYYY-MM-DD.
    start_date = datetime.date(2010, 3, 1)
    end_date = datetime.date(2012, 3, 1)
    print_random_date(start_date, end_date)
