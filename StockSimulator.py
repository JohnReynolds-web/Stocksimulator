import random
from time import sleep
joblist={'Fastfood worker':10,
         'Office Drone':15,
         'Beggar':5,
         'Manager':20}
stocks={"Blackwell Ventures":120,
        "Vantage Dynamics":30,
        "Crestline Industries":130,
        "Nexar Solutions":25,
        "Ironbridge Capital":80,
        "Aurum Technologies":250,
        "Meridian Logistics":15,
        "Stonehaven Energy":100,
        "Calibra Systems":90,
        "Halcyon Pharmaceuticals":300,
        "Ironclad Manufacturing":35,
        "Solace Biotech":150,
        "Pinnacle Aerospace":935,
        "Redwood Financial":785,
        "Corvus Electronics":45,
        "Ashford Consumer Goods":120}
totalshares = {stock: 1000 for stock in stocks}
giglist={
    'Deliver groceries':3,
    'Walk dogs':2,
    'Fix a bicycle':4,
    'Help someone move furniture':6,
    'Babysit':5,
    'Mow a lawn':3,
    'Wash cars':4,
    'Paint a fence':5,
    'Fix a computer':7,
    'Cater a small event':8}
def gigs():
    todaygigs=random.sample(list(giglist.keys()), 3)
    return todaygigs
class Player:
    def __init__(self):
        self.joblevels={'Beggar':0,
                        'Fastfood worker':0,
                        'Office Drone':0,
                        'Manager':0}
        self.joborder=['Beggar', 'Fastfood worker', 'Office Drone', 'Manager']
        self.job='unemployed'
        self.daysplayed=0
        self.importantstocksowned={}
        self.money=50
        self.companiesowned=[]
        self.stocksowned={"Blackwell Ventures":0,
        "Vantage Dynamics":0,
        "Crestline Industries":0,
        "Nexar Solutions":0,
        "Ironbridge Capital":0,
        "Aurum Technologies":0,
        "Meridian Logistics":0,
        "Stonehaven Energy":0,
        "Calibra Systems":0,
        "Halcyon Pharmaceuticals":0,
        "Ironclad Manufacturing":0,
        "Solace Biotech":0,
        "Pinnacle Aerospace":0,
        "Redwood Financial":0,
        "Corvus Electronics":0,
        "Ashford Consumer Goods":0}
    def playerjob(self):
        if self.job!='unemployed':
            if self.joblevels[self.job]==0:
                self.money+=joblist[self.job]
                self.joblevels[self.job]+=1
            else: 
                self.money+=joblist[self.job]*self.joblevels[self.job]
                if self.joblevels[self.job]<5:
                    self.joblevels[self.job]+=1
                else:
                    return
        else:
            return
    def importantstocksownedf(self):
        self.importantstocksowned={}
        for stock in self.stocksowned:
            if self.stocksowned[stock]>=1:
                self.importantstocksowned[stock] = self.stocksowned[stock]
    def totalstockvalue(self):
        self.tstockvalue=0
        for stock in self.stocksowned:
            self.tstockvalue+=self.stocksowned[stock]*stocks[stock]
        return self.tstockvalue
    def ownedcompanies(self):
        for stock in self.importantstocksowned:   
            if totalshares[stock]==0:
                if stock not in self.companiesowned:
                    self.companiesowned.append(stock)
                self.money+=self.stocksowned[stock]*stocks[stock]/75
            elif totalshares[stock]/2<=self.stocksowned[stock]:
                if stock not in self.companiesowned:
                    self.companiesowned.append(stock)
                self.money+=self.stocksowned[stock]*stocks[stock]/100
playerchoices=['s','c','j']
sellbuychoices=['b','s']
gigsjobslist=['g','j']
def stockchange():
    for stock in stocks:
        stockprice=stocks[stock]
        stockprice=round(random.randint(-10,15)/100*stockprice+stockprice)
        stocks[stock]=stockprice
        if stocks[stock]<10:
            stocks[stock]=10
p=Player()
def news():
    newsrandom=random.randint(1,10)
    randomstock=random.choice(list(stocks.keys()))
    if newsrandom==1:
        print(f'Lucky day! {randomstock} has gained 15% value!')
        stocks[randomstock]=round(stocks[randomstock]+stocks[randomstock]*0.15)
    elif newsrandom==2:
        print(f"Uh oh, due to a workplace accident {randomstock}'s price has fallen 15%")
        stocks[randomstock]=round(stocks[randomstock]-stocks[randomstock]*0.15)
        if stocks[randomstock]<10:
            stocks[randomstock]=10
    elif newsrandom==3:
        print(f"Due to resent expansion of {randomstock} the company has gained 30% of value!!")
        stocks[randomstock]=round(stocks[randomstock]+stocks[randomstock]*0.3)
    elif newsrandom==4:
        print(f'Recent reports say that {randomstock} has had many layoffs. This decreased their value by 30%!')
        stocks[randomstock]=round(stocks[randomstock]-stocks[randomstock]*0.3)
        if stocks[randomstock]<10:
            stocks[randomstock]=10
    else:
        print('The world is quiet. Nothing happend today!')
