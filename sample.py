import ghasedakpack

from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
tesla = TA_Handler(


symbol="MATICUSDT",
screener="crypto",
exchange="Kucoin",
interval=Interval.INTERVAL_4_HOURS,

#INTERVAL_1_MINUTE = "1m"
#INTERVAL_5_MINUTES = "5m"
#INTERVAL_15_MINUTES = "15m"
#INTERVAL_30_MINUTES = "30m"
#INTERVAL_1_HOUR = "1h"
#INTERVAL_2_HOURS = "2h"
#INTERVAL_4_HOURS = "4h"
#INTERVAL_1_DAY = "1d"
#INTERVAL_1_WEEK = "1W"
#INTERVAL_1_MONTH = "1M"

# proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
close=tesla.get_analysis().indicators["close"]

if close<=0.8288:
    
    sms = ghasedakpack.Ghasedak("a38fbde9eefdf9c7034357178b235a2565b50d41fd477252caee205662ce6dea")
    sms.send({'message':'ماتیک به 0.8288 رسید ', 'receptor' :'09303014331' , 'linenumber': '30005006007564' }
    
)







