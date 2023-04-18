from aiogram import Bot
from aiogram.types import Message

from core.keyboards.reply import start_keyboard, schedule_keyboard, subscription_keyboard, notification_keyboard, \
    master_class_keyboard


async def get_start(message: Message, bot: Bot):
    if message.text == "/start":
        await message.answer(f'Привет, {message.from_user.first_name}.\n\n'
                             f'Рад тебя видеть!',
                             reply_markup=start_keyboard)
        await message.delete()
    elif message.text == 'Назад \u21a9\ufe0f':
        await message.answer(f'Вы вернулись в главное меню', reply_markup=start_keyboard)


async def get_schedule(message: Message, bot: Bot):
    await message.answer(f'Выберите пунк, по которому вы хотите узнать расписание',
                         reply_markup=schedule_keyboard)


async def get_master_class(message: Message, bot: Bot):
    await message.answer(f'Что именно вы хотите сделать?',
                         reply_markup=master_class_keyboard)


async def get_notiflication(message: Message, bot: Bot):
    await message.answer(f'У вас уведомеления (тут будет выкл или вкл)',
                         reply_markup=notification_keyboard)


async def get_subscription(message: Message, bot: Bot):
    await message.answer(f'Что именно вы хотите сделать?',
                         reply_markup=subscription_keyboard)


async def get_kontakts(message: Message, bot: Bot):
    await message.answer(f'Контакты создателя бота и тренера:\n\n'
                         f'\U0001f4f1 Номер телефона: 880055535\n'
                         f'\U0001f4e7 Почта: swdas@mail.ru\n\n'
                         f'\U0001f3ec Место провдения занятий:\n'
                         f'ул.Пушикна, д.Калатушкино')


async def get_help(message: Message, bot: Bot):
    await message.answer(f'Если у вас возникли какие-то проблемы по поводу оплаты или нестабильной работы бота, обратитесь, пожалуйста, на почту:\n'
                         f'\U0001f4e7 Почта: swdas@mail.ru\n\n'
                         f'Или обратитесь за помощью в телеграмме:\n'
                         f'@d1f_help')


async def get_inf_subscription(message: Message, bot: Bot):
    await message.answer(f'Подробная ифнормация об абонименте:\n\n'
                         f'Абонемент-это блаблаблабла....\n\n'
                         f'В абонементе постоянных 8 занятий по 2 часа, которые зафиксированы в зале, поэтому отменить их не получится.\n\n'
                         f'Цена: 2800руб.')


async def get_inf_master_classes(message: Message, bot: Bot):
    await message.answer(f'Подробная ифнормация об мастер-классах:\n\n'
                         f'Мастер-класс -это блаблаблабла....\n\n'
                         f'В матсер-класс входит 1 занятие, где мы разбираем кусок выбранного танца, опрос проводится у нас в тг канале (@d1f_непридумалеще).\n\n'
                         f'Цена: 300руб.')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Спасибо за картинку :3')
