import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from itertools import islice

api = vk_api.VkApi(token='6a91d19e4e0182d0e56f37788f853a77be1824ce192be3bd311a5b3f8c357c4b46212e60964223477ca86')
longpoll = VkLongPoll(api)
vk = api.get_api()

list_of_key_words = ['привет', 'начать', 'тс2101', 'тс2102', 'тс2103', 'тс2104', 'тс2001', 'тс2002',
                     'тс2003', 'тс2004', 'тс2005', 'тс1901', 'тс1902', 'тс1903', 'тс1904', 'тс1801',
                     'тс1802', 'тс1803', 'тс1804', 'тс1701', 'тс1702', 'тс1703', 'тс1704', 'ПИб2101',
                     'ПИб2001', '13 декабря', '14 декабря', '15 декабря', '16 декабря', '17 декабря',
                     '18 декабря', '19 декабря', '20 декабря', '21 декабря', '22 декабря', '23 декабря',
                     '24 декабря', '25 декабря', '26 декабря', '27 декабря', '28 декабря', '29 декабря',
                     '30 декабря', '31 декабря', 'мозолева']

def send_message(id, text):
    api.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id

            if message in list_of_key_words:
                if message == 'привет':
                    send_message(id, 'хелоу бро вотсап')

                elif message == 'начать':
                    send_message(id, 'Расписание какой группы Вы хотите получить? Если Вы преподаватель, введите свою фамилию')

                elif message == 'тс2101' or message == 'тс2102' \
                        or message == 'тс2103' or message == 'тс2104' \
                        or message == 'тс2001' or message == 'тс2002' or message == 'тс2003' \
                        or message == 'тс2004' or message == 'тс2005'\
                        or message == 'тс1901' or message == 'тс1902'\
                        or message == 'тс1903' or message == 'тс1904'\
                        or message == 'тс1801' or message == 'тс1802'\
                        or message == 'тс1803' or message == 'тс1804'\
                        or message == 'тс1701' or message == 'тс1702'\
                        or message == 'тс1703' or message == 'тс1704'\
                        or message == 'ПИб2101' or message == 'ПИб2001':
                    send_message(id, 'Введите дату (например, "13 декабря")')

                elif message == 'мозолева':
                    send_message(id, 'Введите дату (например, "13 декабря")')

                elif '13 декабря' in message or '14 декабря' in message \
                        or '19 декабря' in message or '21 декабря' in message \
                        or '24 декабря' in message or '25 декабря' in message \
                        or '26 декабря' in message or '27 декабря' in message \
                        or '28 декабря' in message or '29 декабря' in message \
                        or '30 декабря' in message or '31 декабря' in message :
                    send_message(id, 'В этот день пар нет. С наступающим Новым Годом!')

                # elif '15 декабря' in message:
                #     send_message(id, 'Пара 2' + '\n' + 'Тс2004' + '\n' + '10:10 - 11:40' + '\n' + 'ауд. 405' + '\n'
                #               + 'Организация и техника внешнеторговых операций (пр.зан.)' + '\n' + ' ' + '\n' + 'Пара 3' + '\n'
                #               + 'Тс01/1803' + '\n' + '12:30 - 13:50' + '\n' + 'ауд. 405' + '\n'
                #               + 'ЗАЧЕТ Международная цепь поставок' + '\n' + ' ' + '\n'
                #               + 'Пара 4' + '\n' + 'Тс02/1802' + '\n' + '14:00 - 15:30' + '\n' + 'ауд. 509' + '\n'
                #               + 'ЗАЧЕТ Международная цепь поставок' + '\n' + ' ' + '\n' + 'Тс2004' + '\n'
                #               + '10:10 - 11:40' + '\n' + 'ауд. 405' + '\n'
                #               + 'Организация и техника внешнеторговых операций (пр.зан.)')

                elif '15 декабря' in message:
                    with open('mozoleva.txt', 'r', encoding='utf-8') as file:
                        send_message(id, file.readlines()[2])


                elif message == 'понедельник' or message == 'вторник' or message == 'среда' \
                        or message == 'четверг' or message == 'пятница' or message == 'суббота':
                    send_message(id, 'погоди, тут еще ничего нет')
            else:
                send_message(id, 'Извините, я Вас не понимаю. Может, данные были введены некорректно?')
