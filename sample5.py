from tradingview_ta import*
import tradingview_ta
import time
import numpy as np
import pandas as pd
import datetime
import pandas_ta as pta


from tradingview_ta import TA_Handler, Interval, Exchange




datarsi305=[]
datarsi3015=[]
datarsi3030=[]
datarsi301=[]
datarsi304=[]
datarsi30d=[]

datarsi705=[]
datarsi7015=[]
datarsi7030=[]
datarsi701=[]
datarsi704=[]
datarsi70d=[]

datamacd5=[]
data15=[]
datamacd30=[]
datamacd1=[]
datamacd4=[]
datamacdd=[]


dataichit5=[]
dataichit15=[]
dataichit30=[]
dataichit1=[]
dataichit4=[]
dataichitd=[]

    
dataichint5=[]
dataichint15=[]
dataichint30=[]
dataichint1=[]
dataichint4=[]
dataichintd=[]

dataichiA5=[]
dataichiA15=[]
dataichiA30=[]
dataichiA1=[]
dataichiA4=[]
dataichiAd=[]

dataichiB5=[]
dataichiB15=[]
dataichiB30=[]
dataichiB1=[]
dataichiB4=[]
dataichiBd=[]


databbup5=[]
databbdown5=[]


datacci1005=[]
dataccii1005=[]

dataadxi5=[]


symbols=["BTCUSDT","ADAUSDT","AVAXUSDT","ETHUSDT","LUNAUSDT","XRPUSDT","FTMUSDT","SOLUSDT","ATOMUSDT","SANDUSDT","ONEUSDT","LINKUSDT","TRXUSDT","DOGEUSDT","WAVESUSDT","XMRUSDT","ZECUSDT","NEARUSDT",'KDAUSDT','IMXUSDT','MANAUSDT','JASMYUSDT','KOKUSDT','SHIBUSDT','DOTUSDT','VETUSDT','ICPUSDT','BNBUSDT','MATICUSDT','GALAUSDT','AXSUSDT','HBARUSDT','APEUSDT','FILUSDT','AAVEUSDT','EGLDUSDT','THETAUSDT','HNTUSDT','BSVUSDT','EOSUSDT','MKRUSDT','ZECUSDT','RUNEUSDT','XECUSDT','GRTUSDT','HTUSDT','KLAYUSDT','BATUSDT','ZILUSDT','STXUSDT','PAXGUSDT','LRCUSDT','CAKEUSDT','CVXUSDT','CELOUSDT','XEMUSDT','COMPUSDT','STORJUSDT','CROUSDT','QNTUSDT','MKRUSDT','XECUSDT','KLAYUSDT','CHZUSDT','CRVUSDT','BATUSDT','STXUSDT','ZILUSDT','ARUSDT','COMPUSDT','OPUSDT','RUNEUSDT','SNXUSDT','CRVUSDT','DYDXUSDT','AXSUSDT','RNDRUSDT','ELONUSDT','ROSEUSDT','JUPUSDT','BTTUSDT','PYRUSDT','UNIUSDT','GSTUSDT','FLOWUSDT','CTCUSDT','CFGUSDT','OXTUSDT','OGNUSDT','REEFUSDT','BOBAUSDT','BFCUSDT','TRIBEUSDT','EWTUSDT','ILVUSDT','RLCUSDT','ADSUSDT','ACHUSDT','PROMUSDT','RSRUSDT','ORBSUSDT','RACAUSDT','XNOUSDT','RLYUSDT','POWRUSDT','SYSUSDT','DAGUSDT','GALUSDT','FORTHUSDT','NMRUSDT','CTSIUSDT','AURORAUSDT','WRXUSDT']




