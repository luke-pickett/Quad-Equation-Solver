prime_numbers = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
    223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
]

multiplicative_nums = []



def check_if_prime(num) -> bool:
    for x in prime_numbers:
        if num == x:
            return True
    return False


def multiply_list(list) -> int:
    result = 1
    for x in list:
        result = result * x
    return result


def find_pairs(pair_num, list):
    root_num = 1
    whole_num = 1
    unique_nums = set(list)
    count_dictionary = {}
    for x in unique_nums:
        count_dictionary[x] = list.count(x)

    for number in count_dictionary:
        count = count_dictionary[number]
        if count >= pair_num:
            groups = count // pair_num
            remainder = count % pair_num
            if groups > 0:
                whole_num *= (groups * number)
            if remainder > 0:
                root_num *= (remainder * number)
        else:
            root_num *= (number ** count)

    return whole_num, root_num



mult_list = []


def get_roots(num):
    lowest_prime = None
    for x in prime_numbers:
        is_divisible = num % x == 0
        if is_divisible:
            lowest_prime = x
            break
    if lowest_prime:
        mult_list.append(lowest_prime)
        get_roots(num / lowest_prime)

def get_simple_root(wanted_num,wanted_root):
    mult_list.clear()

    get_roots(wanted_num)
    return find_pairs(wanted_root, mult_list)