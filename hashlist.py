import hashlib

class Node:
    # no previous hash supplied if this is the first node
    def __init__(self, value, previous_hash='head'):
        # this node's value
        self.value = value
        # hash the previous hash and the data
        self.previous_hash = previous_hash
        # a reference to the next node
        self.next = None    
        # sha256 hash of the data
        self.hash = Node.make_hash(self.value, self.previous_hash)

    def __str__(self):
        return f'{self.hash} : {self.value}\n'

    @staticmethod  #decorator
    def make_hash(value, previous_hash):
        # hash the previous hash and the data
        history = str(value) + previous_hash
        # print('making node hash:', history)
        return hashlib.sha256(history.encode()).hexdigest()

    @staticmethod
    def validate(prev_node, current_node):
        if current_node.hash == Node.make_hash(current_node.value, prev_node.hash):
            return True
        else:
            return False
    @staticmethod
    def valid_list():
        pass

    def consensus(head):
        # if the head is the only node, it's valid
        if not head.next:
            return True
        current_node = head
        while current_node.next:
            if not Node.validate(current_node, current_node.next):
                return False
            current_node = current_node.next
        return True

    # hash list tests
head = Node(0)
# print("head node:", head)
one = Node(1, head.hash)
head.next = one
# print("one node:", one)
two = Node(2, one.hash)
one.next = two
# print("two node:", two)
three = Node(3, two.hash)   # three is the last node
two.next = three
# print("three node:", three)

# test the validation
# print("validating head node:", Node.validate(one, two))
# print("validating head node:", Node.validate(one, three))

print(Node.consensus(head))
print(Node.consensus(Node(10)))
two.value = 4   
print(Node.consensus(head))