from time import sleep
from datetime import datetime
from pytz import timezone


textFile = open("time.txt", 'w')
count = 0
constant = 0
timeList = ['America/New_York', 'UTC', 'Europe/Berlin', 'US/Pacific']
listNum = 0
timeZone
while constant = 0:
  count = 0
  if listNum == 3:
    listNum = 0
  else:
    listNum += 1
  timeZone = timeList[listNum]
  while count < 100:
    nowTime = datetime.now(timezone(timeZone))
    textFile.write(now_time.strftime(fmt))
    count +=1
    sleep(0.1)
