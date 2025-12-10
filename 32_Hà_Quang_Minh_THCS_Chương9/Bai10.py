def tim_so_fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)
print(tim_so_fibonacci(7))