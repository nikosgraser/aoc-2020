with open('input', 'r') as fd:
    arrival_raw, bus_lines_raw = fd.read().strip().split('\n')

arrival = int(arrival_raw)
bus_lines = map(int, filter(lambda bl: bl != 'x', bus_lines_raw.split(',')))

bus_dpt_after_arrival = dict()
for bus_line in bus_lines:
    dpt = bus_line
    while dpt < arrival:
        dpt += bus_line
    bus_dpt_after_arrival[bus_line] = dpt

bus, bus_dpt = min([(k, v) for k, v in bus_dpt_after_arrival.items()], key=lambda kv: kv[1])
print(bus * (bus_dpt - arrival))
