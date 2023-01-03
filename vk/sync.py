import random
import vk_api
from vk_api.utils import get_random_id

VK_VERSION = 5.89

class Vkinder:

    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token).get_api()

    def GetUsers(self, count, hometown, sex, status, age):
        """
        :param city:
        :param sex:
            1 — женщина,
            2 — мужчина,
            0 — любой (по умолчанию).
        :param status:
            1 — не женат (не замужем),
            2 — встречается,
            3 — помолвлен(-а),
            4 — женат (замужем),
            5 — всё сложно,
            6 — в активном поиске,
            7 — влюблен(-а),
            8 — в гражданском браке.
        :param age:
        :return:
        """
        users = self.vk.users.search(count=count, fields="education", hometown=hometown, sex=sex, status=status, age_from=age-1, age_to=age+1)
        return [u for u in users['items'] if not u['is_closed']]


    def GetUser(self, user_id):
        """
        [{'can_access_closed': False,
          'first_name': 'Юля',
          'id': 96513,
          'is_closed': True,
          'last_name': 'Иванова',
          'nickname': '',
          'photo_max_orig': 'https://sun3.userapi.com/sun3-13/s/v1/ig1/P82VOiJ2ayadwoli9vEsjDikPSwVpsLJ_IbJr--CHIuyaKmssTEDJAZhoE75gPkstp0mKZyA.jpg?size=400x400&quality=96&crop=1,126,1438,1438&ava=1',
          'sex': 1}]

        """
        return self.vk.users.get(user_ids=user_id,
                                fields="bdate, city, sex, country, nickname, photo_max_orig", v=VK_VERSION)


    def GetTopPhotos(self, user_id):
        """
        {'count': 1,
            'items': [{'album_id': -6,
            'date': 1489951718,
            'id': 456239031,
            'likes': {'count': 31, 'user_likes': 0},
            'owner_id': 8202,
            'post_id': 232,
            'reposts': {'count': 0},
            'sizes': [{'height': 130,
                       'type': 'y',
                       'url': 'https://sun9-west.userapi.com/sun9-4/s/v1/if1/TslcjJfrWnGYkmRSULO_L0RaETOATM_Kffru9HIqa-sgpM16FwSB5mPbD5F3wJ8w9RJ86qIf.jpg?size=616x715&quality=96&type=album',
                       'width': 616}],
            'square_crop': '98,58,493',
            'text': ''}]}

        """
        photos = self.vk.photos.getAll(owner_id=user_id, extended=1)['items']
        #list_of_photo_likes = zip(photos, [p.likes.count for p in photos])
        #max_likes = max(list_of_photo_likes, key=lambda l: l[1])
        return sorted(photos, key=lambda p: p['likes']['count'], reverse=True)[:3]