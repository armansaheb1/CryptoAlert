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
datamacd15=[]
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

databbup15=[]
databbdown15=[]


datacci10015=[]
dataccii10015=[]

dataadxi15=[]




symbols=["BTCUSDT","ADAUSDT","AVAXUSDT","ETHUSDT","LUNAUSDT","XRPUSDT","FTMUSDT","SOLUSDT","ATOMUSDT","SANDUSDT","ONEUSDT","LINKUSDT","TRXUSDT","DOGEUSDT","WAVESUSDT","XMRUSDT","ZECUSDT","NEARUSDT",'KDAUSDT','IMXUSDT','MANAUSDT','JASMYUSDT','KOKUSDT','SHIBUSDT','DOTUSDT','VETUSDT','ICPUSDT','BNBUSDT','MATICUSDT','GALAUSDT','AXSUSDT','HBARUSDT','APEUSDT','FILUSDT','AAVEUSDT','EGLDUSDT','THETAUSDT','HNTUSDT','BSVUSDT','EOSUSDT','MKRUSDT','ZECUSDT','RUNEUSDT','XECUSDT','GRTUSDT','HTUSDT','KLAYUSDT','BATUSDT','ZILUSDT','STXUSDT','PAXGUSDT','LRCUSDT','CAKEUSDT','CVXUSDT','CELOUSDT','XEMUSDT','COMPUSDT','STORJUSDT','CROUSDT','QNTUSDT','MKRUSDT','XECUSDT','KLAYUSDT','CHZUSDT','CRVUSDT','BATUSDT','STXUSDT','ZILUSDT','ARUSDT','COMPUSDT','OPUSDT','RUNEUSDT','SNXUSDT','CRVUSDT','DYDXUSDT','AXSUSDT','RNDRUSDT','ELONUSDT','ROSEUSDT','JUPUSDT','BTTUSDT','PYRUSDT','UNIUSDT','GSTUSDT','FLOWUSDT','CTCUSDT','CFGUSDT','OXTUSDT','OGNUSDT','REEFUSDT','BOBAUSDT','BFCUSDT','TRIBEUSDT','EWTUSDT','ILVUSDT','RLCUSDT','ADSUSDT','ACHUSDT','PROMUSDT','RSRUSDT','ORBSUSDT','RACAUSDT','XNOUSDT','RLYUSDT','POWRUSDT','SYSUSDT','DAGUSDT','GALUSDT','FORTHUSDT','NMRUSDT','CTSIUSDT','AURORAUSDT','WRXUSDT']




