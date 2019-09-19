#import ob_tradable
from ob_tradable import Tradable 
import time

class Side():
    def __init__(self,side="BUY",side_item=None):
        self.side_item=side_item
        self.side=side

    def remove(self,tradable):
        if(tradable is None):
            return

        self.side_item=self.side_item.remove(tradable)
            
    def add(self,tradable):
        if(self.side_item is None):
                self.side_item=SideItem(tradable)
                return
            
        if(self.side=="BUY"):
            temp_si,prev_si = self.side_item.find_descending_position(tradable)
        else:
            temp_si,prev_si = self.side_item.find_ascending_position(tradable)

        if(temp_si is not None and temp_si.is_equal(tradable)):
            #print("add to existing")
            temp_si.add_to_existing(tradable)
        else:
            if(prev_si is not None):
                #adding in the middle
                #print("adding in the middle:{}".format(tradable.price))
                prev_si.next_side_item=SideItem(tradable,temp_si)
            else:
                #adding at the front 
                new_side_item=SideItem(tradable)
                new_side_item.next_side_item=temp_si
                self.side_item=new_side_item

    def print(self):
        print("{} Side:".format(self.side))
        if(self.side_item is not None):
            self.side_item.print()
        

class SideItemTradable():
    def __init__(self,tradable):
        self.item = tradable
        self.next = None
        #print("Creating a new SIT for {}:".format(self.item.price))

    def print(self):
        print("Tradales at Price:{} are:".format(self.item.price))
        sit=self
        while(sit is not None):
            sit.item.print()
            sit=sit.next

    def remove(self,tradable):
        sit=self
        psit=None

        while(sit is not None and not sit.item.equals(tradable)):
            psit=sit
            sit=sit.next

        if(sit is None and psit==self):
            #only one item
            print("SideItemTradable::remove: Only Item Removal")
            return None
        elif(sit is None):
            #no match
            return self
        elif(sit is not None and psit is None):
            #first item
            self=sit.next
            return self
        elif(sit is not None and psit is not None):
            psit.next=sit.next
            return self 
                
                
                
        
            
    def add_tradable(self,tradable):
        sit=self
        psit=None 
        #print("add_tradable::self={} and tradable={}".format(self.item,tradable))
        while(sit is not None and (sit.item.recieve_time()<=tradable.recieve_time())):
            #print("add_tradable::recieve_times:self{} and tradable={}".format(sit.item.recieve_time(),tradable.recieve_time()))
            psit=sit
            sit=sit.next

        nsit=SideItemTradable(tradable)
        if(psit is None):
            nsit.next=sit
            return nsit
        else:
            psit.next=nsit
            return self
        
        
class SideItem():
    def __init__(self,tradable=None,next_item=None):
        #self.item_tradable=tradable
        self.price_level=tradable.price
        self.tradable_item=SideItemTradable(tradable)
        self.next_side_item=next_item
        
    def remove(self,tradable):
        temp_item=self
        prev_item=None
        while(temp_item is not None and not temp_item.is_equal(tradable)):
            prev_item=temp_item
            temp_item=temp_item.next_side_item

        if(temp_item is not None and prev_item==None):
            #first item removal
            #print("SideItem::remove: Removal At the Begining")
            self.tradable_item=self.tradable_item.remove(tradable)
            if(self.tradable_item is None):
                 return temp_item.next_side_item
        elif(temp_item is None and prev_item!=self):
            #last item removal
            #print("SideItem::remove: Removal At the End")
            self.tradable_item=self.tradable_item.remove(tradable)
            if(self.tradable_item is None):
                prev_item.next_side_item=None
        elif(temp_item is not None and prev_item!=self):
            #add in the middle
            #print("SideItem::remove: Removal In the Middle")
            temp_item.tradable_item=temp_item.tradable_item.remove(tradable)
            if(temp_item.tradable_item is None):
                #print("SideItem::remove: REMOVED the Middle")
                prev_item.next_side_item=temp_item.next_side_item
        return self
    
    def add_to_existing(self,tradable):
        if(self.price_level == tradable.price):
            #print("add_to_existing::tradable_item={}".format(self.tradable_item))
            self.tradable_item=self.tradable_item.add_tradable(tradable)
            
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
        return self.price_level>tradable.price

    def is_lower(self,tradable):
        return self.price_level<tradable.price
    
    def is_equal(self,tradable):
        return self.price_level==tradable.price
    
    def print(self):
        si=self
        while(si is not None):
            #si.item_tradable.print()
            if(si.tradable_item is not None):
                si.tradable_item.print()
            else:
                print("SideItem::print: Tradable is NULL for price={}".format(si.price_level))
            si=si.next_side_item
        
if(__name__=="__main__"):
    sitem=SideItem(Tradable(1.25,100,time.time_ns()))
    buy_side=Side(sitem,"BUY")
    time.sleep(1)
    buy_side.add(Tradable(1.00,200,time.time_ns()))
    time.sleep(1)
    buy_side.add(Tradable(1.25,400,time.time_ns()))
    time.sleep(1)
    buy_side.add(Tradable(1.00,800,time.time_ns()))
    buy_side.add(Tradable(1.50,200,time.time_ns()))
    buy_side.add(Tradable(1.30,200,time.time_ns()))
    buy_side.print()


    sitem=SideItem(Tradable(1.25,100,time.time_ns()))
    sell_side=Side(sitem,"SELL")
    sell_side.add(Tradable(1.00,200,time.time_ns()))
    sell_side.add(Tradable(1.50,200,time.time_ns()))
    sell_side.add(Tradable(1.30,200,time.time_ns()))
    time.sleep(1)
    sell_side.add(Tradable(1.50,400,time.time_ns()))
    sell_side.print()


