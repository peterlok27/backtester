import pandas as pd 

class Event(object): 
    def __init__(self): 
        pass 

class MarketEvent(Event):
    """Handles new market information that comes in """
    def __init__(self): 
        self.type = "MARKET"

class SignalEvent(Event):
    """ Handles what needs to be done. Emitted from the strategy object""" 
    def __init__(self,symbol,datetime,signal_type):
        self.type = "SIGNAL"
        self.symbol = symbol
        self.datetime = datetime
        self.signal  = signal_type

class OrderEvent(Event):
    """ Handles the order that needs to be placed in the execution system""" 
    """ order_type is whether the order is market or limit, direction is whether buy or sell"""
    def __init__(self, symbol, order_type, quantity, direction):
        self.type = "ORDER"
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction

    def print_order(self):
        """
        Outputs the values within the Order.
        """
        print "Order: Symbol=%s, Type=%s, Quantity=%s, Direction=%s" % \
            (self.symbol, self.order_type, self.quantity, self.direction)

class 

