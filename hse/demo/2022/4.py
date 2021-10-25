student_count, useless_int = [int(i) for i in input().split()]
specialisations = [int(i) for i in input().split()]
output = [-1] * student_count
students = []
for i in range(student_count):
    string = input().split()
    students.append((i, int(string[0]), [int(string[j + 2]) for j in range(int(string[1]))]))
students.sort(key=lambda x: (x[1], x[2]))
for i in students:
    for j in i[2]:
        if specialisations[j - 1]:
            output[i[0]] = j
            specialisations[j - 1] -= 1
            break
print(output)