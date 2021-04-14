import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()
for i in cur.execute(
        f'SELECT name, height, distance FROM registry, types '
        f'WHERE types.id = registry.types_id AND registry.danger > {int(input())} ORDER by distance'):
    print(*i)
