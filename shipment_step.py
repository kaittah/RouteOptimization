class Shipment_step:
    def __init__(self, id, location, minutes, time_window):
        self.id = id
        self.location = location
        self.service = 60*minutes
        self.time_windows = [time_window]
    
    def get_dictionary(self):
        return {'id': self.id, 
                'location': self.location, 
                'service': self.service, 
                'time_windows':self.time_windows}