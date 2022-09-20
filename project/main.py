from . import db
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, url_for, redirect
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import pandas as pd
import pandas_ta as pta
import numpy as np

from .models import User, Alert
from ta import add_all_ta_features
import datetime
from datetime import date
import time
import datetime
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
import ghasedakpack
sms = ghasedakpack.Ghasedak("a38fbde9eefdf9c7034357178b235a2565b50d41fd477252caee205662ce6dea")



def get_price(symbol, exchange):
    tesla = TA_Handler(


    symbol=symbol,
    screener="crypto",
    exchange= exchange,
    interval=Interval.INTERVAL_15_MINUTES,


    )
    close=tesla.get_analysis().indicators["close"]
    return close



main = Blueprint('main', __name__)

@main.route('/cron')
def checkalert():
    for item in Alert.query.filter_by(status = 0):
        price = get_price(item.coin, item.exchange)
        if item.path == 1:
            if item.price <= price:
                sms.send({'message':f'آلرت {item.coin} شما به قیمت {item.price} رسیده است' , 'receptor' : str(User.query.filter_by(id = item.user).phone), 'linenumber': '30005006007564' })
        else:
            if item.price >= price:
                sms.send({'message':f'آلرت {item.coin} شما به قیمت {item.price} رسیده است' , 'receptor' : str(User.query.filter_by(id = item.user).phone), 'linenumber': '30005006007564' })
    
    return 'hi'


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/price-alert')
@login_required
def price_alert(): 
    coins = ['a', 'b', 'c', 'd']
    alerts = Alert.query.all()
    return render_template('PriceAlert.html', coins = coins , alerts = alerts)

@main.route('/price-alert', methods=['POST'])
@login_required
def price_alert_post():
    coin = request.form.get('coin')
    exchange = request.form.get('exchange')
    price = float(request.form.get('price'))
    now = float(get_price(symbol=coin , exchange = exchange) )
    if price > now :
        path = 1
    if price < now :
        path = 0
    
        
    new_alert = Alert(user = current_user.id,coin = coin, exchange = exchange, price = price, path = path)

    # add the new user to the database
    db.session.add(new_alert)
    db.session.commit()
    coins = ['a', 'b', 'c', 'd']
    alerts = Alert.query.all()
    return redirect(url_for('main.price_alert'))
    return render_template('PriceAlert.html', coins = coins , alerts = alerts)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name , phone = current_user.phone)


