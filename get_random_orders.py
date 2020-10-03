import csv
from datetime import datetime, timezone, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import random

from time_windows import delivery_times, est_tz


def get_random_orders():

    with open('restaurant_coordinates.csv', 'r') as rfile, open('residential_coordinates.csv', 'r') as cfile:
        restaurant_reader = csv.reader(rfile, delimiter = ',')
        customer_reader = csv.reader(cfile, delimiter = ',')
        N_R = len(list(restaurant_reader))
        N_C = len(list(customer_reader))
        rfile.seek(0)
        cfile.seek(0)
        r_line = random.randrange(N_R)
        c_line = random.randrange(N_C)
        for _ in range(r_line):
            next(restaurant_reader)
        for _ in range(c_line):
            next(customer_reader)
        restaurant_loc = next(restaurant_reader)
        customer_loc = next(customer_reader)
    
    time_window = delivery_times['max'] - delivery_times['min']
    time_buffer = 60*5

    order_time_array = range(delivery_times['min'] + time_buffer, delivery_times['max']-time_buffer, (time_window-2*time_buffer)//5) 
    weight_array = [.7, .2, .08, .05, .02]
    order_time = random.choices(order_time_array, weights = weight_array)[0] + random.randrange(-time_buffer, time_buffer)
    time_of_stop = datetime.fromtimestamp(int(order_time), est_tz)
    time_formatted = time_of_stop.strftime('%I:%M')

    restaurant_coords = [float(i) for i in restaurant_loc]
    customer_coords = [float(i) for i in customer_loc]
    restaurant_coords.reverse() #put in longitude, latitude form
    customer_coords.reverse()

    return restaurant_coords, customer_coords, order_time, time_formatted

def graph_order_times(N):
    order_times = [get_random_orders()[2] for i in range(N)]
    orderplot = sns.displot(data=order_times, kde=True, rug =True)

    plt.show()


if __name__ == "__main__":
    graph_order_times(500)