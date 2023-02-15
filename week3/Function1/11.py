def palindrome(word):
    newW= word[::-1]
    if newW == newW[::-1]:
        return True
    else:
        return False

print(palindrome(str(input())))