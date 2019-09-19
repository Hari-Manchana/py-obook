#import ob_tradable
from ob_tradable import Tradable 
import time

class Side():
    def __init__(self,side_item,side):
        self.side_item=side_item
        self.side=side

    def add_tradable(self,tradable):
        if(self.side=="BUY"):
            temp_si,prev_si = self.side_item.find_descending_position(tradable)
        else:
            temp_si,prev_si = self.side_item.find_ascending_position(tradable)

        if(temp_si is not None and temp_si.is_equal(tradable)):
            print("add to existing")
            
        else:
            if(prev_si is not None):
                #adding in the middle
                prev_si.next_side_item=SideItem(tradable,temp_si)
            else:
                #adding at the front 
                new_side_item=SideItem(tradable)
                new_side_item.next_side_item=temp_si
                self.side_item=new_side_item

    def print(self):
        print("{} Side:".format(self.side))
        self.side_item.print()
        

class SideItem():
    def __init__(self,tradable,next_item=None):
        self.item_tradable=tradable
        self.next_side_item=next_item

    def find_descending_position(self,tradable):
        temp_item=self
        prev_item=None
        while(temp_item is not None and temp_item.is_greater(tradable)):
            prev_item=temp_item
            temp_item=temp_item.next_side_item
        return temp_item,prev_item

    def find_ascending_position(self,tradable):
        temp_item=self
        prev_item=None
        while(temp_item is not None and temp_item.is_lower(tradable)):
            prev_item=temp_item
            temp_item=temp_item.next_side_item
        return temp_item,prev_item
    
    def is_greater(self,tradable):
        return self.item_tradable.is_greater(tradable)

    def is_lower(self,tradable):
        return self.item_tradable.is_lower(tradable)
    
    def is_equal(self,tradable):
        return self.item_tradable.is_equal(tradable)
    
    def print(self):
        si=self
        while(si is not None):
            si.item_tradable.print()
            si=si.next_side_item
        

sitem=SideItem(Tradable(1.25,100,time.time_ns()))
buy_side=Side(sitem,"BUY")
buy_side.add_tradable(Tradable(1.00,200,time.time_ns()))
buy_side.add_tradable(Tradable(1.50,200,time.time_ns()))
buy_side.add_tradable(Tradable(1.30,200,time.time_ns()))
buy_side.print()

sitem=SideItem(Tradable(1.25,100,time.time_ns()))
sell_side=Side(sitem,"SELL")
sell_side.add_tradable(Tradable(1.00,200,time.time_ns()))
sell_side.add_tradable(Tradable(1.50,200,time.time_ns()))
sell_side.add_tradable(Tradable(1.30,200,time.time_ns()))
sell_side.print()

