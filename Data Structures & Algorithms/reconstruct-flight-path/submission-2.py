class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        # create adjacency list
        for src, dst in tickets:
            adj[src].append(dst)
        
        # sort the itinerary based on the lexical order
        for origin in adj:
            adj[origin].sort(reverse=True)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                # airports are added to the answer only when they have no remaining outgoing edges.
                res.append(stack.pop())
            else:
                # keep moving forward while tickets exist
                stack.append(adj[curr].pop())

        return res[::-1]
        