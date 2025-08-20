class MinStack(object):

    def __init__(self):
        self.st = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.st:
            self.st.append((val, min(val,self.st[-1][1])))
        else:
            self.st.append((val, val))

    def pop(self):
        """
        :rtype: None
        """
        if self.st:
            self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.st:
            return self.st[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if self.st:
            return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()