def binary_converter(int_num):
  if int_num in range(0, 256):
    if int_num == 0:
      return '0'
    binary = ''
    while int_num > 0:
      if int_num % 2 == 0:
        int_num //= 2
        binary += '0'
      else:
        int_num //= 2
        binary += '1'
    return binary[::-1]
  else:
    return 'Invalid input'



print binary_converter(0)
print binary_converter(62)
print binary_converter(-1)
print binary_converter(300)
print binary_converter(255)