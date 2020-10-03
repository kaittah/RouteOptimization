import matplotlib.pyplot as plt
import matplotlib.colors as clrs
from routingpy import ORS

from shipment import Shipment
from shipment_step import Shipment_step

client = ORS(api_key=API_KEY)

def find_unopt_distance(shipment_list, repetition):
    plot_file = f'route_plots/plot_unopt_{repetition}.svg'
    fig, ax = plt.subplots()
    route_color = 'darkcyan'
    xmin = None
    ymin = None
    distances = []
    for shipment in shipment_list:
        pickup_loc = shipment.pickup.location
        dropoff_loc = shipment.delivery.location
        if xmin == None or ymin == None:
            xmin = pickup_loc[0]
            ymin = pickup_loc[1]
            xmax = xmin
            ymax = ymin
        xmin = min(xmin, pickup_loc[0], dropoff_loc[0])
        ymin = min(xmin, pickup_loc[1], pickup_loc[1])
        xmax = max(xmin, pickup_loc[0], dropoff_loc[0])
        ymax = max(xmin, pickup_loc[1], pickup_loc[1])
        lons = [dropoff_loc[0], pickup_loc[0], dropoff_loc[0]]
        lats = [dropoff_loc[1], pickup_loc[1], dropoff_loc[1]]
        ax.plot(lons, lats, color=route_color)
        dirs = client.directions(locations=[dropoff_loc, pickup_loc, dropoff_loc], profile = 'driving-car')
        ship_distance = dirs.distance
        distances.append(ship_distance)


    title = f"Solution without meal delivery, total distance of {sum(distances)} m"

    ax.set_title(title)
    ax.set_aspect('equal')

    print("Plotting file " + plot_file)
    
    plt.savefig(plot_file, bbox_inches='tight')
    plt.close() 
            
    print(f"List of distances for repetition {repetition}: ")
    print(distances)
    return sum(distances)



