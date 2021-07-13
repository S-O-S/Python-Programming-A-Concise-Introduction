def problem2_8(temp_list):
    sum = 0
    max = temp_list[0]
    min = temp_list[0]
    for x in temp_list:
        sum+=x
        if x > max:
            max=x
        if x < min:
            min=x
    avg = sum / len(temp_list)
    print("Average:",avg)
    print("High:", max)
    print("Low:", min)