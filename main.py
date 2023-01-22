from config import token, group_token
from vk.sync import Vkinder
from bot.main import Bot
from vk_api.utils import enable_debug_mode
from datebase


if __name__ == "__main__":
    import pprint
    vk_kinder = Vkinder(token)
    vk_bot = Bot(group_token, vk_kinder)
    enable_debug_mode(vk_bot.vk_session)
    #
    # pprint.pprint(vkk.GetTopPhotos(vkk.GetUsers(count=1, hometown="Екатеринбург", status=1, sex=2, age=30)[0]['id']))
    vk_bot.loopLongPoll()