import sys

class Node:
    data = ''
    next = None
    prev = None

    def __init__(self, data):
        self.data = data

        class Queue:
            __head = None
            __tail = None
            __size = 0

            def offer(self, element):
                if self.__head == None:
                    self.__head = Node(element)
                    self.tail = self.__head
                else:
                    new_node = Node(element)
                    new_node.next = self.__tail
                    self.__tail.prev = new_node
                    self.__tail = new_node
                    self.__size+=1

                    def poll(self):
                        p = self.__head
                        if p == None:
                            return None
                        self.__head = self.__head.prev
                        p.next = None
                        p.prev = None
                        self.__size = 1
                        return p
                    @property
                    def size(self):
                        return self.__size
                    
                    def output(self, queue):
                        print("Head", end="")
                        node = queue.poll()
                        while node != None:
                            print (node, data, "<-", end="")
                            node = queue.poll()
                            print("Tail\n")

                            def main():
                                queue = Queue()
                                queue.offer("A")
                                queue.offer("B")
                                queue.offer("C")
                                queue.offer("D")
                                queue.output(queue)

                                if __name__ == "__main__":
                                    main()
