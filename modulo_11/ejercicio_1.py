from collections import deque


class Node:
    def __init__(self, num):
        self.num = num
        self.visited = False
        self.distance = 0
        self.neighbors = []

    def __str__(self):
        return f'{self.num}:{self.distance}'


def print_interaction(graph):  # iterate using BFS
    q = deque()
    start = 0
    q.append(start)
    while len(q) > 0:
        current = q.popleft()
        for node in graph[current]:
            if not node.visited:
                node.visited = True
                q.append(node.num)


def run():
    for i in range(int(input())):
        people, couples = map(int, input().split(', '))
        graph = {}
        for j in range(people):
            graph[j] = Node(j)
        for j in range(couples):
            doc1, doc2 = map(int, input().split())
            graph[doc1].neighbors.append(doc2)
        print_interaction(graph)


if __name__ == '__main__':
    run()
