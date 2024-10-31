# # menu = input("Menu ID : ")
# # menu_list = []
# # while menu != "N" :
# #         menu_list.append(menu)
# #         print(menu_list)
# #         menu = input("Menu ID : ")
# # print("All" , menu_list)

# menu_list = []
# amount_list = []
# Total_sum = []

# menu = input("Menu ID : ")
# amount = int(input("Amount : "))
# yes_no = input("Next Order(Y/N) : ")

# while yes_no != "N" : 
#     amount_list.append(amount)
#     menu_list.append(menu)

# while yes_no != "N" :   
#     if menu == "F01" or menu_list == "F02" or menu == "F03" or menu == "F04" or menu == "D01" or menu == "D02" :
#         print(menu_list)
#         print(amount_list)
#         print(Total_sum)
#         if menu == "F01" :
#             Total_sum.append(125*amount)
#         elif menu == "F02" :
#             Total_sum.append(145*amount)
#         elif menu == "F03" :
#             Total_sum.append(169*amount)
#         elif menu == "F04" :
#             Total_sum.append(139*amount)
#         elif menu == "D01" :
#             Total_sum.append(90*amount)
#         elif menu == "D02" :
#             Total_sum.append(60*amount)
#         continue
#     menu = input("Menu ID : ")
#     amount = int(input("Amount : "))
#     yes_no = input("Next Order(Y/N) : ")
# print(menu_list)
# print(amount_list)
# print(Total_sum)

# # if menu == "F01" :
# #             Total_sum.append(125*amount)
# #         elif menu == "F02" :
# #             Total_sum.append(145*amount)
# #         elif menu == "F03" :
# #             Total_sum.append(169*amount)
# #         elif menu == "F04" :
# #             Total_sum.append(139*amount)
# #         elif menu == "D01" :
# #             Total_sum.append(90*amount)
# #         elif menu == "D02" :
# #             Total_sum.append(60*amount)
# #         continue

my_list = [10, 20, 30, 40, 50]
index = 0

while index < len(my_list):
  print(my_list[index])
  index += 1