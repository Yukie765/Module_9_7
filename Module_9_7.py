def is_prime(sum_three):
    def wrapper(one,two,three):
        res = sum_three(one,two,three)

        if res <= 1:
            print("Not Simple")
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                print("Not Simple")
        print("Simple")

        return res
    return wrapper

@is_prime
def sum_three(one,two,three):
    return one+two+three

result = sum_three(2,3,6)
print(result)