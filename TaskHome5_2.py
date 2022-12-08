# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

# для победы над конкурентном первый, тот кто ходит, должен взять остаток от деления на 29 т.е. 2021 % 29 = 20 конфет 
# и далее брать % 29 от оставшегося количества конфет;
# возможен перехват инициацитивы, если 1-й игрок ошибется 

candies_play = 2021

max_cond_pl = 28

if randint(1, 2) == 1: 
    print('Начинает бот с ИИ')
    while candies_play > 0:
        print(f'Бот с ИИ взял {candies_play % (max_cond_pl + 1)} конфет') 
        candies_play = candies_play - candies_play % (max_cond_pl + 1)
        if candies_play == 0:
            print('Бот c ИИ победил')
            break
        print(f'Остаток конфет {candies_play}')
        cand_player = randint(1, (max_cond_pl))
        print(f'Игрок взял {cand_player} конфет')
        candies_play = candies_play - cand_player
        print(f'Остаток конфет {candies_play} конфет')
else:
    print('Начинает игрок')
    while candies_play > 0:
        cand_player = randint(1, (max_cond_pl))
        print(f'Игрок взял {cand_player} конфет')
        candies_play = candies_play - cand_player
        print(f'Остаток конфет {candies_play}')
        if candies_play == 0:
            print('Игрок победил')
            break
        if cand_player == candies_play % (max_cond_pl + 1) and candies_play == candies_play - (candies_play % (max_cond_pl + 1)):
            bot_II = randint(1, (max_cond_pl))
            print(f'Бот с ИИ взял {bot_II} конфет')
            candies_play = candies_play - bot_II
            print(f'Остаток конфет {candies_play}')
        else:
            print(f'Бот с ИИ взял {candies_play % (max_cond_pl + 1)} конфет') 
            candies_play = candies_play - candies_play % (max_cond_pl + 1)
            if candies_play == 0:
                print('Бот с ИИ победил')
                break