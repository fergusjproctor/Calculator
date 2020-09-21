from collections import deque
n = int(input())
issues = deque()
for _ in range(n):
    action = input()
    if 'ISSUE' in action:
        issues.appendleft(action.replace('ISSUE ', ''))
    elif 'SOLVED' in action:
        issues.pop()

while issues:
    print(issues.pop())
