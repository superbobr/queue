from collections import deque

n = int(input())
i = 0
queue = deque()
students = []

while i < n:
    student = input()
    if student.startswith('READY'):
        queue.append(student[6:])
    elif student == 'EXTRA':
        extra_stud = queue.popleft()
        queue.append(extra_stud)
    else:
        pass_stud = queue.popleft()
        students.append(pass_stud)
    i += 1

for student in students:
    print(student)
