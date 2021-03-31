print(*(set([input() for i in range(int(input()))]) -
        set([input() for i in range(int(input())) for j in range(int(input()))])), sep='\n')
