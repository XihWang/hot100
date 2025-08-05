class Solution(object):
    def __init__(self):
        self.hascircle = False
    def graphmake(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        for prerequisite in prerequisites:
            i, j = prerequisite
            graph[j].append(i)
        return graph


    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited = [False] * numCourses
        onpath = [False] * numCourses
        graph = self.graphmake(numCourses, prerequisites)
        postorder = []
        def traverse(graph, s):
            if onpath[s] == True:
                self.hascircle = True
            if self.hascircle == True or visited[s]:
                return
            visited[s] = True
            onpath[s] = True
            for t in graph[s]:
                traverse(graph, t)
            onpath[s] = False
            postorder.append(s)
        for i in range(numCourses):
            traverse(graph, i)
        if self.hascircle == True:
            return []
        postorder.reverse()
        return postorder





