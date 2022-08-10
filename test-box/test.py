# k, l = map(int, input().split())
# v = list(map(int, input().split()))
# # print(k,l)
# # print(v)
# unique_v = set(v)
# # print(unique_v)
# value = 0
# for i in unique_v:
#     count = 0
#     for j in v:
#         if i == j:
#             count+=1
#     if count>l:
#         value = count
#         break
# print(value)
        
# 8 2
# 2 4 2 2 1 1 4 4

n = int(input())
id = list(map(int, input().split()))

# print(sorted(id))
i = 1
while i<n:
    try:
        if id[i-1]  < id[i+1]:
            temp = id[i-1]
            id[i-1] = id[i+1]
            id[i+1] = temp
            # print(id[i])
            # print(id)
        i+=1
    except Exception:
        # print(id[i-2])
        temp = id[i-2]
        id[i-2] = id[i]
        id[i] = temp
        i+=1
for i in id:
    print(i, end=' ')
# print(len(id))
# 5
# 10201 30215 90051 36103 92315