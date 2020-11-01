import datetime

def days_in_month(year,month):
    if(year>+datetime.MINYEAR and year<=datetime.MAXYEAR):
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            return 31
        elif(month==4 or month==6 or month==9 or month==11):
            return 30
        elif(month==2):
            if(((year%4)==0 and (year%100)!=0) or (year%400)==0):
                return 29
            else:
                return 28
        else:
            return "Incorrect input"
 
 
def is_valid_date(year, month, day):
    day_tot = days_in_month(year, month)
    if(day<=day_tot):
        if(day>0):
            return "valid"
    else:
        return "Incorrect input"
       
 
def days_between(year1, month1, day1, year2, month2, day2):
    if(is_valid_date(year1, month1, day1)=="valid"):
        if(is_valid_date(year2, month2, day2)=="valid"):
            date1=datetime.date(year1, month1, day1)
            date2=datetime.date(year2, month2, day2)
            if(date2>date1):
                diff= date2-date1
                return diff
    else:
        return "Incorrect input"
 

def age_in_days(year, month, day):
    todays_date = datetime.date.today()
    if(day>0):
        age=days_between(year, month, day,todays_date.year, todays_date.month, todays_date.day)
        return age
    
        
print("Which option do you choose")
print("1- To find days in a given month YYYY,MM \n2- To find if a given date is valid YYYY,MM,DD")
print("3- To find no. of days in between YYYY1,MM1,DD1,YYYY2,MM2,DD2 \n4- To find your age in days YYYY,MM,DD")
opt=input()
x=int(opt)
if(x==1):
    print("enter input")
    y=input()
    m=input()
    year=int(y)
    month=int(m)
    print(days_in_month(year,month))
elif(x==2):
    print("enter input")
    y=input()
    m=input()
    d=input()
    year=int(y)
    month=int(m)
    day=int(d)
    print(is_valid_date(year, month, day))
elif(x==3):
    print("enter input")
    y1=input()
    m1=input()
    d1=input()
    year1=int(y1)
    month1=int(m1)
    day1=int(d1)
    y2=input()
    m2=input()
    d2=input()
    year2=int(y2)
    month2=int(m2)
    day2=int(d2)
    print(days_between(year1, month1, day1, year2, month2, day2))
elif(x==4):
    print("enter input")
    y=input()
    m=input()
    d=input()
    year=int(y)
    month=int(m)
    day=int(d)
    print(age_in_days(year, month, day))
else:
    print("Invalid Input")