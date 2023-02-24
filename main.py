from config import token, group_token
from vk.sync import Vkinder
from bot.main import Bot
from vk_api.utils import enable_debug_mode

if __name__ == "__main__":
    vk_kinder = Vkinder(token)
    vk_bot = Bot(group_token, vk_kinder)
    enable_debug_mode(vk_bot.vk_session)
    vk_bot.loopLongPoll()