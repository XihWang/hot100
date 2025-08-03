class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            graph[pre].append(cur)
        visited = [False] * numCourses
        onPath = [False] * numCourses
        self.hascircle = False

        def dfs(graph, s):
            if onPath[s]:
                self.hascircle = True
                return
            if visited[s]:
                return
            visited[s] = True
            onPath[s] = True
            for t in graph[s]:
                dfs(graph, t)
            onPath[s] = False

        for i in range(numCourses):
            if not visited[i]:  # 这行有没有都一样
                dfs(graph, i)
        return not self.hascircle






