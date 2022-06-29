def func(n):
    return lambda a:a * n
mydoubler=func(2)
mytripler=func(3)

print(mydoubler(11))
print(mytripler(11))