def remover(arr, n):
    new_arr = arr[:]
    for i in range(n):
        new_arr.remove(max(new_arr))
        new_arr.remove(min(new_arr))
    return new_arr


user_numbers = [int(i) for i in input('Ввод цифирий через пробел => ').split()]

if len(user_numbers) < 4:
    print('Колличество цифирий меньше 4')
else:
    print(user_numbers, remover(user_numbers, 2))
 # В задаче не указано, как вводить кол-во n удаляемых элементов => я сделал просто 2
