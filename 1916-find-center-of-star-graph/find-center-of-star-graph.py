class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Since it's a star graph, the center node must be common in at least two edges
        # Check the first two edges and return the common node
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
