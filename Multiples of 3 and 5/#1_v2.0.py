# Solution v2.0
condition = [x for x in range(0,1000) if (x % 5 == 0 or x % 3 == 0)] 
sum = 0 
for x in condition: 
 sum += x 
print(sum)