for x in symbols:
    
    
    from tradingview_ta import TA_Handler, Interval, Exchange
    import tradingview_ta
    tesla = TA_Handler(
        
        
    symbol=x,
    screener="crypto",
    exchange="Kucoin",
    interval=Interval.INTERVAL_15_MINUTES,
    
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
    
    df=tv.get_hist(symbol=x,exchange="Kucoin",interval=Interval.in_15_minute,n_bars=100, extended_session=False)
    
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
        databbdown15.append(x)
        
    if bband['BBM_20_2.0'][99]<df['close'][99]< bband['BBU_20_2.0'][99]:
        
        databbup15.append(x)
    
    
    if cci>100:
        datacci10015.append(x)
    
    if cci<-100:
        dataccii10015.append(x)
    
    
    if adx1>adx2:
        dataadxi15.append(x)
    
    
    
    
    
    
    if rsi<30:
        
        datarsi3015.append(x)
    if rsi>70:
        datarsi7015.append(x)
    
    if macd>macds:
        datamacd15.append(x)
    
    
    

    if df['tenkan-sen'][99]>df['kijun-sen'][99]:
        
        
        
        
        dataichit15.append(x)   
    
    
    if df['tenkan-sen'][99]<df['kijun-sen'][99]:
        
        dataichint15.append(x)   
    
    
    
    if  df['senkou-span-A'][99]>df['senkou-span-B'][99]:
        dataichiA15.append(x)
    
    else:
        
        dataichiB15.append(x)
        
        
if datarsi3015==[]:
    
    
    with open('/home/indbit/project/mysite/static/rsi3015.txt', 'w',encoding="utf-8") as f2:
        

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    
    
    with open('/home/indbit/project/mysite/static/rsi3015.txt', 'w',encoding="utf-8") as f2:
        
    

        for line in datarsi3015:
    
    

            f2.write(line)
            f2.write('\n')
    

if datarsi7015==[]:
    
    
    
    with open('/home/indbit/project/mysite/static/rsi7015.txt', 'w',encoding="utf-8") as f2:
        

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    
    with open('/home/indbit/project/mysite/static/rsi7015.txt', 'w',encoding="utf-8") as f2:
        
    
    
        for line in datarsi7015:
            f2.write(line)
            f2.write('\n')
    

if datamacd15==[]:

    with open('/home/indbit/project/mysite/static/macd15.txt', 'w',encoding="utf-8") as f2:
        
            
        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/macd15.txt', 'w',encoding="utf-8") as f2:

        for line in datamacd15:

            f2.write(line)
            f2.write('\n')
    


if dataichit15==[]:
    
    
    
    with open('/home/indbit/project/mysite/static/ichit15.txt', 'w',encoding="utf-8") as f3:
        
        
            
        data="?????? ???? ???????? ??????" 
        
        f3.write(data)        

else:
            
    with open('/home/indbit/project/mysite/static/ichit15.txt', 'w',encoding="utf-8") as f4:
        
        for line in dataichit15:
            
            f4.write(line)
            f4.write('\n')        
    

if dataichint15==[]:
    
    
    with open('/home/indbit/project/mysite/static/ichint15.txt', 'w',encoding="utf-8") as f5:
        
            
        data="?????? ???? ???????? ??????"  
        f5.write(data)        

else:
    
    
    with open('/home/indbit/project/mysite/static/ichint15.txt', 'w',encoding="utf-8") as f6:
        
        for line in dataichint15:
            
            f6.write(line)
            f6.write('\n') 




if dataichiA15==[]:

    with open('/home/indbit/project/mysite/static/ichiA15.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/ichiA15.txt', 'w',encoding="utf-8") as f2:

        for line in dataichiA15:
        

            f2.write(line)
            f2.write('\n')   

    

if dataichiB15==[]:
    
    
    

    with open('/home/indbit/project/mysite/static/ichiB15.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/ichiB15.txt', 'w',encoding="utf-8") as f2:
        

        for line in dataichiB15:
            

            f2.write(line)
            f2.write('\n')     




if databbup15==[]:

    with open('/home/indbit/project/mysite/static/bbandup15.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:

    with open('/home/indbit/project/mysite/static/bbandup15.txt', 'w',encoding="utf-8") as f2:

        for line in databbup15:

            f2.write(line)
            f2.write('\n')
    
    

if databbdown15==[]:
    

    with open('/home/indbit/project/mysite/static/bbanddown15.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    

    with open('/home/indbit/project/mysite/static/bbanddown15.txt', 'w',encoding="utf-8") as f2:
    

        for line in databbdown15:

            f2.write(line)
            f2.write('\n')




if datacci10015==[]:
    
    

    with open('/home/indbit/project/mysite/static/cci10015.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    

    with open('/home/indbit/project/mysite/static/cci10015.txt', 'w',encoding="utf-8") as f2:
    

        for line in datacci10015:

            f2.write(line)
            f2.write('\n')



if dataccii10015==[]:
    
    

    with open('/home/indbit/project/mysite/static/cci-10015.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    

    with open('/home/indbit/project/mysite/static/cci-10015.txt', 'w',encoding="utf-8") as f2:
    

        for line in dataccii10015:

            f2.write(line)
            f2.write('\n')


if dataadxi15==[]:
    
    

    with open('/home/indbit/project/mysite/static/adxi15.txt', 'w',encoding="utf-8") as f2:

        data="?????? ???? ???????? ??????"  
        f2.write(data)        

else:
    
    with open('/home/indbit/project/mysite/static/adxi15.txt', 'w',encoding="utf-8") as f2:

        for line in dataadxi15:

            f2.write(line)
            f2.write('\n')





    
    


    
    
    
    
        
    
    
            

        
    
    


    

# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}