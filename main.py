import json
import random

import pandas as pd

from call import call
from find_unopt_distance import find_unopt_distance
from get_random_orders import get_random_orders
from plot_routes import plot_routes
from shipment_step import Shipment_step
from shipment import Shipment
from stop import Stop
from time_windows import delivery_times
from vehicle import Vehicle

#set fixed parameters
number_of_orders = 21
min_time = delivery_times['min']
max_time = delivery_times['max']
pickup_time = [delivery_times['min'] - 30*60, delivery_times['max']]  
pickup_dur = 2 #time to pick up order
dropoff_dur = 2 #time to drop off order
num_drivers = 3 
car_capacity = 10 #max number of orders a car can hold
car_start = [-71.061033, 42.358157] #starting vehicle location

#set variables
buffers = [10,20,30]
cases = ['A','B','C']

#number of repetitions
N=10

#define vehicles and shipments for routes
vehicles = [Vehicle(j, car_capacity, car_start) for j in range(num_drivers)]

unopt_distances = []
for repetition in range(N):
    shipment_cases = {}
    
    for i in range(number_of_orders):
        #get random restaurant, delivery address, and time for order
        restaurant_loc, customer_loc, order_time, time_formatted = get_random_orders()

        shipment_id = 2*i
        pickup_step = Shipment_step(shipment_id, restaurant_loc, pickup_dur, pickup_time)
        dropoff = Stop(customer_loc, order_time)
        for buffer in buffers:
            dropoff_time_window = dropoff.get_delivery_window(buffer = buffer)
            dropoff_step = Shipment_step(shipment_id+1, dropoff.coordinates, dropoff_dur, dropoff_time_window)
            if shipment_cases.get(buffer, 0) == 0:
                shipment_cases[buffer] = []
            shipment_cases[buffer].append(Shipment(pickup_step, dropoff_step))
        for case in cases:
            dropoff_time_window = dropoff.get_delivery_window(case = case)
            dropoff_step = Shipment_step(shipment_id+1, dropoff.coordinates, dropoff_dur, dropoff_time_window)
            if shipment_cases.get(case, 0) == 0:
                shipment_cases[case] = []
            shipment_cases[case].append(Shipment(pickup_step, dropoff_step))
    
    unopt_shipment_list = shipment_cases['A'] #pick a list of shipments to calculate distances when unoptimized
    unopt_distance = find_unopt_distance(unopt_shipment_list, repetition)
    unopt_distances.append(unopt_distance)

    for case, shipment_list in shipment_cases.items():
        delivery_count, cost, distance = call(case, repetition, shipment_list, vehicles)
        plot_routes(case, repetition)

print(f"The unoptimized distance traveled would be {sum(unopt_distances)/len(unopt_distances)} on average.")
print(unopt_distances)





