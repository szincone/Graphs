import random
# class Queue():
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None

#     def size(self):
#         return len(self.queue)


# class Stack():
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)


# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise IndexError("That vertex does not exist!")

#     def add_directed_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("That vertex does not exist!")

#     def dft_r(self, start_vert, visited=None):
#         if visited is None:
#             visited = set()
#         visited.add(start_vert)
#         print(start_vert)
#         for child_vert in self.vertices[start_vert]:
#             if child_vert not in visited:
#                 self.dft_r(child_vert, visited)

#     def bfs_path(self, starting_vertex_id, target_value):
#         q = Queue()
#         q.enqueue([starting_vertex_id])
#         visited = set()
#         while q.size() > 0:
#             path = q.dequeue()
#             v = path[-1]
#             if v not in visited:
#                 if v == target_value:
#                     return path
#                 visited.add(v)
#                 for next_vert in self.vertices[v]:
#                     new_path = list(path)
#                     new_path.append(next_vert)
#                     q.enqueue(new_path)
#         return None

#     def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
#         if visited is None:
#             visited = set()
#         if path is None:
#             path = []
#         visited.add(start_vert)
#         path = path + [start_vert]
#         if start_vert == target_value:
#             return path
#         for child_vert in self.vertices[start_vert]:
#             if child_vert not in visited:
#                 new_path = self.dfs_r_path(
#                     child_vert, target_value, visited, path)
#                 if new_path:
#                     return new_path
#         return None
# added above code from lecture


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for x in range(numUsers):
            self.addUser(x)
        # Create friendships
        for x in self.users:
            self.rand_avg_num_friendships = round(
                (random.random() * avgFriendships) * 2)
            for j in range(self.rand_avg_num_friendships):
                self.rand_user_in_list = random.randint(1, len(self.users))
                self.addFriendship(x, self.rand_user_in_list)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
