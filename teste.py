# vingadores = ['homem de ferro', 'hulk', 'capitão america', 'viúva negra', 'gavião arqueiro']
# # for i in range(0, len(vingadores)):
# #     print(vingadores[i])
# # print()
# for h in vingadores:
#     print(h)
s = [16,24,6,14,12,15,10,7,5,3]
# max(s)
# print(max(s))
# a = []
# a = [x+2 for x in s]
# print(a)
a = [x for x in s if x % 2 == 0]
print(a)