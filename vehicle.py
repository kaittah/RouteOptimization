class Vehicle:
    def __init__(self, id_num, capacity, start_loc):
        self.id = id_num
        self.capacity = [capacity]
        self.start_loc = start_loc
        
    def get_dictionary(self):
        return {'capacity': self.capacity,
         'start': self.start_loc, 
         'id': self.id, 
         'profile':'driving-car'}