todaygigs=gigs()
while True:
    p.importantstocksownedf()
    p.totalstockvalue()
    if p.money<=0 and p.tstockvalue<=0:
                input('You have ran out of money, Unfortunate press any key to close the game.')
                quit()
    print(f'Your current job is {p.job}')
    print(f'You currently own the companies: {p.companiesowned}')
    print(f'Your current stocks are {p.importantstocksowned}')
    print(f'You currently have {p.money} cash')
    playerinput=input('Would you like to buy/sell stocks (S), continue to the next day (C) or look at current jobs, gigs (J)?: ').lower()
    if playerinput not in playerchoices:
        print('Thats not a valid option.')
        sleep(2)
        continue
    elif playerinput=='s':
        while True:
            sellbuyinput=input('Would you like to buy or sell stocks?(B/S) q to quit: ').lower()
            if sellbuyinput=='q':
                break
            if sellbuyinput not in sellbuychoices:
                print('Thats not an option.')
                sleep(2)
                continue
            elif sellbuyinput=='b':
                while True:
                    stockchoice=input(f'Here are the current stocks and their values what would you like to buy?: {stocks} (q) to go back: ').lower().title()
                    if stockchoice=='Q':
                        print('You left the stockmarket.')
                        sleep(1)
                        break
                    elif stockchoice not in stocks:
                        print('Thats not a valid option.')
                        sleep(2)
                        continue
                    stockamount=input(f'How many {stockchoice} would you like to purchase?: ')
                    try:
                        stockamount=int(stockamount)
                    except ValueError:
                        print('Please input a number..')
                        sleep(2)
                        continue
                    if p.money<stocks[stockchoice]*stockamount:
                        print('You dont have enough money.')
                        sleep(2)
                        continue
                    elif totalshares[stockchoice]-stockamount<0:
                        print("There aren't enough shares!")
                        sleep(2)
                        continue
                    else:
                        totalshares[stockchoice]-=stockamount
                        moneyspent=stocks[stockchoice]*stockamount
                        p.money-=moneyspent
                        p.stocksowned[stockchoice]+=stockamount
                        print(f'You purchased {stockamount} {stockchoice} for {moneyspent}')
            elif sellbuyinput=='s':
                while True:
                    print(f'You currently have {p.stocksowned}')
                    print(f'and {p.money} money.')
                    sellinput=input('What stocks do you want to sell? q to go back: ').lower().title()
                    if sellinput=='Q':
                        break
                    elif sellinput not in stocks:
                        print('Thats not a valid option.')
                        sleep(2)
                        continue
                    sellamount=input(f'How many of {sellinput} do you want to sell?')
                    try:
                        sellamount=int(sellamount)
                    except ValueError:
                        print('Thats not a valid amount.')
                        sleep(2)
                        continue
                    if p.stocksowned[sellinput]<sellamount:
                        print(f"You don't have that much {sellinput} in your inventory!")
                        sleep(2)
                        continue
                    else:
                        totalshares[sellinput]+=sellamount
                        moneygained=stocks[sellinput]*sellamount
                        p.money+=moneygained
                        p.stocksowned[sellinput]-=sellamount
                        print(f'You sold {sellamount} of {sellinput} for {moneygained}')
                        sleep(3)
                        break
    elif playerinput=='c':
        print('You went to sleep')
        sleep(3)
        print('You slept to the next day.')
        sleep(2)
        print('The stock prices have changed.')
        sleep(1)
        p.daysplayed+=1
        todaygigs=gigs()
        p.ownedcompanies()
        stockchange()
        news()
        p.playerjob()
        continue
    elif playerinput=='j':
        while True:
            gigsorjobs=input('Do you want to go to the gigs or the jobs (G/J) menu? (q to quit): ').lower()
            if gigsorjobs=='q':
                print('You went back.')
                sleep(2)
                break
            elif gigsorjobs not in gigsjobslist:
                print('Thats not an option.')
                sleep(2)
                continue
            elif gigsorjobs=='j':
                while True:
                    print('You can unlock news jobs after reaching lvl 5 in your current job. Beggar is the first job.')
                    print(f'Your current job levels are {p.joblevels}')
                    jobchoiceinput=input(f'Our current job options are {p.joborder} (press q to leave): ').lower().title()
                    if jobchoiceinput=='Q':
                        print('You left the job center')
                        sleep(2)
                        break
                    elif jobchoiceinput not in p.joborder:
                        print('Thats not a valid option.')
                    elif jobchoiceinput==p.job:
                        print('You already have that job!!')
                        sleep(2)
                        continue
                    elif jobchoiceinput=='Beggar':
                        p.job=jobchoiceinput
                    elif jobchoiceinput:
                        previousjob=p.joborder[p.joborder.index(jobchoiceinput)-1]
                        if p.joblevels[previousjob]!=5:
                            print(f"You don't have enough levels on {previousjob}")
                            sleep(2)
                        else:
                            p.job=jobchoiceinput
            elif gigsorjobs=='g':
                while True:
                    gigsinput=input(f'Todays gigs are {todaygigs} (q to quit): ').lower().title()
                    if gigsinput=='Q':
                        print('You went back')
                        sleep(2)
                        break
                    elif gigsinput not in todaygigs:
                        print('Thats not a valid option.')
                        sleep(2)
                        continue
                    else:
                        print('Youre doing the gig..')
                        for x in range(1,6):
                            print(x)
                            sleep(1)
                        print(f'You finished {gigsinput} and got paid {giglist[gigsinput]}')
                        p.money+=giglist[gigsinput]
                        todaygigs.remove(gigsinput)
                        sleep(2)
                        continue