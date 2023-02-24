"""Создание бота Vkinder"""
import vk_api
VK_VERSION = 5.89


class Vkinder:
    """Объект Vkinder"""
    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token).get_api()

    def getUsers(self, count, hometown, sex, status, age):
        """Поиск пользователя по параметрам"""
        users = self.vk.users.search(count=count, fields="education",
                                     hometown=hometown, sex=sex,
                                     status=status, age_from=age-1,
                                     age_to=age+1)
        return [u for u in users['items'] if not u['is_closed']]

    def getUser(self, user_id):
        """Информация о пользователе"""
        return self.vk.users.get(user_ids=user_id,
                                 fields="bdate, city, sex, "
                                        "country, "
                                        "nickname, photo_max_orig",
                                 v=VK_VERSION)

    def getTopPhotos(self, user_id):
        """Поиск фото пользователя"""
        photos = self.vk.photos.getAll(owner_id=user_id, extended=1)['items']
        return sorted(photos, key=lambda p: p['likes']['count'],
                      reverse=True)[:3]
