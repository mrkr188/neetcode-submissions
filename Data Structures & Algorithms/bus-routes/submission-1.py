class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        bus_stops = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                bus_stops[stop].append(i)
        # bus_stop: list of busses - { 1: [0], 7: [0, 1], .. }

        if source not in bus_stops:
            return -1
        
        seen = set([source])
        queue = deque() # bus, num_buses

        for bus in bus_stops[source]:
            queue.append((bus, 1))
        
        while queue:
            bus, num_buses = queue.popleft()
            for next_stop in routes[bus]:
                if next_stop == target:
                    return num_buses
                if next_stop not in seen:
                    seen.add(next_stop)
                    for next_bus in bus_stops[next_stop]:
                        queue.append((next_bus, num_buses+1))
        return -1

