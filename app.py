def hello():
    print("Hello World")


hello()


def say_hello(name):
    print(f"Hi {name}")


say_hello("Bob")  # Hi Bob
say_hello("Tom")  # Hi Tom


def double(number):
    return 2 * number


result_3 = double(3)
print(result_3)

print(double(1))  # 2
print(double(2))  # 4
print(double(3))  # 6


# 1分課題

def str_conbine(str1, str2):
    return str1 + " " + str2


result = str_conbine("Kazuma", "Takahashi")

print(result)  # Kazuma Tkahashi
