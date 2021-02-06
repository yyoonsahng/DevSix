# input
n = int(input())

student_info = []
for _ in range(n):
    student_info.append(input().split())

# use sort function
student_info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for info in student_info:
    print(info[0])
