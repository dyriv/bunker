# удаляем старые файлы игры перед генерацией новых

from os import listdir, remove, path

clear_dir = 'data/'  # путь к файлам


def clear_dis():  # удаляем файл с катастрофой
    try:
        filelist = [f for f in listdir(clear_dir)]  # добавляем все файлы из директории в список
        for f in filelist:  # для файла с названием disaster.txt удаляем его
            if f == 'disaster.txt':
                remove(path.join(clear_dir, f))  # удаляем файл
    except:
        pass


def clear_bun():  # удаляем файл с описанием бункера
    try:
        filelist = [f for f in listdir(clear_dir)]
        for f in filelist:
            if f == 'shelter.txt':
                remove(path.join(clear_dir, f))
    except:
        pass


def clear_card():  # удаляем файлы с характеристиками персонажей
    try:
        filelist = [f for f in listdir(clear_dir)]
        for f in filelist:
            if f != 'disaster.txt' and f != 'shelter.txt':
                remove(path.join(clear_dir, f))
    except:
        pass
