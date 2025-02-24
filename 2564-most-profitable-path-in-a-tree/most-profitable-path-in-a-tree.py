class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = []
        self.max_income = float("-inf")

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n

        # Form tree with edges
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        # Find the path taken by Bob to reach node 0 and the times it takes to get there
        self.find_bob_path(bob, 0)

        # Find Alice's optimal path
        self.visited = [False] * n
        self.find_alice_path(0, 0, 0, amount)

        return self.max_income

    # Depth First Search to find Bob's path
    def find_bob_path(self, source_node, time):
        # Mark and set time node is reached
        self.bob_path[source_node] = time
        self.visited[source_node] = True

        # Destination for Bob is found
        if source_node == 0:
            return True

        # Traverse through unvisited nodes
        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node] and self.find_bob_path(
                adjacent_node, time + 1
            ):
                return True

        # If node 0 isn't reached, remove current node from path
        self.bob_path.pop(source_node, None)
        return False

    # Depth First Search to find Alice's optimal path
    def find_alice_path(self, source_node, time, income, amount):
        # Mark node as explored
        self.visited[source_node] = True

        # Alice reaches the node first
        if (
            source_node not in self.bob_path
            or time < self.bob_path[source_node]
        ):
            income += amount[source_node]
        # Alice and Bob reach the node at the same time
        elif time == self.bob_path[source_node]:
            income += amount[source_node] // 2

        # Update max value if current node is a new leaf
        if len(self.tree[source_node]) == 1 and source_node != 0:
            self.max_income = max(self.max_income, income)

        # Traverse through unvisited nodes
        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node]:
                self.find_alice_path(adjacent_node, time + 1, income, amount)