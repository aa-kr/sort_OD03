mas = [1, 9, 12, 3, 7, 5, 15, 10, 4, 6]
n = 10
for run in range(n-1):
   for i in range(n-1-run):
       if mas[i] > mas[i + 1]:
           mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)
# Результат [1, 3, 4, 5, 6, 7, 9, 10, 12, 15]