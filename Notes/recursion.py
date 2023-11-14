def add_one(num):
    ans = num + 1
    return ans


def rec_func(i):
    if i < 5:
        rec_func(i+1)
        print(i)

def main():
    rec_func(0) #initial call
    print('Goodbye')

main()
