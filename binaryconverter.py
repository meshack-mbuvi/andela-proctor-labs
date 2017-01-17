def binary_converter(int_num):
  """
  Author:Mbuvi
  Function convert decimal numbers between 0 and 256 to their
  binary representaion
  params:int_num-number in decimal(base 10)
  Returns: binary-binary representation of int_num
  """
  if int_num in range(0, 256):#The binary converter is for numbers from 0 to 255
    if int_num == 0:
      return '0'#0 in binary is 0
    binary = ''
    while int_num > 0:
      if int_num % 2 == 0:
        int_num //= 2
        binary += '0'
      else:
        int_num //= 2
        binary += '1'
    return binary[::-1]#reverse the string 
  else:
    return 'Invalid input'#if number not between 0 and 256


#test cases
print binary_converter(0)
print binary_converter(62)
print binary_converter(-1)
print binary_converter(300)
print binary_converter(255)
