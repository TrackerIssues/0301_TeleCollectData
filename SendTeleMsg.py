import asyncio
import telegram
import datetime
from pytz import timezone, utc
import sys

from SetTimeZone import NowDateTime

KST = timezone('Asia/Seoul')

dtKorea = NowDateTime(KST)

sExtMsg = ""
with open("dfMsg.csv", "r") as f :
    lstLines = f.readlines()
    for line in lstLines :
        sExtMsg += line

sMsg = dtKorea.strftime('%Y-%m-%d %H:%M') + """

Ta~Da~ External Argv

Real Time Keyword~

""" + sExtMsg

async def main() :
    bot = telegram.Bot(sToken)
    async with bot :
        # print(await bot.get_me())
        await bot.send_message(text=sMsg, chat_id=sId)

if __name__ == '__main__' :
    sId = sys.argv[1]
    sToken = sys.argv[2]
    # print(sId)
    # print(sToken)
    asyncio.run( main())
