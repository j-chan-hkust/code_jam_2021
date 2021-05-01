
from collections import Counter
from itertools import combinations
from operator import mul
from functools import reduce
from numpy import dot


def process_input(inputs):
    output = []
    for input in inputs:
        m, primes = input

        #sum primes
        sum_prime = 0
        prime_list = []
        for prime in primes:
            p, f = prime
            p = int(p)
            f = int(f)
            sum_prime += p*f
            for _ in range(f):
                prime_list.append(p)
        previous_solutions = set()
        max=0
        for i in range(len(prime_list)):
            for combination in combinations(prime_list, i+1):
                product = reduce(mul, combination, 1)
                if product>sum_prime:
                    continue #this is an obvious bad option, we skip
                elif product in previous_solutions:
                    continue #we've already explored it
                else:
                    c1 = Counter(prime_list)
                    c2 = Counter(combination)

                    diff = c1 - c2

                    if dot(list(diff.values()), list(diff.keys()))==product:
                        if product>max:
                            max = product

                    previous_solutions.add(product)
        output.append(max)

    return output


if __name__ == "__main__":
    T = int(input())
    inputs = []
    for _ in range(T):
        N = int(input())
        x = []
        for _ in range(N):

            str = input().split(' ')
            x.append(str)
        inputs.append([N,x])

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
