def fun(text):
    text=str(text)
    rev_str=text[::-1]
    if text==rev_str:
        print("it is palindrom")
    else:
        print("It is not a palindrom")
    return text
print(fun("123321"))