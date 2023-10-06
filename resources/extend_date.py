from datetime import datetime,timedelta

def extend_license(date,time_months):
    date = str(date)
    date_format = '%Y-%m-%d %H:%M:%S'
    date_obj = datetime.strptime(date, date_format)
    if (date_obj < datetime.now()):
        date_obj = datetime.now()
    date_obj = date_obj + timedelta(time_months*30)
    return str(date_obj)