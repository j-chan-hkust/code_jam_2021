
#so with append sort, you can just take a greedy approach, very little thought is needed.
# for each element, you just find the minimum number that has same x number of digits,
# and find the difference in size.

def process_input(inputs):
    output = []
    for input in inputs:
        N, nums = input
        nums = [int(item) for item in nums.split(' ')]
        score = 0
        max = 0
        for num in nums:
            if num > max:
                max = num
                continue
            else:
                num *= 10
                score += 1
                if num>max:
                    max = num
                else:
                    while num<=max:
                        if max-num<=8:
                            num += max-num + 1
                        else:
                            num *= 10
                            score += 1
                    max = num


        output.append(score)
    return output


if __name__ == "__main__":
    T = int(input())
    inputs = []
    for _ in range(T):
        N = int(input())
        str = input()
        inputs.append([N, str])

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
