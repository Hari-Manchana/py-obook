#import obk_side_v1

from obk_side_v1 import Side, SideItem
from ob_tradable import Tradable
import time
        

class OrderBook():
    def __init__(self,buy_side,sell_side):
            self.buy_side=buy_side
            self.sell_side=sell_side

    def remove(self,tradable):
        if(tradable.side=="BUY"):
            self.buy_side.remove(tradable)
        else:
            self.sell_side.remove(tradable)
        
    def add(self,tradable):
        if(tradable.side=="BUY"):
            self.buy_side.add(tradable)
        else:
            self.sell_side.add(tradable)
            
    def print(self):
        self.buy_side.print()
        self.sell_side.print()
            
if(__name__=="__main__"):
   
    buy_side=Side("BUY")
    sell_side=Side("SELL")

    obk=OrderBook(buy_side,sell_side)
    t100=Tradable(1.00,200,time.time_ns())

    t1=Tradable(1.50,400,time.time_ns(),"SELL")
    obk.add(t1)
    
    obk.add(t100)
    obk.print()
    obk.remove(t100)
    obk.remove(t1)
    obk.print()

    '''
    t0=Tradable(1.00,200,time.time_ns())
    obk.add(t0)
    time.sleep(1)
    t=Tradable(1.25,400,time.time_ns())
    obk.add(t)
    time.sleep(1)
    obk.add(Tradable(1.00,800,time.time_ns()))
    obk.add(Tradable(1.50,200,time.time_ns()))
    obk.add(Tradable(1.30,200,time.time_ns()))
    t175=Tradable(1.75,200,time.time_ns())
    obk.add(t175)
    

    obk.add(Tradable(1.00,200,time.time_ns(),"SELL"))
    obk.add(Tradable(1.50,200,time.time_ns(),"SELL"))
    obk.add(Tradable(1.30,200,time.time_ns(),"SELL"))
    time.sleep(1)
    t1=Tradable(1.50,400,time.time_ns(),"SELL")
    obk.add(t1)
    obk.add(Tradable(1.00,600,time.time_ns(),"SELL"))
    obk.add(Tradable(0.80,600,time.time_ns(),"SELL"))
    
    obk.print()
    obk.remove(t175)
    obk.remove(t)
    obk.remove(t1)
    obk.remove(t0)
    obk.print()
    '''
    
