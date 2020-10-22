def main():
    #write your code below this line
    print(sum_list(range(0,5)))
def sum_list(numbers):
  soma = 0
  for number in numbers:
    soma+=number
  return soma

if __name__ == '__main__':
    main()
