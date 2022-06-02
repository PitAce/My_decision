import datetime

def date_in_future(integer):
    cur_date = datetime.datetime.now()
    
    if type(integer) != int:
        return(cur_date.strftime('%m-%d-%Y %H:%M:%S')) # or %d-%m-%Y ?

    
    days = datetime.timedelta(days = integer)
    new_date = cur_date + days
    return(new_date.strftime('%m-%d-%Y %H:%M:%S'))
