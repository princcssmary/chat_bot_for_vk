import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

api = vk_api.VkApi(token='6a91d19e4e0182d0e56f37788f853a77be1824ce192be3bd311a5b3f8c357c4b46212e60964223477ca86')
longpoll = VkLongPoll(api)
vk = api.get_api()


def send_mess(id, text):
    api.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id

            if message == 'привет':
                send_mess(id, 'хелоу бро вотсап')

            elif message == 'начать':
                send_mess(id, 'Расписание какой группы Вы хотите получить?')


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
                send_mess(id, 'Введите день недели')

            elif message == 'понедельник' or message == 'вторник' or message == 'среда' \
                    or message == 'четверг' or message == 'пятница' or message == 'суббота':
                send_mess(id, 'погоди, тут еще ничего нет')

            else:
                send_mess(id, 'че?')

            CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')
            settings = dict(one_time=False, inline=True)
            keyboard_1 = VkKeyboard(**settings)