for x in symbols:
    
    
    from tradingview_ta import TA_Handler, Interval, Exchange
    import tradingview_ta
    tesla = TA_Handler(
        
        
    symbol=x,
    screener="crypto",
    exchange="Kucoin",
    interval=Interval.INTERVAL_5_MINUTES,
    
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
        
    rsi=tesla.get_analysis().indicators["RSI"]
    macd=tesla.get_analysis().indicators["MACD.macd"]
    macds=tesla.get_analysis().indicators["MACD.signal"] 
    
    cci=tesla.get_analysis().indicators["CCI20"]
    
    
    adx1=tesla.get_analysis().indicators["ADX+DI"]
    adx2=tesla.get_analysis().indicators["ADX-DI"]



    
    #ichimokue
    from tvDatafeed import TvDatafeed, Interval
    tv=TvDatafeed()
    
    df=tv.get_hist(symbol=x,exchange="Kucoin",interval=Interval.in_5_minute,n_bars=100, extended_session=False)
    
    nine_period_high = df['high'].rolling(window=9).max()
    nine_period_low = df['low'].rolling(window=9).min()
    df['tenkan-sen'] = (nine_period_high + nine_period_low ) / 2
    
    
    period26_high = df['high'].rolling(window=26).max()
    period26_low = df['low'].rolling(window=26).min()
    df['kijun-sen'] = (period26_high + period26_low ) / 2
    
    
    df['senkou-span-A'] = ((df['tenkan-sen'] + df['kijun-sen'])/2).shift(26)
    
    
    period52_high = df['high'].rolling(window=52).max()
    period52_low = df['low'].rolling(window=52).min()
    df['senkou-span-B'] = ((period52_high + period52_low ) / 2).shift(26)
    
    
    bband=pta.bbands(df['close'],length=20,std=2,offset=0)
    
    
    
    

    
    
    if df['close'][99]>bband['BBL_20_2.0'][99]:
        databbdown5.append(x)
        
    if bband['BBM_20_2.0'][99]<df['close'][99]< bband['BBU_20_2.0'][99]:
        
        databbup5.append(x)
    
    
    if cci>100:
        datacci1005.append(x)
    
    if cci<-100:
        dataccii1005.append(x)
    
    
    if adx1>adx2:
        dataadxi5.append(x)
    
    
        
    
    
    if rsi<30:
        
        datarsi305.append(x)
    if rsi>70:
        datarsi705.append(x)
    
    if macd>macds:
        datamacd5.append(x)
    
    
    
        

    if df['tenkan-sen'][99]>df['kijun-sen'][99]:
        
        
        
        
        dataichit5.append(x)   
    
    
    if df['tenkan-sen'][99]<df['kijun-sen'][99]:
        
        dataichint5.append(x)   
    
    
    
    if  df['senkou-span-A'][99]>df['senkou-span-B'][99]:
        dataichiA5.append(x)
    
    else:
        
        dataichiB5.append(x)
        
        
if datarsi305==[]:
    
    
    with open('/home/indbit/project/mysite/static/rsi305.txt', 'w',encoding="utf-8") as f2:
        

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    
    
    with open('/home/indbit/project/mysite/static/rsi305.txt', 'w',encoding="utf-8") as f2:
        
    

        for line in datarsi305:
    
    

            f2.write(line)
            f2.write('\n')
    

if datarsi705==[]:
    
    
    
    with open('/home/indbit/project/mysite/static/rsi705.txt', 'w',encoding="utf-8") as f2:
        

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    
    with open('/home/indbit/project/mysite/static/rsi705.txt', 'w',encoding="utf-8") as f2:
        
    
    
        for line in datarsi705:
            f2.write(line)
            f2.write('\n')
    

if datamacd5==[]:

    with open('/home/indbit/project/mysite/static/macd5.txt', 'w',encoding="utf-8") as f2:
        
            
        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/macd5.txt', 'w',encoding="utf-8") as f2:

        for line in datamacd5:

            f2.write(line)
            f2.write('\n')
    


if dataichit5==[]:
    
    
    
    with open('/home/indbit/project/mysite/static/ichit55.txt', 'w',encoding="utf-8") as f3:
        
        
            
        data="سکه ای یافت نشد" 
        
        f3.write(data)        

else:
            
    with open('/home/indbit/project/mysite/static/ichit55.txt', 'w',encoding="utf-8") as f4:
        
        for line in dataichit5:
            
            f4.write(line)
            f4.write('\n')        
    

if dataichint5==[]:
    
    
    with open('/home/indbit/project/mysite/static/ichint55.txt', 'w',encoding="utf-8") as f5:
        
            
        data="سکه ای یافت نشد"  
        f5.write(data)        

else:
    
    
    with open('/home/indbit/project/mysite/static/ichint55.txt', 'w',encoding="utf-8") as f6:
        
        for line in dataichint5:
            
            f6.write(line)
            f6.write('\n') 




if dataichiA5==[]:

    with open('/home/indbit/project/mysite/static/ichiA5.txt', 'w',encoding="utf-8") as f2:

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/ichiA5.txt', 'w',encoding="utf-8") as f2:

        for line in dataichiA5:
        

            f2.write(line)
            f2.write('\n')   

    

if dataichiB5==[]:
    
    
    

    with open('/home/indbit/project/mysite/static/ichiB5.txt', 'w',encoding="utf-8") as f2:

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/ichiB5.txt', 'w',encoding="utf-8") as f2:
        

        for line in dataichiB5:
            

            f2.write(line)
            f2.write('\n')     
    



            
        
if databbup5==[]:

    with open('/home/indbit/project/mysite/static/bbandup5.txt', 'w',encoding="utf-8") as f2:

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:

    with open('/home/indbit/project/mysite/static/bbandup5.txt', 'w',encoding="utf-8") as f2:

        for line in databbup5:

            f2.write(line)
            f2.write('\n')
    
    

if databbdown5==[]:
    
    
    

    with open('/home/indbit/project/mysite/static/bbanddown5.txt', 'w',encoding="utf-8") as f2:
        

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    
    

    with open('/home/indbit/project/mysite/static/bbanddown5.txt', 'w',encoding="utf-8") as f2:
 
        for line in databbdown5:
            

            f2.write(line)
            f2.write('\n')




if datacci1005==[]:
    
    

    with open('/home/indbit/project/mysite/static/cci1005.txt', 'w',encoding="utf-8") as f2:

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    

    with open('/home/indbit/project/mysite/static/cci1005.txt', 'w',encoding="utf-8") as f2:
    

        for line in datacci1005:

            f2.write(line)
            f2.write('\n')



if dataccii1005==[]:
    
    

    with open('/home/indbit/project/mysite/static/cci-1005.txt', 'w',encoding="utf-8") as f2:

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    

    with open('/home/indbit/project/mysite/static/cci-1005.txt', 'w',encoding="utf-8") as f2:
    

        for line in dataccii1005:

            f2.write(line)
            f2.write('\n')


if dataadxi5==[]:
    
    

    with open('/home/indbit/project/mysite/static/adxi5.txt', 'w',encoding="utf-8") as f2:

        data="سکه ای یافت نشد"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/adxi5.txt', 'w',encoding="utf-8") as f2:

        for line in dataadxi5:

            f2.write(line)
            f2.write('\n')










    
    
    
    
        
    
    
            

        
    
    


    

# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}