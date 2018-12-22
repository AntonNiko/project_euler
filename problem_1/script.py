#!/usr/bin/env python

def main():
    limit = 1000
    mult_sum = 0
    for i in range(1,limit):
        if i%5==0 or i%3==0:
            mult_sum+=i
    return mult_sum
        

if __name__ == "__main__":
    print(main())
