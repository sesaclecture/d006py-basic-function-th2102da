def add(a, b):
    return a+b


def sub(a, b):
    return a-b



def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def power(base, pow):
    ans = 1
    for _ in range(pow):
        ans *= base
    
    return ans



def square(base):
    
    return power(base, 2)



def greet(이름="낯선자", 나이=20):

    if 이름 is None:
        이름 = "낯선자"

    if 이름 == "낯선자" and 나이 >= 20:
        return "안녕하신가 낯선자!"
    
    elif 나이 >= 20:
        return f"안녕하십니까 {이름}!"
    
    else:
        return f"안녕 낯선자!"
