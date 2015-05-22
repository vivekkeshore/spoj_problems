# Vivek Keshore
# http://www.spoj.com/problems/ONP/


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
            print 'Empty Stack ...'
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

optstack = Stack()
output = Stack()

inp = int(raw_input())
for i in xrange(inp):
    expression = raw_input()
    expression = list(expression)
    precedence = {'/': 4, '*': 3, '+': 2, '-': 1}

    for char in expression:
        if char == ' ':
            continue
        elif char == '(':
            optstack.push(char)
        elif char in '*/+^-':
            # import pdb; pdb.set_trace()
            order = precedence.get(char)
            while precedence.get(optstack.peek()) >= order \
                    and optstack.peek() in '/*+-':
                output.push(optstack.pop())
            optstack.push(char)

        elif char == ')':
            if not optstack.is_empty():
                while True:
                    item = optstack.pop()
                    if item and item != '(':
                        output.push(item)
                    else:
                        break
            else:
                print 'Invalid Expression'
        else:
            output.push(char)

    postfix_exp = ''
    while not optstack.is_empty():
        output.push(optstack.pop())
    while not output.is_empty():
        postfix_exp += output.pop()

    print postfix_exp[::-1]
