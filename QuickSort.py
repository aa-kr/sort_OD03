def quick_sort(s):
   if len(s) <= 1:
       return s

   element = s[0]
   left = list(filter(lambda i: i < element, s))
   center = [i for i in s if i==element]
   right = list(filter(lambda i: i > element, s))

   return quick_sort(left) + center + quick_sort(right)

print(quick_sort([1, 9, 12, 3, 7, 5, -5, 5, 15, 10, 4, 6]))
# Результат: [-5, 1, 3, 4, 5, 5, 6, 7, 9, 10, 12, 15]