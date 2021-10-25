abb = input()
amounts = dict()
for i in range(int(input())):
    info = input()
    split_info = info.split()
    if split_info[0][0] + split_info[1][0] + split_info[2][0] == abb:
        if info in amounts:
            amounts[info] += 1
        else:
            amounts[info] = 1
for i in sorted(amounts.items(), key=lambda x: (-x[1], x[0])):
    print(i[0], i[1])
# 'qwe ' => 'qwe': rstrip
# ' qwe' => 'qwe': lstrip
# ' qwe qwe ' => 'qwe qwe': strip
