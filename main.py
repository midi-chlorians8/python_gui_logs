import os, sys

FILE_NAME = '../log.txt'

def create_file(FILE_NAME):
    isFile = os.path.isfile(f'./{FILE_NAME}')
    #print(isFile)

    if isFile == False:
        f = open(f"{FILE_NAME}", "w")
        f.write("Лог файл который поможет придти к целям. Каждый день сдесь будет дата и что сделано:\n")
        f.close()



from date import * #Тут берётся текушвя дата дня + проверка есть ли сегодня в списке



create_file(FILE_NAME)
#print ( is_date_exist(FILE_NAME, date_today()) )
if is_date_exist(FILE_NAME, date_today()) == False:
    f = open(f"{FILE_NAME}", "a")
    f.write(f"\nДата: {date_today()}. Что сделано:\n")
    f.write(f"Английский:\t\n")
    f.write(f"DevOps:\t\t\n")
    f.write(f"Python:\t\t\n")
    f.write(f"Tело:\t\t\n")
    f.close()

import time

while True:
    create_file(FILE_NAME)
    # print ( is_date_exist(FILE_NAME, date_today()) )
    if is_date_exist(FILE_NAME, date_today()) == False:
        f = open(f"{FILE_NAME}", "a")
        f.write(f"\nДата: {date_today()}. Что сделано:\n")
        f.write(f"Английский:\t\n")
        f.write(f"DevOps:\t\t\n")
        f.write(f"Python:\t\t\n")
        f.write(f"Tело:\t\t\n")
        f.close()
    #print(date_today())
    #print(now_time())
    time.sleep(60)