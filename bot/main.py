import pprint
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

class Bot:

    def __init__(self, token, kinder):
        self.vk_session = vk_api.VkApi(token=token)
        self.kinder = kinder

    def write_msg(self, user_id, message):
        self.vk_session.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': get_random_id(),})


    def getSerachSex(self, sex):
        if sex == 1:
            return 2
        elif sex == 2:
            return 1
        else:
            return 0

    def loopLongPoll(self):
        user = {}
        for event in VkLongPoll(self.vk_session).listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text
                    if request.lower() == "привет":
                        user[event.user_id] = self.kinder.GetUser(event.user_id)[0]
                        #pprint.pprint(user[event.user_id])
                        self.write_msg(event.user_id, f"Хай, {user[event.user_id]['first_name']}. Введите возраст?")
                    elif request.isnumeric():
                        # Todo обработать исключения KeyError не ввели привет
                        friends = self.kinder.GetUsers(
                            count=1, status=1,
                            hometown=user[event.user_id]['city']['title'],
                            sex=self.getSerachSex(user[event.user_id]['sex']),
                            age=int(request))
                        #pprint.pprint(friends)
                        if len(friends) == 0:
                            self.write_msg(event.user_id,f"Нет подходящих кандидатур по вашему запросу. Введите другой возраст")
                            continue
                        friend_id = friends[0]['id']
                        photos = self.kinder.GetTopPhotos(friend_id)
                        #pprint.pprint(photos)
                        msg = f"Нашел друга https://vk.com/id{friend_id}, \nФото"
                        for photo in photos:
                            photo_url = max(photo['sizes'], key=lambda p: p['height'])['url']
                            msg = f"{msg} {photo_url}"

                        self.write_msg(event.user_id, msg)
                    elif request.lower() == "пока":
                        self.write_msg(event.user_id, "Пока((")
                    else:
                        self.write_msg(event.user_id, "Не поняла вашего ответа...")
