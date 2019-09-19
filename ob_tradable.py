import time
import datetime 

class Tradable():
    def __init__(self,price,qty,recv_time,side="BUY"):
        self.price=price
        self.qty=qty
        self.recv_nano_time=recv_time
        self.side=side

    def get_recieve_datetime(self):
        secs = self.recv_nano_time / 1e9
        dt = datetime.datetime.fromtimestamp(secs)
        return dt.strftime('%Y-%m-%d %H:%M:%S.%f')

    def is_equal(self,tradable):
        return self.price == tradable.price

    def equals(self,tradable):
        if( self.price == tradable.price and self.qty==tradable.qty and self.recv_nano_time==tradable.recv_nano_time):
            return True

    def is_greater(self,tradable):
        return self.price > tradable.price
    
    def is_lower(self,tradable):
        return self.price < tradable.price

    def get_side():
        return self.side
    
    def print(self):
        print("Tradable Price={}, Qty={}, Recieved Time={}".format(self.price,self.qty,self.get_recieve_datetime()))

    def recieve_time(self):
        return self.recv_nano_time

if __name__=='__main__':
    tble=Tradable(1.25,100,time.time_ns())
    tble.display()
