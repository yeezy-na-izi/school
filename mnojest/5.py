print(*(set([input() for _ in range(int(input()))]) -
        set([input() for _ in range(int(input())) for _ in range(int(input()))])), sep='\n')
