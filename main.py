from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token, group_token
from vk.sync import Vkinder

vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request.lower() == "привет":
                    write_msg(event.user_id, f"Хай, {event.user_id}")
                elif request.lower() == "пока":
                    write_msg(event.user_id, "Пока((")
                else:
                    write_msg(event.user_id, "Не поняла вашего ответа...")

if __name__ == "__main__":
    import pprint
    vkk = Vkinder(token)
    pprint.pprint(vkk.GetTopPhotos())
    main()