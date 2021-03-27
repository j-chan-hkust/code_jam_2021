
def process_input(inputs):
    output = []

    for input in inputs:
        T = int(input[0])
        C = int(input[1])

        min = T-1
        max = T*(T+1)/2 - 1

        if min <= C <= max:
            Cprime = C-T+1
            scores = []
            for i in reversed(range(T)):
                if Cprime == 0:
                    break
                elif i<=Cprime:
                    scores.append(i)
                    Cprime -= i
            out = list(range(1,T+1))
            print (scores)
        else:
            output.append("IMPOSSIBLE")



    return output


if __name__ == "__main__":
    n = int(input())
    inputs = []
    for _ in range(n):
        str = input()
        inputs.append(str.split(" "))

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
