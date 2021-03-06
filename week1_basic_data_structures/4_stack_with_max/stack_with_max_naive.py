#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max=[]

    def Push(self, a):
        if len(self.__stack)==0:
            self.max=[a] 
            self.__stack.append(a)
        elif self.max[-1]<=a:
            self.__stack.append(a)
            self.max.append(a)
        else:
            self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1]==self.max[-1]:
            self.__stack.pop()
            self.max.pop()
        else:
            self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