@main.route("/macd")   
def index2():
    data=request.args.get("indicators")
    if data=="macd5":
        #f2=open("/home/indbit/project/mysite/static/a.txt", "r") 
        #f3=f2.read()
        text_file = open("/home/indbit/project/mysite/static/macd5.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
            
        with open('/home/indbit/project/mysite/static/macd5.txt') as fp:
            

            coins = set(fp.read().split())

    if data=="macd15":
        
        text_file = open("/home/indbit/project/mysite/static/macd15.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        with open('/home/indbit/project/mysite/static/macd15.txt') as fs:
            

            coins = set(fs.read().split())

    if data=="macd30":
        
        text_file = open("/home/indbit/project/mysite/static/macd30.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        
        
        
        with open('/home/indbit/project/mysite/static/macd30.txt') as fs2:
            
            

            coins = set(fs2.read().split())

    if data=="macd1":
        
        text_file = open("/home/indbit/project/mysite/static/macd1.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        
        with open('/home/indbit/project/mysite/static/macd1.txt') as fs3:
            
            

            coins = set(fs3.read().split())

    if data=="macd4":
        
        text_file = open("/home/indbit/project/mysite/static/macd4.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        

        with open('/home/indbit/project/mysite/static/macd4.txt') as fs4:
            
 
            coins = set(fs4.read().split())     

    if data=="macdd":
        
        text_file = open("/home/indbit/project/mysite/static/macdd.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        

        with open('/home/indbit/project/mysite/static/macdd.txt') as fs5:


            coins = set(fs5.read().split())                    

    return render_template('index.html',x=coins)

@main.route("/rsi")     
def index3():
    data=request.args.get("rsi")
    if data=="rsi5":
        
        
        text_file = open("/home/indbit/project/mysite/static/rsi705.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        
        with open('/home/indbit/project/mysite/static/rsi705.txt') as fs6:
            

            coins = set(fs6.read().split())
    
    if data=="rsi15":
        
        text_file = open("/home/indbit/project/mysite/static/rsi7015.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
            
        with open('/home/indbit/project/mysite/static/rsi7015.txt') as fs7:
            coins = set(fs7.read().split())


    if data=="rsi30":
        
        text_file = open("/home/indbit/project/mysite/static/rsi7030.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        with open('/home/indbit/project/mysite/static/rsi7030.txt') as fs8:
            coins = set(fs8.read().split())
    

    if data=="rsi1":
        
        text_file = open("/home/indbit/project/mysite/static/rsi701.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        with open('/home/indbit/project/mysite/static/rsi701.txt') as fs9:
            coins = set(fs9.read().split())
    
    
    if data=="rsi4":
        
        text_file = open("/home/indbit/project/mysite/static/rsi704.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')

        with open('/home/indbit/project/mysite/static/rsi704.txt') as fs10:      
            coins = set(fs10.read().split())

    if data=="rsid":
        
        
        text_file = open("/home/indbit/project/mysite/static/rsi70d.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        with open('/home/indbit/project/mysite/static/rsi70d.txt') as fs11:
            
            coins = set(fs11.read().split())
    
    return render_template('index.html',x=coins)

@main.route("/rsi2")     
def index4():
    data=request.args.get("rsi2")
    if data=="rsi5":
        
        
        text_file = open("/home/indbit/project/mysite/static/rsi305.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        with open('/home/indbit/project/mysite/static/rsi305.txt') as fs12:
            coins = set(fs12.read().split())
    
    if data=="rsi15":
        
        
        text_file = open("/home/indbit/project/mysite/static/rsi3015.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        with open('/home/indbit/project/mysite/static/rsi3015.txt') as fs13:
            coins = set(fs13.read().split())


    if data=="rsi30":
        
        text_file = open("/home/indbit/project/mysite/static/rsi3030.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        
        
        with open('/home/indbit/project/mysite/static/rsi3030.txt') as fs14:
            coins = set(fs14.read().split())
    

    if data=="rsi1":
        
        text_file = open("/home/indbit/project/mysite/static/rsi301.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')

        with open('/home/indbit/project/mysite/static/rsi301.txt') as fs15:
            coins = set(fs15.read().split())
    
    
    if data=="rsi4":
        
        text_file = open("/home/indbit/project/mysite/static/rsi304.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')

        with open('/home/indbit/project/mysite/static/rsi304.txt') as fs16:      
            coins = set(fs16.read().split())

    if data=="rsid":
        text_file = open("/home/indbit/project/mysite/static/rsi30d.txt", "r",encoding='utf-8')
        f=text_file.read() 
        if f=="سکه ای یافت نشد" :
            return render_template('index9.html')
        with open('/home/indbit/project/mysite/static/rsi30d.txt') as fs17:
            
            coins = set(fs17.read().split())
    
    return render_template('index.html',x=coins)

@main.route("/ichimokue")
def index5():

        data=request.args.get("ichimokue")
        data2=request.args.get("ichimokuen")
        if data=="ichimokue":
            if data2=="ichimokue5":
                with open('/home/indbit/project/mysite/static/ichit55.txt') as fs18:
                    coins = set(fs18.read().split())
            
            if data2=="ichimokue15":
                with open('/home/indbit/project/mysite/static/ichit15.txt') as fs19:
                    coins = set(fs19.read().split())

            if data2=="ichimokue30":            
                with open('/home/indbit/project/mysite/static/ichit30.txt') as fs20:
                    coins = set(fs20.read().split())

            if data2=="ichimokue1":            
                with open('/home/indbit/project/mysite/static/ichit1.txt') as fs21:

                    coins = set(fs21.read().split())
            
            
            if data2=="ichimokue4":

                with open('/home/indbit/project/mysite/static/ichit4.txt') as fs22:


                    coins = set(fs22.read().split())




            if data2=="ichimokued":            
                with open('/home/indbit/project/mysite/static/ichitd.txt') as fs23:
                    coins = set(fs23.read().split())


        

        if data=="ichimokue2":
            if data2=="ichimokue5":
                with open('/home/indbit/project/mysite/static/ichint55.txt') as fs24:
                    coins = set(fs24.read().split())
            
            if data2=="ichimokue15":
                with open('/home/indbit/project/mysite/static/ichint15.txt') as fs25:
                    coins = set(fs25.read().split())

            if data2=="ichimokue30":            
                with open('/home/indbit/project/mysite/static/ichint30.txt') as fs26:
                    coins = set(fs26.read().split())

            if data2=="ichimokue1":            
                with open('/home/indbit/project/mysite/static/ichint1.txt') as fs27:
                    coins = set(fs27.read().split())
            
            
            if data2=="ichimokue4":            
                with open('/home/indbit/project/mysite/static/ichint4.txt') as fs28:
                    coins = set(fs28.read().split())


            if data2=="ichimokued":            
                with open('/home/indbit/project/mysite/static/ichintd.txt') as fs29:
                    coins = set(fs29.read().split())

        

        if data=="ichimokue3":
            if data2=="ichimokue5":
                with open('/home/indbit/project/mysite/static/ichiA5.txt') as fs30:
                    coins = set(fs30.read().split())
            
            if data2=="ichimokue15":
                with open('/home/indbit/project/mysite/static/ichiA15.txt') as fs31:
                    coins = set(fs31.read().split())

            if data2=="ichimokue30":            
                with open('/home/indbit/project/mysite/static/ichiA30.txt') as fs32:
                    coins = set(fs32.read().split())

            if data2=="ichimokue1":            
                with open('/home/indbit/project/mysite/static/ichiA1.txt') as fs33:
                    coins = set(fs33.read().split())
            
            if data2=="ichimokue4":            
                with open('/home/indbit/project/mysite/static/ichiA4.txt') as fs34:
                    coins = set(fs34.read().split())


            if data2=="ichimokued":            
                with open('/home/indbit/project/mysite/static/ichiAd.txt') as fs35:
                    coins = set(fs35.read().split())


        
        if data=="ichimokue4":
            if data2=="ichimokue5":
                with open('/home/indbit/project/mysite/static/ichiB5.txt') as fs36:

                    coins = set(fs36.read().split())
            
            if data2=="ichimokue15":
                with open('/home/indbit/project/mysite/static/ichiB15.txt') as fs37:
                    coins = set(fs37.read().split())

            if data2=="ichimokue30":            
                with open('/home/indbit/project/mysite/static/ichiB30.txt') as fs38:
                    coins = set(fs38.read().split())


            if data2=="ichimokue1":            
                with open('/home/indbit/project/mysite/static/ichiB1.txt') as fs39:
                    coins = set(fs39.read().split())
            
            
            if data2=="ichimokue4":

                with open('/home/indbit/project/mysite/static/ichiB4.txt') as fs40:


                    coins = set(fs40.read().split())

     

            if data2=="ichimokued":            
                with open('/home/indbit/project/mysite/static/ichiBd.txt') as fs41:
                    coins = set(fs41.read().split())
        

        if data=="ichimokue6":

            if data2=="ichimokue5":

                with open('/home/indbit/project/mysite/static/ichiB5.txt') as fs42:

                    coins = set(fs42.read().split())
            
            if data2=="ichimokue15":
                with open('/home/indbit/project/mysite/static/ichiB15.txt') as fs43:
                    coins = set(fs43.read().split())

            if data2=="ichimokue30":            
                with open('/home/indbit/project/mysite/static/ichiB30.txt') as fs44:
                    coins = set(fs44.read().split())

            if data2=="ichimokue1":            
                with open('/home/indbit/project/mysite/static/ichiB1.txt') as fs45:
                    coins = set(fs45.read().split())


            if data2=="ichimokue4":

                with open('/home/indbit/project/mysite/static/ichiB4.txt') as fs46:
                    
                    coins = set(fs46.read().split())


            if data2=="ichimokued":            
                with open('/home/indbit/project/mysite/static/ichiBd.txt') as fs47:
                    coins = set(fs47.read().split())


        return render_template('index.html',x=coins)

@main.route("/bolinger")
def index6():
    data=request.args.get("bolinger")
    data2=request.args.get("bolinger2")
    if data=="bbup":
            if data2=="bb5":
                with open('/home/indbit/project/mysite/static/bbandup5.txt') as fs48:
                    coins = set(fs48.read().split())
            
    
            if data2=="bb15":
                with open('/home/indbit/project/mysite/static/bbandup15.txt') as fs49:
                    coins = set(fs49.read().split())
            
            

            if data2=="bb30":
                with open('/home/indbit/project/mysite/static/bbandup30.txt') as fs50:
                    coins = set(fs50.read().split())
            
            
            if data2=="bb1":
                with open('/home/indbit/project/mysite/static/bbandup1.txt') as fs51:
                    coins = set(fs51.read().split())
            
            if data2=="bb4":
                with open('/home/indbit/project/mysite/static/bbandup4.txt') as fs52:
                    coins = set(fs52.read().split())


            if data2=="bbd":
                with open('/home/indbit/project/mysite/static/bbandupd.txt') as fs53:
                    coins = set(fs53.read().split())




    if data=="bbdown":
            if data2=="bb5":
                with open('/home/indbit/project/mysite/static/bbanddown5.txt') as fs54:
                    coins = set(fs54.read().split())
            

            if data2=="bb15":

                with open('/home/indbit/project/mysite/static/bbanddown15.txt') as fs55:
                    coins = set(fs55.read().split())
            
            if data2=="bb30":
                with open('/home/indbit/project/mysite/static/bbanddown30.txt') as fs56:
                    coins = set(fs56.read().split())
            
            if data2=="bb1":
                with open('/home/indbit/project/mysite/static/bbanddown1.txt') as fs57:
                    coins = set(fs57.read().split())
            
            if data2=="bb4":
                with open('/home/indbit/project/mysite/static/bbanddown4.txt') as fs58:
                    coins = set(fs58.read().split())
            
            if data2=="bbd":
                with open('/home/indbit/project/mysite/static/bbanddownd.txt') as fs59:
                    coins = set(fs59.read().split())
    return render_template('index.html',x=coins)



@main.route("/cci")
def index7():
    data=request.args.get("cci1")
    data2=request.args.get("cci2")
    if data=="cci100":
            if data2=="cci5":
                with open('/home/indbit/project/mysite/static/cci1005.txt') as fs60:
                    coins = set(fs60.read().split())
            
    
            if data2=="cci15":
                with open('/home/indbit/project/mysite/static/cci10015.txt') as fs61:
                    coins = set(fs61.read().split())
            
            

            if data2=="cci30":
                with open('/home/indbit/project/mysite/static/cci10030.txt') as fs62:
                    coins = set(fs62.read().split())
            
            
            if data2=="cci1":
                with open('/home/indbit/project/mysite/static/cci1001.txt') as fs63:
                    coins = set(fs63.read().split())
            
            if data2=="cci4":
                with open('/home/indbit/project/mysite/static/cci1004.txt') as fs64:
                    coins = set(fs64.read().split())


            if data2=="ccid":
                with open('/home/indbit/project/mysite/static/cci100d.txt') as fs65:
                    coins = set(fs65.read().split())




    if data=="cci-100":
            if data2=="cci5":
                with open('/home/indbit/project/mysite/static/cci-1005.txt') as fs66:
                    coins = set(fs66.read().split())
            

            if data2=="cci15":

                with open('/home/indbit/project/mysite/static/cci-10015.txt') as fs67:
                    coins = set(fs67.read().split())
            
            if data2=="cci30":
                with open('/home/indbit/project/mysite/static/cci-10030.txt') as fs68:
                    coins = set(fs68.read().split())
            
            if data2=="cci1":
                with open('/home/indbit/project/mysite/static/cci-1001.txt') as fs69:
                    coins = set(fs69.read().split())
            
            if data2=="cci4":
                with open('/home/indbit/project/mysite/static/cci-1004.txt') as fs70:
                    coins = set(fs70.read().split())
            
            if data2=="ccid":
                with open('/home/indbit/project/mysite/static/cci-100d.txt') as fs71:
                    coins = set(fs71.read().split())
    return render_template('index.html',x=coins)


@main.route("/adx")
def index8():
    data=request.args.get("adx")
    if data=="adx5":
        with open('/home/indbit/project/mysite/static/adxi5.txt') as fs72:
            coins = set(fs72.read().split())
    
    if data=="adx15":
        with open('/home/indbit/project/mysite/static/adxi15.txt') as fs73:
            coins = set(fs73.read().split())


    if data=="adx30":
        with open('/home/indbit/project/mysite/static/adxi30.txt') as fs74:
            coins = set(fs74.read().split())
    

    if data=="adx1":
        with open('/home/indbit/project/mysite/static/adxi1.txt') as fs75:
            coins = set(fs75.read().split())
    
    
    if data=="adx4":

        with open('/home/indbit/project/mysite/static/adxi4.txt') as fs76:      
            coins = set(fs76.read().split())

    if data=="adxd":
        with open('/home/indbit/project/mysite/static/adxid.txt') as fs77:

            
            coins = set(fs77.read().split())
    
    return render_template('index.html',x=coins)