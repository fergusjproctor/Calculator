reversed_queue = deque()
while queue:
    reversed_queue.appendleft(queue.popleft())
