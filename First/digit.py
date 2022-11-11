from in_num import indata


def parse():
    s = indata()
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(float(digit))
            digit = ""
            result.append(symbol) 
    else:
        if digit:
            result.append(float(digit))
    return result


def calculate(lst):
    result = 0.0
    for s in lst:  
        if s == '*' or s == '/':
            if s == '*':
                index = lst.index(s)
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] / lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    for s in lst:  
        if s == '+' or s == '-':
            if s == '+':
                index = lst.index(s)
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] - lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result
