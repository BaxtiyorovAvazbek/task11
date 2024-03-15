# 1-masala

# def steps_to_convert(lst1):
#     result = 0
#     result1 = 0
#     for x in lst1:
#         if x.count(x.lower()) == 1:
#             result += 1
#         elif x.count(x.upper()) == 1:
#             result1 += 1
#     if result < result1:
#         return result
#     elif result == result1:
#         return result
#     else:
#         return result1
#
#
# print(steps_to_convert("abC"))
# print(steps_to_convert("abCBA"))
# print(steps_to_convert("aba"))
# print(steps_to_convert("abaCCC"))

# 2-masala

# def maximum_score(lst):
#     result = 0
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         for values in x.values():
#             if type(values) == int:
#                 result += values
#         i += 1
#     print(result)
#
#
# maximum_score([
#     {"tile": "N", "score": 1},
#     {"tile": "K", "score": 5},
#     {"tile": "Z", "score": 10},
#     {"tile": "X", "score": 8},
#     {"tile": "D", "score": 2},
#     {"tile": "A", "score": 1},
#     {"tile": "E", "score": 1}
# ])

# 3-masala

# def convert_to_number(lst):
#     while lst:
#         x, y = lst.popitem()
#         if type(y) == str:
#             m = int(y)
#             print(f"{x}", y)
#
#
# convert_to_number({"piano": "200"})

# 4-masala

# def get_budgets(lst):
#     result = 0
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         y = x.get("budget")
#         result += y
#         i += 1
#     print(result)
#
#
# get_budgets([
#     {"name": "John", "age": 21, "budget": 23000},
#     {"name": "Steve", "age": 32, "budget": 40000},
#     {"name": "Martin", "age": 16, "budget": 2700}
# ])

# 5-masala

# def mapping(lst):
#     result = {}
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         result[x] = x.upper()
#         i += 1
#     print(result)
#
#
# mapping(["p", "s"])

# 6-masala

# def is_subset(lst, lst2):
#     i = 0
#     while i < len(lst):
#         m = set(lst)
#         n = set(lst2)
#         i += 1
#         return m.issubset(n)
#
#
# print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))

# 7-masala

# def func(lst,lst2):
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         if type(x) == str:
#             lst2.append(x)
#         i += 1
#     return lst2
#
#
# print(func([1, 2, 3, 4, "a", "b", "d", 5, 6], []))

# 8-masala
# def func(lst,lst2):
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         if x > 6:
#             lst2.append(x)
#         i += 1
#     return lst2
#
#
# print(func([7, 4, 17, 14, 12, 34, 8, 3], []))

# 9-masala
# def func(lst,lst2):
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         if type(x) == int:
#             lst2.append(x)
#         i += 1
#     return lst2
#
#
# print(func([9, 2, "nike", "lamborgini", "white", 16], []))

# 10-masala

# def func10(lst):
#     result = 0
#     for x in lst:
#         if lst.count(x.upper()) == 1:
#             result += 1
#     return result
#
#
# print(func10(["abDCE"]))