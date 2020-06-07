def formatTime(timeString):
    if 'p' in timeString.lower():
        index = timeString.lower().index('p')
        time = timeString[:index].strip()
        timeString = time + 'P.M.'
    elif 'a' in timeString.lower():
        index = timeString.lower().index('a')
        time = timeString[:index].strip()
        timeString = time + 'A.M.'
    return timeString

def getTimeDifferenceInhours(bedTime, wakeUpTime):
    if 'P.M.' in bedTime:
        mrngHour,mrngMinute = wakeUpTime.replace('A.M.','').split(':')
        nightHour,nightMinute = bedTime.replace('P.M.','').split(':')
        minutes = (60 - int(nightMinute)) + int(mrngMinute)
        if minutes >= 60:
            minutes = minutes - 60
            hours =  int(mrngHour) + (12 - int(nightHour))
        else:
            hours = int(mrngHour) + (12 - int(nightHour)) - 1

    elif 'A.M.' in bedTime:
        mrngHour,mrngMinute = wakeUpTime.replace('A.M.','').split(':')
        nightHour,nightMinute = bedTime.replace('A.M.','').split(':')
        minutes = (60 - int(nightMinute)) + int(mrngMinute)
        if minutes >= 60:
            minutes = minutes - 60
            hours = int(mrngHour) - int(nightHour)
            if int(nightHour) == 12:
                 hours =  int(mrngHour) + (12 - int(nightHour))
        else:
            hours = int(mrngHour) - int(nightHour) - 1
            if int(nightHour) == 12:
                 hours =  int(mrngHour) + (12 - int(nightHour)) - 1
    if minutes != 60:
        minutes = minutes / 60
    return round(hours+minutes,2)
