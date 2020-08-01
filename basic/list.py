#list: 마트의 장바구니 느낌, 내용을 넣고 빼고가 쉬움, 대신에 연산은 좀 느림(이건 컴퓨터 속도가 빨라져서 어느정도는 커버가능)
#[] 이런식으로

a_list = ["카네기", "스탠포드", "버클리", "콜롬비아", "하버드"]
b_list = ["UCLA", "MICHIGAN", "UPenn", "UIUC", "UW"]

# #데이터 추가하기 - 이경우 가장 끝에 코넬이 추가됨
# a_list.append("코넬")
# print(a_list)
#
# #데이터 삭제하기 - 이 경우 카네기가 날라감
# del a_list[0]
# print(a_list)
#
# #반복문 1
# for index, value in enumerate(a_list):
#     print("%s - %s" % (index, value))
#
# #반복문 2
# cnt = 0
# for value2 in a_list:
#     print("%s - %s" % (cnt, value2))
#     cnt += 1
#
# 반복문 + 특정데이터 삭제
# check_univ = "버클리"
#
# cnt = 0
# for value in a_list:
#     if value == check_univ:
#         del a_list[cnt]
#
#     cnt += 1
# print(a_list)
#
# #반복문 + 특정데이터 그룹을 추가
# for value in b_list:
#     a_list.append(value)
#
# print(a_list)

#반복문 + 특정데이터 그룹으로 교체
for index, value in enumerate(b_list):
    a_list[index] = value

print(a_list)