class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size <= 0:
            return self.storage.remove_from_head()
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size


class Node:
    def __init__(self, value=None, next_node=None):
        # its own value
        self.value = value
        # the next node in the list
        self.next_node = next_node

    def get_value(self):
        # return the value of this node
        return self.value

    def get_next(self):
        # return a reference to this node's next_node property
        return self.next_node

    def set_next(self, new_next):
        # set this node's `next_node` property
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference the first node in the linked list
        self.head = None
        # reference to the last node in the linked list
        self.tail = None

    # add a new node to the tail of our list
    def add_to_tail(self, value):
        new_node = Node(value)
        # we have an empty linked list
        # check the head reference
        if self.head is None and self.tail is None:
            # both self.head and self.tail to point
            # to the new node we're adding
            self.head = new_node
            self.tail = new_node
        # every other case
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # remove and return the value of the head node
    def remove_from_head(self):
        # make sure our list isn't empty
        if not self.head and not self.tail:
            return None
        # take another reference to the head we're
        # about to delete
        old_head_value = self.head.value
        # we only have a single node in the list
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        # we have at least two nodes in the list
        else:
            # move the self.head reference to refer
            # to the old head's next node
            self.head = self.head.get_next()
            return old_head_value

    def contains(self, target):
        # make sure we don't have an empty list
        if not self.head and not self.tail:
            return False
        # init a current reference to refer to the current
        # node we're iterating on
        current = self.head
        # while the current node in the list is a valid Node
        while current:
            # check if the current node's value matches
            # what we're looking for
            if current.value == target:
                return True
            # update the current reference to the next
            # node in the list
            current = current.get_next()
        # we've traversed the entire list
        return False


"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError(
                "That vertex has vanished w/o a trace, doesn't exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bf_traversal(self, starting_vert_id):
        queue = Queue()
        queue.enqueue(starting_vert_id)
        visited = []
        while queue.len() > 0:
            vert = queue.dequeue()
            if vert not in visited:
                # print("FIRST ADDED", vert)
                visited.append(vert)
                for next_vert in self.vertices[vert]:
                    queue.enqueue(next_vert)
        return visited

    def df_traversal_stack(self, starting_vert_id):
        stack = []
        stack.append(starting_vert_id)
        visited = []
        while len(stack) > 0:
            vert = stack.pop()
            if vert not in visited:
                visited.append(vert)
                for next_vert in self.vertices[vert]:
                    stack.append(next_vert)
        return visited

    def df_traversal_recursion(self, starting_vert_id, visited=None):
        if visited is None:
            visited = []
        vert = starting_vert_id
        if len(visited) != len(self.vertices.keys()):
            if vert not in visited:
                visited.append(vert)
                for next_vert in self.vertices[vert]:
                    return self.df_traversal_recursion(next_vert, visited)
            else:
                return self.df_traversal_recursion(vert, visited)
        elif len(visited) == len(self.vertices.keys()):
            return visited
