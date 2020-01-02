# Simple linked list implementation

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        n = self.head

        while n:
            print(n.data)
            n = n.next

    def get_node(self, data):
        n = self.head
        if not n:
            return 'Empty list'
        stop = False
        while not stop:
            if n.data == data:
                stop = True
            else:
                if n.next is None:
                    stop = True
                    return 'Data not found'
                else:
                    n = n.next
        return n

    def insert_at_front(self, new_node):
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def insert_after_node(self, new_node, target_node):
        n = self.head

        if n == target_node:
            n.next = new_node
            return

        stop = False
        while not stop:
            if n == target_node:
                temp = n.next
                n.next = new_node
                new_node.next = temp
                stop = True
            else:
                n = n.next

    def insert_at_end(self, new_node):
        stop = False
        n = self.head

        # empty list
        if not n:
            self.head = new_node
            return

        while not stop:
            if n.next is None:
                n.next = new_node
                stop = True
            else:
                n = n.next

        n.next = new_node

# if __name__=='__main__':
#     linked_list = LinkedList()
#     linked_list.head = Node(1)
#     second = Node(5)
#     third = Node(7)
#     '''
#      llist.head        second              third 
#          |                |                  | 
#          |                |                  | 
#     +----+------+     +----+------+     +----+------+ 
#     | 1  | None |     | 5  | None |     |  7 | None | 
#     +----+------+     +----+------+     +----+------+ 
#     '''
#     linked_list.head.next = second
#     second.next = third
# 
#     ''' 
#     Now next of head refers to second and second Node refers to third.  So all three 
#     nodes are linked. 
# 
#     llist.head        second              third 
#          |                |                  | 
#          |                |                  | 
#     +----+------+     +----+------+     +----+------+ 
#     | 1  |  o-------->| 5  |  o-------->|  7 | null | 
#     +----+------+     +----+------+     +----+------+  
#     '''
#     
#     # ----------------------------------------------------------------------------------------
#     # insert at first
#     linked_list.insert_at_front(Node(10))
#     # insert at last
#     linked_list.insert_at_end(Node(20))
#     # get node with data 5
#     node = linked_list.get_node(5)
#     # print(node)
#     # insert at after node with data 5
#     linked_list.insert_after_node(Node(100), node)
#     linked_list.print_list()
