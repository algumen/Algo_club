#n=int(input())
stones = input()

i = 1
new_stones = stones[0]
while i < len(stones):
    if stones[i] != stones[i-1]:
        new_stones = new_stones+stones[i]
    i += 1

#if stones[len(stones)-2] != stones[len(stones)-1] or new_stones == '':
 #       new_stones = new_stones+stones[i]

print(new_stones)
print(len(stones)-len(new_stones))
