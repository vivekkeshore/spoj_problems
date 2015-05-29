# Vivek Keshore
# http://www.spoj.com/problems/STPAR/


class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            item = self.items.pop()
            self.items.append(item)
            return item
        # return self.items[len(self.items)-1]  # Will take O(n) due to len

        else:
            return None

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def reset(self):
        self.items = []


while True:
    num = int(raw_input())
    if num == 0:
        break

    data = raw_input().split()
    trucks = [int(truck) for truck in data]
    flag = True

    side_street = Stack()
    parade = Stack()

    for i in xrange(num):
        curr_truck = trucks[i]

        side_truck = side_street.peek()
        parade_truck = parade.peek()

        while not side_street.is_empty():
            side_truck = side_street.peek()
            if side_truck <= curr_truck:
                if side_truck < parade_truck:
                    flag = False
                    break
                else:
                    side_truck = None
                    parade.push(side_street.pop())
            else:
                break

        if i + 1 < num:
            if curr_truck > trucks[i+1]:
                if side_truck and side_truck < curr_truck:
                    flag = False
                    break
                else:
                    side_street.push(curr_truck)

            else:
                if parade_truck and parade_truck > curr_truck:
                    flag = False
                    break
                else:
                    parade.push(curr_truck)
        else:
            if parade_truck and parade_truck > curr_truck:
                flag = False
                break
            else:
                parade.push(curr_truck)

    if flag:
        print 'yes'
    else:
        print 'no'
