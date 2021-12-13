import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from itertools import islice

api = vk_api.VkApi(token='6a91d19e4e0182d0e56f37788f853a77be1824ce192be3bd311a5b3f8c357c4b46212e60964223477ca86')
longpoll = VkLongPoll(api)
vk = api.get_api()

list_of_key_words = ['привет', 'начать', '19 декабря', '26 декабря', '28 декабря', '29 декабря',
                     '30 декабря', '31 декабря', 'тс2001 13 декабря', 'тс2001 14 декабря', 'тс2001 15 декабря',
                     'тс2001 16 декабря', 'тс2001 17 декабря', 'тс2001 18 декабря', 'тс2001 20 декабря',
                     'тс2001 21 декабря', 'тс2001 22 декабря', 'тс2001 23 декабря', 'тс2001 24 декабря',
                     'тс2001 25 декабря', 'тс2001 27 декабря',
                     'тс2002 13 декабря', 'тс2002 14 декабря', 'тс2002 15 декабря',
                     'тс2002 16 декабря', 'тс2002 17 декабря', 'тс2002 18 декабря', 'тс2002 20 декабря',
                     'тс2002 21 декабря', 'тс2002 22 декабря', 'тс2002 23 декабря', 'тс2002 24 декабря',
                     'тс2002 25 декабря', 'тс2002 27 декабря',
                     'тс2004 13 декабря', 'тс2004 14 декабря', 'тс2004 15 декабря',
                     'тс2004 16 декабря', 'тс2004 17 декабря', 'тс2004 18 декабря', 'тс2004 20 декабря',
                     'тс2004 21 декабря', 'тс2004 22 декабря', 'тс2004 23 декабря', 'тс2004 24 декабря',
                     'тс2004 25 декабря', 'тс2004 27 декабря',
                                          'тс2003 13 декабря', 'тс2003 14 декабря', 'тс2003 15 декабря',
                     'тс2003 16 декабря', 'тс2003 17 декабря', 'тс2003 18 декабря', 'тс2003 20 декабря',
                     'тс2003 21 декабря', 'тс2003 22 декабря', 'тс2003 23 декабря', 'тс2003 24 декабря',
                     'тс2003 25 декабря', 'тс2003 27 декабря',
                                          'тс2005 13 декабря', 'тс2005 14 декабря', 'тс2005 15 декабря',
                     'тс2005 16 декабря', 'тс2005 17 декабря', 'тс2005 18 декабря', 'тс2005 20 декабря',
                     'тс2005 21 декабря', 'тс2005 22 декабря', 'тс2005 23 декабря', 'тс2005 24 декабря',
                     'тс2005 25 декабря', 'тс2005 27 декабря',
                     'тс2001 19 декабря', 'тс2001 26 декабря', 'тс2001 28 декабря', 'тс2001 29 декабря',
                     'тс2001 30 декабря', 'тс2001 31 декабря',
                     'тс2002 19 декабря', 'тс2002 26 декабря', 'тс2002 28 декабря', 'тс2002 29 декабря',
                     'тс2002 30 декабря', 'тс2002 31 декабря',
                     'тс2003 19 декабря', 'тс2003 26 декабря', 'тс2003 28 декабря', 'тс2003 29 декабря',
                     'тс2003 30 декабря', 'тс2003 31 декабря',
                     'тс2004 19 декабря', 'тс2004 26 декабря', 'тс2004 28 декабря', 'тс2004 29 декабря',
                     'тс2004 30 декабря', 'тс2004 31 декабря',
                     'тс2005 19 декабря', 'тс2005 26 декабря', 'тс2005 28 декабря', 'тс2005 29 декабря',
                     'тс2005 30 декабря', 'тс2005 31 декабря']

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

                if message == 'начать':
                    send_message(id, 'Расписание какой группы Вы хотите получить? '
                                     'Введите группу и дату (например, "Тс2001 14 декабря")')

                if 'тс2001 13 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[1:5]))
                elif 'тс2001 14 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[5:9]))
                elif 'тс2001 15 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[9:13]))
                elif 'тс2001 16 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[13:17]))
                elif 'тс2001 17 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[17:22]))
                elif 'тс2001 18 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[22:24]))
                elif 'тс2001 20 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[24:28]))
                elif 'тс2001 21 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[28:31]))
                elif 'тс2001 22 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[31:36]))
                elif 'тс2001 23 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[36:40]))
                elif 'тс2001 24 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[40:45]))
                elif 'тс2001 25 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[45:47]))
                elif 'тс2001 27 декабря' in message:
                    with open('2001.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[47:50]))


                if 'тс2002 13 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[1:6]))
                elif 'тс2002 14 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[7:11]))
                elif 'тс2002 15 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[11:14]))
                elif 'тс2002 16 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[14:18]))
                elif 'тс2002 17 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[18:22]))
                elif 'тс2002 18 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[22:24]))
                elif 'тс2002 20 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[24:29]))
                elif 'тс2002 21 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[29:31]))
                elif 'тс2002 22 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[33:36]))
                elif 'тс2002 23 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[36:41]))
                elif 'тс2002 24 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[41:46]))
                elif 'тс2002 25 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[46:48]))
                elif 'тс2002 27 декабря' in message:
                    with open('2002.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[48:52]))


                if 'тс2004 13 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[1:3]))
                elif 'тс2004 14 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[3:8]))
                elif 'тс2004 15 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[8:12]))
                elif 'тс2004 16 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[12:17]))
                elif 'тс2004 17 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[17:21]))
                elif 'тс2004 18 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[21:24]))
                elif 'тс2004 20 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[24:28]))
                elif 'тс2004 21 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[28:33]))
                elif 'тс2004 22 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[33:36]))
                elif 'тс2004 23 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[36:41]))
                elif 'тс2004 24 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[41:45]))
                elif 'тс2004 25 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[45:47]))
                elif 'тс2004 27 декабря' in message:
                    with open('2004.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[47:49]))

                if 'тс2003 13 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[1:4]))
                elif 'тс2003 14 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[4:9]))
                elif 'тс2003 15 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[9:13]))
                elif 'тс2003 16 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[13:18]))
                elif 'тс2003 17 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[18:23]))
                elif 'тс2003 18 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[23:25]))
                elif 'тс2003 20 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[25:30]))
                elif 'тс2003 21 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[30:35]))
                elif 'тс2003 22 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[35:40]))
                elif 'тс2003 23 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[40:45]))
                elif 'тс2003 24 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[45:48]))
                elif 'тс2003 25 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[48:50]))
                elif 'тс2003 27 декабря' in message:
                    with open('2003.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[50:55]))

                if 'тс2005 13 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[1:4]))
                elif 'тс2005 14 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[4:9]))
                elif 'тс2005 15 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[9:11]))
                elif 'тс2005 16 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[11:15]))
                elif 'тс2005 17 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[15:19]))
                elif 'тс2005 18 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[19:22]))
                elif 'тс2005 20 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[22:26]))
                elif 'тс2005 21 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[26:31]))
                elif 'тс2005 22 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[31:35]))
                elif 'тс2005 23 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[35:40]))
                elif 'тс2005 24 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[40:44]))
                elif 'тс2005 25 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[44:46]))
                elif 'тс2005 27 декабря' in message:
                    with open('2005.txt', 'r', encoding='utf-8') as file:
                        send_message(id, ''.join(file.readlines()[46:49]))


                if 'тс2001 19 декабря' in message or 'тс2001 26 декабря' in message\
                        or 'тс2002 19 декабря' in message or 'тс2002 26 декабря' in message\
                        or 'тс2003 19 декабря' in message or 'тс2003 26 декабря' in message\
                        or 'тс2004 19 декабря' in message or 'тс2004 26 декабря' in message\
                        or 'тс2005 19 декабря' in message or 'тс2005 26 декабря' in message:
                    send_message(id, 'Воскресенье. В этот день выходной.')

                if 'тс2001 28 декабря' in message or 'тс2001 29 декабря' in message or 'тс2001 30 декабря' in message\
                        or 'тс2002 28 декабря' in message or 'тс2002 29 декабря' in message or 'тс2002 30 декабря' in message\
                        or 'тс2003 28 декабря' in message or 'тс2003 29 декабря' in message or 'тс2003 30 декабря' in message\
                        or 'тс2004 28 декабря' in message or 'тс2004 29 декабря' in message or 'тс2004 30 декабря' in message\
                        or 'тс2005 28 декабря' in message or 'тс2005 29 декабря' in message or 'тс2005 30 декабря' in message:
                    send_message(id, 'День самоподготовки. С наступающим Новым Годом!')

                if 'тс2001 31 декабря' in message or 'тс2002 31 декабря' in message or 'тс2003 31 декабря' in message\
                        or 'тс2004 31 декабря' in message or 'тс2005 31 декабря' in message:
                    send_message(id, 'Пар нет. С Новым Годом!')

                
            else:
                send_message(id, 'Извините, я Вас не понимаю. Может, данные были введены некорректно?')
