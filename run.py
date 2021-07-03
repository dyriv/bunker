from disaster import get_dis
from shelter import get_bunker
from player import write_card
from cleaner import clear_card, clear_bun, clear_dis

player_max = 99  # максимальное количество игроков


def runcode():
    while True:
        # узнаем количество играков
        players = input(f'\nВведите к-во играков от 6 до {player_max} >>> ')
        # удаляем файлы игры
        if players.lower() == 'c':
            clear_card(), clear_bun(), clear_dis()
            break
        # отмена начала игры
        if players.isdigit() and int(players) == 0:
            print('\nИгра отменена. Но Вы можете начать сначало. :(\n')
            break
        # начинаем игру
        if players.isdigit() and int(players) in range(6, ((player_max) + 1)):
            print('\nИгра сгенерирована. Приятной игры! :)\n')
            get_dis()
            get_bunker()
            write_card(players)
            break


if __name__ == '__main__':
    runcode()
