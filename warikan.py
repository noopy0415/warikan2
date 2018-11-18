# # Table1:1500円で3人
# amount = 1500
# number_of_people = 3
# print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")
#
# # Table2:2000円で3人
# amount = 2000
# number_of_people = 3
# print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")
#
# # Table3:3647円で4人
# amount = 3647
# number_of_people = 4
# print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")


def warikan(price, count):
    return price // count, price % count


while 1:
    price = input("割り勘する金額を入力してください : ")
    if price == "": break

    count = input("割り勘する人数を入力してください : ")
    if count == "": break

    result = warikan(int(price), int(count))
    print(f"1人あたり: {str(result[0])}円, 端数: {str(result[1])}円")
