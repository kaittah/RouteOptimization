from datetime import datetime, timezone, timedelta
import random

from time_windows import fixed_time_windows, delivery_times, est_tz

class Stop:
    def __init__(self, coordinates, time_of_order):
        self.coordinates = coordinates
        self.time_of_order = time_of_order  #units: s since epoch
    
    def get_delivery_window(self, **kwargs):
        '''
        Returns time window in which delivery should be made
        Units are in s since epoch, based on all deliveries being 
        made during 12-1pm EDT on October 1, 2020
        '''
        for key, value in kwargs.items():

            if key == 'case':
                if value in fixed_time_windows.keys():  #'A', 'B', 'C' are accepted
                    scrambled_windows = fixed_time_windows[value][:]
                    random.shuffle(scrambled_windows)
                    for window in scrambled_windows:
                        if window[0] <= self.time_of_order and window[1]>= self.time_of_order:
                            return window
                raise ValueError(f"No appropriate time window found in case {value}")

            elif key == 'buffer':
                time_dif = 60*value 
                start_time = int(self.time_of_order) - time_dif//2
                end_time = start_time + time_dif
                if end_time > delivery_times['max']: #make all delivery windows follow the same time restrictions
                    end_time = delivery_times['max']
                    start_dt = end_time - time_dif
                elif start_time < delivery_times['min']:
                    start_time = delivery_times['min']
                    end_time = start_time + time_dif
                return [start_time, end_time]

            else:
                raise ValueError(f'No keyword argument named {key}')
