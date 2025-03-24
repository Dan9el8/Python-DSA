import sys

class Node:
    data = ''
    prev = None
    next = None

    def __init__(self,data):
        self.data = data

        class LinkedList:
            __head = None
            __tail = None

            def __init(self):
                self.__head = Node("San Fransisco")
                self.__head.prev = None
                self.__head.next = None

                node_oakland = Node("Oakland")
                node_oakland.prev = self.__head
                node_oakland.next = None
                self.__head.next = node_oakland

                node_berkeley = Node("Berkeley")
                node_berkeley.prev = node_oakland
                node_berkeley.next = None
                node_oakland.next = node_berkeley

                self.__tail = Node("Fremount")
                self.__tail.prev = node_berkeley
                self.__tail.next = None
                node_berkeley.next = self.__tail
                return self.__head
            
            def output(self, node):
                p = node
                end = None
                while p != None:
                    print (p, data, "->", end="")
                    end = p
                    p = p.next
                    print("End\n")

                    p = end
                    while p != None:
                        print(p.data, "->", end="")
                        p = p.prev
                        print("Start\n")

                        def main():
                            linkedlist = LinkedList()
                            head = linkedlist, init()
                            linkedlist, output(head)

                            if __name__ == "__main__":
                                main()