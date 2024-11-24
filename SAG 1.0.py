import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
print('Enter login id and password')
loginid=str(input('ENTER ID--->'))
password=input('ENTER PASSWORD--->')


if loginid=='shresth' and password=='shresth@singh':
    import datetime
    currentTime=datetime.datetime.now()
    currentTime.hour
    if currentTime.hour<12:
        print('Good morning',loginid)
        print('I AM S.A.G,YOUR PERSONAL ASSISTANT')
    elif currentTime.hour<24 and currentTime.hour<17:
        print('Good Afternoon',loginid)
        print('I AM S.A.G,YOUR PERSONAL ASSISTANT')
    else:
        print('Good Evening',loginid)
        print('I AM S.A.G,YOUR PERSONAL ASSISTANT')
    for i in range(30):
        bot=str(input('HOW MAY I HELP YOU SIR:'))
        if bot=='open calculator':
            print('opening caluclator')
            num1=float(input('enter first number'))
            num2=float(input('enter second number'))
            o=input('enter operation')
            if o=='+':
                print('the result is:'\
,num1,o,num2,'=',num1+num2)
            elif o=='-':
              print('the result is:'\
,num2,o,num1,'=',num2-num1)
            elif o=='*':
               print('the result is:'\
,num1,o,num2,'=',num1*num2)
            elif o=='/':
              print('the result is:'\
,num1,o,num2,'=',num1/num2)
            else:
              print('invalid operation!!')
        elif bot=='pen down a note':
            nm=str(input('enter name of the person you want to wish:'))
            oca=str(input('enter occasion:'))
            if oca=='birthday':
              print('dear',nm,',')
              print('We’ve made so many wonderful memories togethers.\
Cheers to many more. Happy birthday!')
            elif oca=='diwali':
              print('Dear',nm,',')
              print('Wish you a very Happy Diwali!\
May the festival of lights be the harbinger of joy and prosperity.')
            elif oca=='Holi':
              print('Dear',nm,',')
              print('Wishing you a very colorful and joyous Holi! On the happy occasion of Holi,\
may your life always be filled with the colors of joy and happiness. ')
            elif oca=='Durga puja':
              print('Dear',nm,',')
              print(' wish you peace, happiness, and joy on this happy occasion of Durga Puja!\
I wish the blessing of Maa Durga fills your life with happiness and prosperity.')
            elif oca=='Chhath puja':
              print('dear',nm,',')
              print('I pray that each and every day of your life is blessed by Chhathi Mata and Lord Sun.')
            elif oca=='christmas':
              print('Dear',nm,',')
              print('May this season be full of light and laughter for you and your family.')
        elif bot=='play music':
            print('Opening your playlist')
            df=pd.read_csv('D:\playlist.csv',sep=',')
            print(df)
            ch=str(input('Which song do you want me to play:-->'))
            if ch=='HYMN FOR THE WEEKEND':
                print('playing',ch,'!!')
            elif ch=='THE NIGHTS':
                print('playing',ch,'!!')
            elif ch=='HEAT WAVES':
                print('playing',ch,'!!')
            elif ch=='I WANT IT THAT WAY':
                print('playing',ch,'!!')
            else:
                print('this song is not added to your playlsit')
                s=str(input('Do you want this song to be in your playlist?'))
                if s=='yes':
                    print('OK song',ch,' has been added to your playlist!')
                    print('playing',ch,'!!')
        elif bot=='open my phonebook':
            print('opening your phonebook')
            df=pd.read_csv('D:\phbook.csv',sep=',')
            print(df)
        elif bot=='open timetable':
            print('opening timetable')
            df=pd.read_csv('E:\\python exm\\TT.csv',sep=',')
            print(df)
        elif bot=='show air pollution level in India':
            print("Sure!!")
            df=pd.read_csv('D:\\state air pollution.csv',sep=',')
            print(df)
            pl.figure(figsize=(15,9))
            pl.plot(df['STATES'],df['AQI-US'],'c')
            pl.plot(df['STATES'],df['PM2.5'],'r')
            pl.show()   
        elif bot=='set alarm':
            tm=str(input('Enter time-->'))
            lb=str(input('Enter Label-->'))
            print('Alarm set for',tm,'!!')
        elif bot=="literacy rate in states of India":
            print('Literacy rate of few states of India as follows:')
            pl.figure(figsize=(15,5))
            x=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Goa','Gujarat','Haryana','Kerala']
            y=[66,67,73,70,87,79,76,74]
            pl.bar(x,y,color='red')
            pl.show()