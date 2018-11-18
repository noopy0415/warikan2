# # Table1:1500円で3人 -> 500, 0
# # Table2:2000円で3人 -> 666, 1
# # Table3:3647円で4人

def calc_warikan(amount, number_of_people):
    return f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円"

# print(warikan(amount=2000, number_of_people=3))
# print(warikan(amount=1500, number_1of_people=3))
# print(warikan(amount=3647, number_of_people=4))
