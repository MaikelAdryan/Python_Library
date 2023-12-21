def apply(func, val):
  return func(val)

print(apply(lambda x: x + 1, (1)))


print(list(map(lambda x: x ** 2, range(6))))
pows = []
for num in range(6):
  pows.append((lambda x: x ** 2)(num))
print(pows) # -> 
