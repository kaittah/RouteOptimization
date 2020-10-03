# RouteOptimization
A case study on optimizing on-demand restaurant delivery

![Gif of route plots](https://github.com/kaittah/RouteOptimization/blob/main/images/route0.gif?raw=true)

Delivery services are on the rise, prompting the question of what consumers and delivery providers can do to reduce their impact on the environment.

The most eco-friendly method to buy and sell would have the consumer walk or bike over to the store to purchase goods. However, weather, distance, lack of sidewalks make this impractical in many situations, so people drive. In the case of restaurant delivery, usually the customer drives to the restaurant and back home. Meal delivery services improve upon this by reducing the number of round trips and optimizing routes to minimize distance and gas emissions.

This simulation creates fake restaurant orders for a set number of pretend customers in Boston, MA. The addresses of the customers and restaurants are randomly selected from separate sets of geographical coordinates. The supposed time at which the customer would want their food is randomly selected from a normal distribution with a mean at 12:05pm and a standard deviation of 20 minutes. Times were limited to between 12:00 and 1:00 pm. 

![Gif of route plots](https://github.com/kaittah/RouteOptimization/blob/main/images/randomorders.png?raw=true)

The orders were strung together into a route optimized using [VROOM](http://vroom-project.org/). Several cases were explored to compare which would lead to the most environmentally-friendly meal delivery.

In one scenario, customers place an order for food to be delivered in a fixed time window. In case 'A', all orders share the time window 12pm - 1pm. Case 'B' splits it into 2 shorter time windows, 12 - 12:30pm and 12:30-1pm. Case 'C' has 3 time windows (12-12:30, 12:15-12:45, and 12:30-1) the are of the same length as those of 'B', the difference being that if a customer wants their food at 12:16pm, they can either select the 12-12:30 or 12:15-12:45 window. 

In another scenario, customers place orders for food to be delivered at a random time, but the allowable delivery window is either +/5, 10, or 15 mintues (case '10', '20', and '30', respectively) around that designated time. Deliveries were still limited to between 12-1pm.

Case 'A' should lead to the most efficient routes because, with the largest time windows for deliveries to be made, the routing algorithm had the most flexibility to optimize. Cases '10' and '20' have the shortest time windows, leading to the least flexibility. Flexibility is important for efficiency in scheduling, as reflected in the results:

|   | A  |  10 | 20 | 30 |
|---|---|---|---|---|
|Avg. Cost |2630.2|3511.4| 3179.2| 2965.2|
|Avg. Distance (m)|18905.2|25410.8|22794.0|21067.1|

Cases 'B' and 'C', and '30' each have 30 minute long delivery windows for orders. To understand the difference, consider 2 neighbors who place orders at the same restaurant, but one neighbor wants food at 12:20 while the other wants food at 12:40. In Case 'B', the food can be delivered to the neighbors at the same time only if the neighbors receive food at 12:30pm. In cases 'C' and '30', due to the overlapping time windows, there is a wider range of times available for the food to be delivered in the same stop, giving the algorithm more flexibility. In the end, cases 'B', 'C', and '30' had similar results. The frequency at which situations where having overlapping windows adds benefit may be low.

|   | B |  C | 30 |
|---|---|---|---|
|Avg. Cost |2983.4|2982.8|2965.2|
|Avg. Distance (m)|21240.8|21383.5|21067.1|

A summary of average distances for all routes is shown below.
![Box plots](https://github.com/kaittah/RouteOptimization/blob/main/images/distancesboxplot.png?raw=true)

To obtain these averages, random order times, customer locations, and restaurant locations were generated 20 times. Then, the allowable time windows were derived for each of the cases and the routes were optimized and plots were made (some of which are below). Note that all the pickup and dropoff locations are the same, the only difference is that the times that food is delivered to each stop may vary in each situation.

![Image of route plots](https://github.com/kaittah/RouteOptimization/blob/main/images/trial0plots.png?raw=true)

This is a simplified study of a problem faced by delivery services. It proved that meal delivery services can be more efficient than customers driving to pick up food at a restaurant themselves, and that customers' adding flexibility to their delivery time choice will increase efficiency.










