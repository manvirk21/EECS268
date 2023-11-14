def my_div(num1, num2):
    if num2 != 0: #this is not need for the try/except only return
        return num1/num2
    else:
        raise ZeroDivisionError

def middle_func(num1, num2):
    print("middle_func called")
    ans = my_div(num1, num2)
    print("middle_func ending")
    return ans


def main():
    ans = middle_func(10,5)
    print(ans)

    try:
        ans = my_div(20, 5)
        print(ans)
        ans = middle_func(10, 0)
        print(ans)
    except:
        print("Uh oh! Something broke!")

    print(ans)
    
main()
