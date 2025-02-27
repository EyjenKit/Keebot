import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Твой сервисный ключ доступа
TOKEN = "a515cd91a515cd91a515cd91c9a6371a1aaa515a515cd91c23df30cf49b4824ee31b871"

# Авторизация в API ВКонтакте
vk_session = vk_api.VkApi(token="1g3CArHI5Z6yZhthe8nu")
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def send_message(user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=0)

print("Бот запущен!")

# Основной цикл обработки сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id

        if user_message == "привет":
            send_message(user_id, "Привет! Как я могу помочь?")
        else:
            send_message(user_id, "Я пока не понимаю это сообщение, но я учусь!")
