
calorie_list = []

if __name__ == "__main__":
    with open('./input.txt') as f:
        aggregate = 0
        for line in f.readlines():
            if line.strip().isdigit():
                aggregate += int(line.strip())
            else:
                calorie_list.append(aggregate)
                aggregate = 0

    calorie_list.sort(reverse=True)
    print(calorie_list[0] + calorie_list[1] + calorie_list[2])
