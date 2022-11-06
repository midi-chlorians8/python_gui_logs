
import datetime as dt
def date_today():
    now = dt.datetime.utcnow()
    moscow_now = now + dt.timedelta(hours=3)
    #print(f'Я пишу этот код в {moscow_now.strftime("%d-%m-%Y")} по московскому времени')
    return moscow_now.strftime("%d-%m-%Y")

def now_time():
    return dt.datetime.utcnow()

#Читаем посдежнюю лог запись. Сверяем её с сеголняшним днём. Если нету то вернуть true.
def is_date_exist(file, today):
    f = open(file)
    is_data_in_list = False
    for line in f:

        if line.find("Дата") == 0:
            #print(line)
            data_s = line.split()[1]
            data = data_s[:-1]

            #print (f'data:{data}')
            #print(f'today:{today}')
            if data == today:
                is_data_in_list = True
            else:
                is_data_in_list = False
    f.close()
    return is_data_in_list