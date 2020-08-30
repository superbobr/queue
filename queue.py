from collections import deque

n = int(input())
queue = deque()
i = 0
while i < n:
    issue = input()
    if issue == 'SOLVED':
        queue.popleft()
    else:
        queue.append(issue)
    i += 1

for issue in queue:
    print(issue[-1])
