print("please enter your binary number")
num = int(input())
l = 0
s = 0
while (num):
  r = int(num % 10)
  s = s + (r * 2**l)
  num = int(num // 10)
  l += 1
print(s)


  
