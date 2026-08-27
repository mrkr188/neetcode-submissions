class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        bus_stops = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                bus_stops[stop].append(bus)
        # bus_stops: list of busses - { 1: [0], 7: [0, 1], .. }

        if source not in bus_stops or target not in bus_stops:
            return -1

        q = deque([source])
        visited_buses = set()
        visited_stops = {source}
        buses_taken = 0
        
        while q:
            buses_taken += 1
            for i in range(len(q)):
                curr = q.popleft()

                for bus in bus_stops[curr]:
                    if bus in visited_buses:
                        continue

                    visited_buses.add(bus)
                    for nei in routes[bus]:
                        if nei == target:
                            return buses_taken
                        if nei in visited_stops:
                            continue
                        visited_stops.add(nei)
                        q.append(nei)
        return -1
        
        # if source == target:
        #     return 0

        # bus_stops = defaultdict(list)
        # for i in range(len(routes)):
        #     for stop in routes[i]:
        #         bus_stops[stop].append(i)
        # # bus_stop: list of busses - { 1: [0], 7: [0, 1], .. }

        # if source not in bus_stops:
        #     return -1
        
        # seen = set([source])
        # queue = deque() # bus, num_buses

        # for bus in bus_stops[source]:
        #     queue.append((bus, 1))
        
        # while queue:
        #     bus, num_buses = queue.popleft()
        #     for next_stop in routes[bus]:
        #         if next_stop == target:
        #             return num_buses
        #         if next_stop not in seen:
        #             seen.add(next_stop)
        #             for next_bus in bus_stops[next_stop]:
        #                 queue.append((next_bus, num_buses+1))
        # return -1

