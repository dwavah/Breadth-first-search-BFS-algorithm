from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            node, level = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        return visited

    def mutualf(self, user1, user2):
        friends_user1 = self.bfs(user1)
        friends_user2 = self.bfs(user2)
        mutual_friends = friends_user1.intersection(friends_user2)
        mutual_friends.remove(user1)  
        mutual_friends.remove(user2)  
        return mutual_friends

social = Graph()
social.add_edge('Daniel', 'Wavah')
social.add_edge('Daniel', 'Lukya')
social.add_edge('Wavah', 'Chris')
social.add_edge('Lukya', 'Denis')
social.add_edge('Denis', 'Peter')
social.add_edge('Wavah', 'Mase')

user1 = 'Daniel'
user2 = 'Wavah'
mutualf = social.mutualf(user1, user2)
print(f"The mutual friends between {user1} and {user2} are {mutualf}")
