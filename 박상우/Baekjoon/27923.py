from math import floor


n, k, l = map(int, input().split())
burger = list(map(int, input().split()))
k_idx = list(map(int, input().split()))

stomach_list = [0] * n 


for i in k_idx:
    for j in range(l):
        if i-1+j >= n:
            pass
        else:
            stomach_list[i-1+j] += 1 
            
stomach_list.sort(reverse=True)

stomach = 0 
burger.sort(reverse=True)
for i in range(len(burger)):
    stomach += floor(burger[i] / (2**stomach_list[i]))
    
print(stomach)