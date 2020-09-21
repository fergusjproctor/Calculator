n = int(input())
unread = []
read = []
for _ in range(n):
    action = input()
    if 'BUY' in action:
        unread.append(action.replace('BUY ', ''))
    elif 'READ' in action:
        read.append(unread.pop())

for book in read:
    print(book)
