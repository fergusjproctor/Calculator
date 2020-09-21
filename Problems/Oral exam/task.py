from collections import deque
studs = deque()
n = int(input())
for _ in range(n):
    inp = input()
    if 'READY' in inp:
        studs.appendleft(inp.replace('READY ', ''))
    elif inp == 'EXTRA':
        studs.appendleft(studs.pop())
    elif inp == 'PASSED':
        print(studs.pop())
