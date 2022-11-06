def palindrome(text):
    redacted = [letter for letter in text if letter.isalnum()]

    if len(redacted) <= 2:
        if len(redacted) == 1:              return True
        elif redacted[0] == redacted[1]:    return True
        else:                               return False
    
    inner = palindrome(redacted[1:-1])

    if (redacted[0] == redacted[-1]) and inner: return True
    else:                                       return False
    

print(palindrome("abc,def fedc,,b,a"), '---> Palindrom')
print(palindrome("lubie robic muze d-_____-b"), '---> Nie Palindrom')