if __name__ == '__main__':
    name_score = []
    score_list = []

    for _ in range(int(input())):
        input_list = []
        name = input()
        score = float(input())
        input_list.append(name)
        input_list.append(score)
        name_score.append(input_list)
        score_list.append(score)

    score_list_sorted = list(set(score_list))
    score_list_sorted.sort()

    second_lowest_name = []
    for i in range(len(name_score)):
        if score_list_sorted[1] == name_score[i][1]:
            temp = name_score[i].pop(0)
            second_lowest_name.append(temp)

    second_lowest_name.sort()
    for i in second_lowest_name:
        print(i)