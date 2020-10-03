import json
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
from datetime import datetime, timezone, timedelta

from time_windows import est_tz

def plot_routes(case, repetition):
    solution_file = 'solution_files/case_' + str(case) + '_' + str(repetition) + '_output.json' 
    plot_file = f'route_plots/plot{case}_{repetition}.svg'
    color_list = ['mediumslateblue', 'darkcyan', 'indianred', 'forestgreen']
    fig, ax = plt.subplots()
    with open(solution_file, 'r') as sol_file:
        solution = json.load(sol_file)
    
    if(not solution.get('routes', None)):
        return
    
    xmin = solution['routes'][0]['steps'][0]['location'][0]
    xmax = xmin
    ymin = solution['routes'][0]['steps'][0]['location'][1]
    ymax = ymin

    for route in solution['routes']:
        lons = [step['location'][0] for step in route['steps']]
        lats = [step['location'][1] for step in route['steps']]
        route_color = color_list[route['vehicle'] % len(color_list)]
        ax.plot(lons, lats, color=route_color)
        xmin = min(xmin, min(lons))
        xmax = max(xmax, max(lons))
        ymin = min(ymin, min(lats))
        ymax = max(ymax, max(lats))

        for num, step in enumerate(route['steps']):
            if step['type'] == 'start':
                marker_shape = 'o'
                marker_color = 'blue'
            elif step['type'] == 'pickup':
                marker_shape = '^'
                marker_color = 'red'
            elif step['type'] == 'delivery':
                marker_shape = 'v'
                marker_color = 'green'
            else:
                continue
            
            ax.scatter([step['location'][0]], [step['location'][1]],
                            facecolor='none',
                            edgecolor=marker_color,
                            marker=marker_shape,
                            linewidth = 0.7)

            if num%2 == 0:
                time_of_stop = step['arrival']
                time_of_stop = datetime.fromtimestamp(int(step['arrival']), est_tz)
                time_formatted = time_of_stop.strftime('%I:%M')
                ax.annotate(time_formatted, (step['location'][0], step['location'][1]), fontsize = 'xx-small', 
                                color= route_color, textcoords="offset pixels", xytext=(-8,5))
        
        if 'unassigned' in solution and len(solution['unassigned']) > 0:
            unassigned_lons = [u['location'][0] for u in solution['unassigned']]
            unassigned_lats = [u['location'][1] for u in solution['unassigned']]
            ax.scatter(unassigned_lons,
                        unassigned_lats,
                        marker='x',
                        color='red',
                        s=100)       
            xmin = min(xmin, min(unassigned_lons))
            xmax = max(xmax, max(unassigned_lons))
            ymin = min(ymin, min(unassigned_lats))
            ymax = max(ymax, max(unassigned_lats))

    size_factor = max((xmax - xmin) / 100, (ymax - ymin) / 100)
    margin_delta = 3 * size_factor

    title = str(solution['summary']['delivery'][0]) + " deliveries"
    title += " ; cost: " + str(solution['summary']['cost'])
    title += " ; distance: " + str(solution['summary']['distance']) + " m"
    ax.set_title(title)

    ax.set_xlim(xmin - margin_delta, xmax + margin_delta)
    ax.set_ylim(ymin - margin_delta, ymax + margin_delta)
    ax.set_aspect('equal')

    print("Plotting file " + plot_file)
    
    plt.savefig(plot_file, bbox_inches='tight')
    plt.close() 
            