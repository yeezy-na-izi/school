# from functools import

def dfs(graph, start, finish, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, finish, visited)
    if finish in visited:
        return True
    return False


def dfs1(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print(start)
    for next in graph[start] - visited:
        dfs1(graph, next, visited)
    return visited


# @lru_cache


city_count, way_count = [int(i) for i in input().split()]

nonexistent_ways = [set() for i in range(city_count + 1)]
existing_ways = [set() for i in range(city_count + 1)]

for i in range(way_count):
    string = input().split()
    if string[0] == '+':
        existing_ways[int(string[1])] |= {int(string[2])}
        existing_ways[int(string[2])] |= {int(string[1])}
        nonexistent_ways[int(string[1])] |= {int(string[2])}
        nonexistent_ways[int(string[2])] |= {int(string[1])}
    elif string[0] == '-':
        nonexistent_ways[int(string[1])] |= {int(string[2])}
        nonexistent_ways[int(string[2])] |= {int(string[1])}
    else:
        # print(existing_ways)
        # print(nonexistent_ways)
        # print(string[1], string[2])
        plus_path = dfs(existing_ways, int(string[1]), int(string[2]))
        minus_path = dfs(nonexistent_ways, int(string[1]), int(string[2]))

        # print(dfs1(nonexistent_ways, int(string[1])))
        if plus_path:
            print('+')
        elif minus_path:
            print('-')
        else:
            print('?')

# print(existing_ways)
# print(nonexistent_ways)
