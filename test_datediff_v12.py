import pytest
from datediff_final_ver12 import findDateDifference
from datetime import date

@pytest.mark.parametrize("start, end",[
   #Same day
   ("02/08/2021","02/08/2021"),
   #Same month diff day
   ("01/08/2021","20/08/2021"),
    #Same year diff month
   ("01/01/2021","20/08/2021"),
    #Adjuscent year
   ("01/08/2020","20/08/2021"),
    #Diffeent year
   ("01/08/2010","20/08/2021"),
   ("01/08/2010","20/08/3000"),
   ("01/08/1900","20/08/2999"),
   ("01/08/19//","20/08/29"),

   ])
def test_multiplication_11(start,end):
   d0,m0,y0 = getDateSplit(start)
   d1,m1,y1 = getDateSplit(end)
   res = findDateDifference(start,end)
   assert res== dateDifference(d0,m0,y0,d1,m1,y1)

def dateDifference(day,month,year, day1,month1,year1):
   d0 = date(year, month, day)
   d1 = date(year1, month1, day1)
   delta = d1 - d0
   print(delta.days)
   return delta.days

def getDateSplit(date):
   day,month,year = date.split("/")
   return int(day), int(month), int(year)
   