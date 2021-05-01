def process_input(inputs):
    output = []
    for input in inputs:
        N, Q, x = input
        N = int(N)

        for y in x:
            answers, score = x

        output.append(score)
    return output


if __name__ == "__main__":
    T = int(input())
    inputs = []
    for _ in range(T):
        N, Q = input().split(' ')
        x=[]
        for _ in range(int(N)):
            str, score = input().split(' ')
            x.append([str,score])
        inputs.append([N, Q, x])

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
