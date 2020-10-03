from shipment_step import Shipment_step

class Shipment:
    def __init__(self, pickup, dropoff, priority=0, amount=[1]):
        self.pickup = pickup
        self.delivery = dropoff
        self.priority = priority
        self.amount = amount
    
    def get_dictionary(self):
        return {'pickup':self.pickup.get_dictionary(), 
                'delivery':self.delivery.get_dictionary(), 
                'amount':self.amount, 
                'priority':self.priority}