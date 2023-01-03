import random

import requests
import vk_api
import random2
from config import token

randint_id = random.randint(1, 100000)
session = vk.Session(access_token=token)
vk_api = vk.API(session)

usr = vk_api.users.get(user_ids=randint_id,
                       fields="city, sex, country, nickname, photo_max_orig, mobile_phone", v=5.89)
fn = (usr[0]['first_name'] + ' ' + usr[0]['last_name'])
first_name = (usr[0]['first_name'])
last_name = (usr[0]['last_name'])
id_vk = (usr[0]['id'])
try:
    is_closed = (usr[0]['is_closed'])
except KeyError:
    is_closed = 2
try:
    city = (usr[0]["city"]['title'])
except KeyError:
    city = 'город скрыт настройками приватности =('
sex = (usr[0]["sex"])
if sex == 1:
         sex_pol = "Женский"
else:
         sex_pol = "Мужской"
try:
    coutry = (usr[0]['country']['title'])
except KeyError:
     coutry = 'Страна скрыта настройками приватности =('
try:
    nickname = (usr[0]["nickname"])
except KeyError:
    nickname = 'Никнейм отсутствует'
try:
    phnum = (usr[0]["mobile_phone"])
except KeyError:
    phnum = 'Телефон неизвестен'
try:
    avatar = (usr[0]["photo_max_orig"])
except KeyError:
    avatar = 'Фото отсутствует'
if is_closed == 0:
        pclose = 'Открыт'
if is_closed == 1:
        pclose = 'Закрыт'
if is_closed == 2:
        pclose = 'Страница заблокирована либо удалена'
print('Пользователь: ' + fn)
print('Имя ' + first_name)
print('Фамилия: ' + last_name)
print('Пол: ' + sex_pol)
print('Страна:', coutry)
print('Город', city)
print('Vk_id', id_vk)
print('Ссылка на профиль: ' + 'https://vk.com/id' + str(id_vk))
print('Никнейм:', nickname)
print('Профиль:', pclose)
print('Аватарка', avatar)
print('Мобильный', phnum)