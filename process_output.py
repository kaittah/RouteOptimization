import json

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def read_output(case, repetition):
    solution_file = 'solution_files/case_' + str(case) + '_' + str(repetition) + '_output.json' 

    with open(solution_file, 'r') as sol_file:
        data = json.load(sol_file)

    return data['summary']['delivery'][0], data['summary']['cost'], data['summary']['distance']

cases = ['A', 'B', 'C', 10, 20, 30]

case_results = {}
for key in cases:
    case_results[key] = {'delivery_counts':[], 'costs':[], 'distances':[]}

for repetition in range(15):
    for case in cases:
        delivery_count, cost, distance = read_output(case, repetition)
        case_results[case]['delivery_counts'].append(delivery_count)
        case_results[case]['costs'].append(cost)
        case_results[case]['distances'].append(distance)

dataframes =[]
for case in case_results.keys():
    case_data = pd.DataFrame.from_dict(case_results[case])
    case_data['Case'] = case
    dataframes.append(case_data)
    print('______________')
    print(case)
    print(case_data.mean())
    print('______________')
df = pd.concat(dataframes)

fig, axes = plt.subplots()
sns.boxplot(data =  [   df[df.Case == 'A']['distances'].values,
                        df[df.Case == 'B']['distances'].values,
                        df[df.Case == 'C']['distances'].values,
                        df[df.Case == 10]['distances'].values,
                        df[df.Case == 20]['distances'].values,
                        df[df.Case == 30]['distances'].values 
                        ]).set_title('Distances of solution to route optimization, 20 repetitions')
plt.show()
                                    