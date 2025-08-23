def add_time(start, duration,day=''):
    parts=start.split()
    dictionarie={
        "Monday":0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday":6

    }
    

    time=parts[1]
    parts1=parts[0].split(':')
    hour=parts1[0]
    minutes=parts1[1]
    parts2=duration.split(':')
    add_hour=parts2[0]
    add_minutes=parts2[1]
    final_minutes=int(minutes)+int(add_minutes)
    if (final_minutes)>=60:
        final_hour=int(hour)+int(add_hour)+1
    else:
        final_hour=int(hour)+int(add_hour)
    xio=0
    if time=="PM":
        xio  =(final_hour+12)//24
    else:
        xio=final_hour//24
    period_changes = (final_hour // 12)
    n=""
    if xio==1:
        n=" (next day)"
    if xio>1:
        n=" ("+str(xio)+" days later)"
    if period_changes % 2 == 1:
        time = "PM" if time == "AM" else "AM"

    final_minutes=final_minutes%60
    final_hour=final_hour%12
    aux_final_minutes=''
    if final_hour==0:
        final_hour="12"
    if final_minutes<10:
        aux_final_minutes='0'+str(final_minutes)
    else:
        aux_final_minutes = str(final_minutes)
    results=str(final_hour)+':'+aux_final_minutes+' '+time
    if day:
        day=day.capitalize()
        
        t = (dictionarie[day] + xio) % 7
        for key, value in dictionarie.items():
            if value == t:
                results +=", "+key
    results+=n
    return results



