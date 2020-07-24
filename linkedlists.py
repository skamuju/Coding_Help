class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
​
    def __str__(self):
        return str(self.data)
​
class SinglyLinkedList:
​
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
​
    def push(self, new_node):
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
​
    def pop(self):
        if self.length == 0:
            raise IndexError("pop from empty list")
        else:
            return_node = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                prev = None
                while current.next is not None:
                    if current.next.next is None:
                        break
                    prev = current
                    current = current.next
                self.tail = current
                self.tail.next = None
            self.length -= 1
            return return_node
​
    @staticmethod
    def none_repr(node):
        return str(node) if node is not None else ""
​
    def navigate(self):
        return_string = "["
        current = self.head
        if self.length in (0,1):
            return_string += self.none_repr(self.head)
        else:
            while current.next is not None:
                return_string += self.none_repr(current) + ", "
                current = current.next
            return_string += self.none_repr(current)
​
        return return_string + "]"
​
    def __str__(self):
        return_string = f'length: {self.length} '
        return_string += f'sll: {self.navigate()} '
        return return_string
​
    def __len__(self):
        return self.length
​
if __name__ == "__main__":
    data = 201
    addr_next = None
    first = Node(data)
    my_sll = SinglyLinkedList()
    print(my_sll)
    # my_sll.pop()
    my_sll.push(first)
    # popped_value = my_sll.pop()
    popped_value = None
    print(f"popped value is: {popped_value}")
    print(my_sll)
    
​
    second = Node(202)
    my_sll.push(second)
    popped_value = my_sll.pop()
    # popped_value = None
    print(f"popped value is: {popped_value}")
    print(my_sll)
​
    third = Node(203)
    my_sll.push(third)
    # popped_value = my_sll.pop()
    popped_value = None
    print(f"popped value is: {popped_value}")
    print(my_sll)
​
    fourth = Node(204)
    my_sll.push(fourth)
    # popped_value = my_sll.pop()
    popped_value = None
    print(f"popped value is: {popped_value}")
    print(my_sll)
​
​
    # fifth = Node(200)
    # my_sll.shift(fifth)
    # print(my_sll)
    # my_sll.unshift()
    # print(f"sll after unshift: {my_sll}")
    # my_sll.unshift()
    # print(f"sll after unshift: {my_sll}")