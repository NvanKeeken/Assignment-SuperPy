import datetime
import calendar
import fileinput

def advance_time(day=0):
    date_today = datetime.date.today()
    advanced_date = date_today +  datetime.timedelta(days = day)
    with open("currentDate.txt", "w") as file:
            file.write(advanced_date.strftime("%Y-%m-%d"))

def set_date_today():
      with open("currentDate.txt", "w") as file:
            date_today= datetime.date.today()
            file.write(date_today.strftime("%Y-%m-%d"))

def get_date_now():
     return datetime.date.today().strftime("%Y-%m-%d")

def get_date_yesterday():
      current_date = get_date_file()
      decremented_date = datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days = 1)
      return decremented_date.strftime("%Y-%m-%d")

def get_date_file():
      with open("currentDate.txt", "r") as f:
            for line in f.readlines():
                print(line)
                return line

def get_date_Format(date):
    try:
      if date == datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d"):
            return "%Y-%m-%d"
    except ValueError:
      try:
          if date == datetime.datetime.strptime(date, "%Y-%m").strftime("%Y-%m"):
            return "%Y-%m"
      except ValueError:
           try:
               if date == datetime.datetime.strptime(date, "%Y").strftime("%Y"):
                  return "%Y"
           except ValueError:
                raise ValueError("format must be '%Y-%m-%d', '%Y-%m' or '%Y'")
           
def get_month(date):
     date_format = get_date_Format(date)
     if date_format == "%Y-%m":
        month = int(datetime.datetime.strptime(date, "%Y-%m").strftime("%m").lstrip("0").replace(" 0", " "))
        year = datetime.datetime.strptime(date, "%Y-%m").strftime("%Y")
        return calendar.month_name[month] +" " + year
     else:
          return date
print(get_month("2023"))
     

                
        
