import json

import requests
from pprint import pprint

def call(case, repetition, shipments, vehicles):
    #format call body
    body ={'shipments': [ship.get_dictionary() for ship in shipments], 
            'vehicles': [car.get_dictionary() for car in vehicles],
            'options':{'g':True}}
    
    input_file_name = 'input_files/case_' + str(case) + '_' + str(repetition) + '_input.json' 
    with open(input_file_name, 'w') as f:
        json.dump(body, f)

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': API_KEY,
        'Content-Type': 'application/json; charset=utf-8'
    }

    call = requests.post('https://api.openrouteservice.org/optimization', json=body, headers=headers)
    print(call.status_code, call.reason)

    #process results
    data = call.json()

    output_file_name = 'solution_files/case_' + str(case) + '_' + str(repetition) + '_output.json' 
    with open(output_file_name, 'w') as f:
        json.dump(call.json(), f)
    
    return data['summary']['delivery'][0], data['summary']['cost'], data['summary']['distance']