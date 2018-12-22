#!/usr/bin/env python

def main():
    num_1, num_2, result = 1, 2, 0
    even_sum = 2
    while result <= 4000000:
        result = num_1 + num_2
        if result%2==0: even_sum+=result
        num_1 = num_2
        num_2 = result
    return even_sum

if __name__ == "__main__":
    print(main())
