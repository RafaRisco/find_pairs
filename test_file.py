import random
import timeit


from find_pairs import find_pairs_with_sum

def random_test_list_generator(size):
  random_list = [random.randint(-10000,1000000) for i in range(0,size)]
  return list(set(random_list))

def test_results():
    provided_list = [1,9,5,0,20,-4,12,16,7]
    test_results = find_pairs_with_sum(provided_list, 12)
    assert {(12, 0), (16, -4), (7, 5)} == set(test_results)

def test_all_results_valid():
    generated_list = random_test_list_generator(100000)
    test_results = find_pairs_with_sum(generated_list, 12)
    my_testing_list = [True if item[0] + item[1] else False for item in test_results]
    assert True == all(my_testing_list)

def test_execution_time():
    random_list = random_test_list_generator(100000)
    tiempo = timeit.timeit(lambda: find_pairs_with_sum(random_list, 12), number=1000)
    assert tiempo / 1000 < 0.2
