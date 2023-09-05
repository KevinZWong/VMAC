# Generate all possible combinations of movement types and time graphs
x_movements = ['LtR', 'RtL', 'L', 'C', 'R']  # X-axis movement or fixed position
y_movements = ['TtB', 'BtT', 'T', 'M', 'B']  # Y-axis movement or fixed position
time_graphs = ['E', 'L']  # 'E' for Exponential, 'L' for Linear

# Generate the list of all possible movement types
all_possibilities = [f"{x}_{y}_{time_graph}" 
                     for x in x_movements 
                     for y in y_movements 
                     for time_graph in time_graphs ]

print(f"all_possibilities = {all_possibilities }")