# practice01

r = 10
pi = 3.1415

print("r =", r)
print("r =", r*2)
print("r =", r**2*pi)
print("r =", r*2*pi)
print("r =", 4*pi*r**2)
print("r =", 4/3*pi*r**3)

# Refactoring Practice01
r = eval(input("r > "))

pi = 3.1415

print("r =", round(r,3))
print("d =", round(r*2,3))
print("c =", round(r**2*pi,3))
print("a =", round(r*2*pi,3))
print("gnb =", round(4*pi*r**2,3))
print("v =", round(4/3*pi*r**3,3))

# Final Practice
## 1
number = input()
number = '-'.join(number.split(' '))
print(number)

## 2
_str = input()
if _str.isalpha():
  print(f"{_str}은 알파벳 단독")
elif _str.isdㄹigit():
  print(f"{_str}은 숫자 단독")
elif _str.isalnum():
  print(f"{_str}은 알파벳 숫자")
if _str.islower():
  print(f"{_str}은 소문자")
if _str.isupper():
  print(f"{_str}은 대문자")
