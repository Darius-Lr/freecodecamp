def add_time(start,duration,day=''):
    parts=start.split()
    tm=parts[1]
    numberday=0
    days ={
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    if day:
        day=day.capitalize()
        numberday=days[day]
    totaldays=0
    if tm=="PM":
        totaldays+=12
    parts1=parts[0].split(":")
    parts2=duration.split(":")
    parts1[0]=int(parts1[0])
    parts1[1] = int(parts1[1])
    parts2[0] = int(parts2[0])
    parts2[1] = int(parts2[1])
    time1=parts1[0]+parts2[0]

    time2=parts1[1]+parts2[1]
    time1+=time2//60
    totaldays+=time1
    totaldays//=24
    time2=time2%60
    howmany=time1//12
    while howmany!=0:
        howmany-=1
        if tm=="AM":
            tm="PM"
        else:
            tm="AM"
    time1=time1%12
    time2=str(time2)
    if len(time2)<2:
        time2='0'+time2
    if time1==0:
        time1=12
    string=str(time1)+':'+time2+' '+tm
    numberday=(numberday+totaldays)%7
    if day:
        for key, value in days.items():
            if value == numberday:
                string+=", "+key
    if totaldays==1:
        string+=" (next day)"
    elif totaldays>1:
        string+=" ("+str(totaldays)+" days later)"

    return string

if __name__ == '__main__':
    add_time('3:30 PM', '2:12')
