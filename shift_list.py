def do_shift_list(my_list, step):
    level = 1
    if step > len(my_list):
        step = step - len(my_list)

    for j in range(len(my_list)//step):
        for i in range(step):
            if i + step*level >= len(my_list):
                step_end = i + step*level - len(my_list)
            else:
                step_end = i + step*level
            my_list[i], my_list[step_end] = my_list[step_end], my_list[i]
        level += 1
    for i_sym in range(step_end+1, step - step_end):
        my_list[i_sym], my_list[step-step_end-1] = my_list[step-step_end-1], my_list[i_sym]

    return my_list


user_list = [0,1,2,3,4,5,6]
num_shift = 4

print('Список со сдвигом:', do_shift_list(user_list, num_shift))

