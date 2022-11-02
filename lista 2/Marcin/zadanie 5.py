def palindrome(word):
    chars = list(word)
    if len(chars) == 0:
        return "Word is a palindrome"
    elif len(chars) == 1:
        return "Word is a palindrome"
    else:
        if chars[0] == chars[-1]:
            chars.pop(0)
            chars.pop(-1)
            new_word = "".join(chars)
            return palindrome(new_word)
        else:
            return "Word is not a palindrome"
print(palindrome("sdsas"))