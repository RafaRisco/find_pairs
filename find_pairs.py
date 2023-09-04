import random


def find_pairs_with_sum(nums, target):
    seen = set()
    pairs = []
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

def user_list_inpunt():
   return input('Welcome to the pairs finders. Please, provide a list of integer numbers separated by a comma: ')

def user_target_input():
   return input('Please, now provide an integer number: ')

if __name__ == '__main__':
    user_list = user_list_inpunt()
    splitted_list = user_list.replace(' ', '').split(',')
    formatted_list = []

    while True:
      for item in splitted_list:
        try:
          int(item)
          formatted_list.append(int(item))
        except ValueError:
          print('Not all the items provided where integers. Please, try again')
          splitted_list = user_list_inpunt().split(',')
          break
      else:
        break

    while True:
        try:
            target_number = user_target_input()
            int(target_number)
            break
        except ValueError:
            print("That is not an integer. Please, try again.")

    result = find_pairs_with_sum(formatted_list, int(target_number))
    print(f'Here are the pairs that sum {target_number}: {result}')
 