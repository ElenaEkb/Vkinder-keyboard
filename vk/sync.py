import random
import vk_api
from vk_api.utils import get_random_id

VK_VERSION = 5.89

class Vkinder:

    def __init__(self, token):
        self.vk = vk_api.VkApi(token=token).get_api()

    def GetUsers(self):
        return self.vk.users.get(user_ids=random.randint(1, 100000),
                                fields="city, sex, country, nickname, photo_max_orig", v=VK_VERSION)