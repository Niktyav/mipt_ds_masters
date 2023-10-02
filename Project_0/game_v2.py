"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np



def binary_predict(number: int = 1) -> int:
    
    """угадываем число бинарным поиском
       подробнее о методе: 
            https://ru.wikipedia.org/wiki/Двоичный_поиск
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    #счетчик попыток
    count = 0
    #максимальное значение 
    high = 100
    #минимальное значение
    low = 0 
    #среднее, которым ищем
    
    
    while low<=high:
        count += 1   
        #делим промежуток пополам   
        mid = (high+low)//2  
        if number == mid:
            break# выход из цикла, если угадали    
        elif mid > number:#иначе смотрим как сократить интервал
            high = mid- 1
        else:    
            low = mid+ 1
    return count


def score_game(func_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        func_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    print(score_game(binary_predict))
