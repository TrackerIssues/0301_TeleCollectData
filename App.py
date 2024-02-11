
from SetTimeZone import NowDateTime
from CollectRequests import *
from CollectWebDriver import signal_crawler


from pytz import timezone
import time 
import os
import pandas as pd


KST = timezone('Asia/Seoul')

dtKorea = NowDateTime(KST)

sDate = (dtKorea.strftime('%Y%m%d%H%M'))

def list_print(lstData) :
  for i in range( len( lstData )):
    print( str(i+1) + "위" + lstData[i])
  
##################################################
  
print(sDate)

lstRank = [ str(i) for i in range(1, 11) ]
lstNateKeyword = []
lstGoogleKeyword = []
lstZumKeyword = []
lstSignalKeyword = []


lstSignalKeyword = signal_crawler()
# time.sleep(3)
list_print(lstSignalKeyword)

lstNateKeyword = nate_crawler( sDate )
# time.sleep(1)
list_print(lstNateKeyword)
lstZumKeyword = zum_crawler()
# time.sleep(1)
list_print(lstZumKeyword)
lstGoogleKeyword = google_crawler()
# time.sleep(1)
list_print(lstGoogleKeyword)

list_print(lstRank)



dfMsg = pd.DataFrame( { "Rank" : lstRank, "Signal":lstSignalKeyword, "Zum" : lstZumKeyword, "Nate" : lstNateKeyword, "Google" : lstGoogleKeyword } )
dfMsg.to_csv("dfMsg.csv", index=False)

if os.path.isfile("dfKeyWord.csv") :
  dfKeyWord = pd.read_csv("dfKeyWord.csv")
  dfKeyWordPlus = pd.DataFrame( { "Date" : sDate, "Rank" : lstRank, "Signal":lstSignalKeyword, "Zum" : lstZumKeyword, "Nate" : lstNateKeyword, "Google" : lstGoogleKeyword } )
  dfKeyWord = pd.concat([dfKeyWord, dfKeyWordPlus])
  dfKeyWord.to_csv("dfKeyWord.csv", index=False)
else :
  dfKeyWord = pd.DataFrame( { "Date" : sDate, "Rank" : lstRank, "Signal":lstSignalKeyword, "Zum" : lstZumKeyword, "Nate" : lstNateKeyword, "Google" : lstGoogleKeyword } )
  dfKeyWord.to_csv("dfKeyWord.csv", index=False)

print()
print("="*20 +" Pandas DataFram "+"="*20)
