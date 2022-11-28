import math

import SimpleRad as spr


def prompt():
    print("What is the value of A?")
    A = int(input())
    print("What is the value of B?")
    B = int(input())
    print("What is the value of C?")
    C = int(input())
    return A,B,C


def simplify_fraction(denominator, numerator1,numerator2):
    return math.gcd(denominator,numerator1,numerator2)


def whole_rad_result(num_in_root) -> bool:
    is_negative = False
    if num_in_root < 0:
        is_negative = True
        num_in_root = num_in_root * -1
    squared_num = math.sqrt(num_in_root)
    if squared_num.is_integer() == True and is_negative == False:
        return True, is_negative
    else:
        return False, is_negative


def calc_inside_radical(A,B,C) -> int:
    return (B**2-(4*A*C))


def main():
    A,B,C = prompt()
    inside_rad = calc_inside_radical(A,B,C)
    rad_result, is_negative = whole_rad_result(inside_rad)
    print("\n")
    if rad_result == True:
        if (-B + math.sqrt(inside_rad)) % (A*2) == 0:
            print(str(int((-B + math.sqrt(inside_rad)) / (A*2))))
        else:
            GCF = math.gcd(int(-B - math.sqrt(inside_rad)),A*2)
            print(str((-B + math.sqrt(inside_rad))/GCF) + "/" + str((A*2)/GCF))
        print(",")
        if (-B - math.sqrt(inside_rad)) % (A*2) == 0:
            print(str(int((-B - math.sqrt(inside_rad)) / (A*2))))
        else:
            GCF = math.gcd(int(-B - math.sqrt(inside_rad)),A*2)
            print(str((-B - math.sqrt(inside_rad))/GCF) + "/" + str((A*2)/GCF))
    else:
        whole_num, rad_num = spr.get_simple_root(inside_rad,2)
        GCF = simplify_fraction(A*2,whole_num,B)
        if is_negative == True:
            print("(" + str(int(-B/GCF)) + "±" + str(int(whole_num/GCF)) + "i" "√" + str(rad_num) + ")/" + str((A*2)/GCF))
        else:
            print("(" + str(int(-B/GCF)) + "±" + str(int(whole_num/GCF)) + "√" + str(rad_num) + ")/" + str((A*2)/GCF))


if __name__ == '__main__':
    main()