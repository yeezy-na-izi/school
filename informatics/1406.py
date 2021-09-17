def anagram(a, b):
    if sorted(a) == sorted(b):
        return False
    return True


print('NO' if anagram(input(), input()) else 'YES')