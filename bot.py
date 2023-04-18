from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.filters import Command

from core.settings import settings
from core.handlers.basic import get_start, get_photo, get_schedule, get_subscription, get_notiflication, get_master_class, get_kontakts, get_help, get_inf_subscription, get_inf_master_classes
from core.handlers.pay import order_master_class, pr_checkout_query, succesful_payment, order_subscribe

import asyncio
import logging
import emoji


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher(bot=bot)
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_start, F.text == 'Назад \u21a9\ufe0f')
    dp.startup.register(start_bot)
    dp.message.register(order_master_class, F.text == emoji.emojize('Купить мастер-класс :credit_card:'))
    dp.message.register(order_subscribe, F.text == emoji.emojize('Купить абонемент :credit_card:'))
    dp.pre_checkout_query.register(pr_checkout_query)
    dp.message.register(succesful_payment, F.content_type == ContentType.SUCCESSFUL_PAYMENT)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_schedule, F.text == emoji.emojize('Расписание :tear-off_calendar:'))
    dp.message.register(get_subscription, F.text == '\u2728 Абонемент \u2728')
    dp.message.register(get_master_class, F.text == emoji.emojize(':collision: Мастер-класс :collision:'))
    dp.message.register(get_notiflication, F.text == '\U0001f514')
    dp.message.register(get_kontakts, F.text == emoji.emojize("Контакты :open_book:"))
    dp.message.register(get_help, F.text == 'Помощь')
    dp.message.register(get_inf_subscription, F.text == 'Об абонементе')
    dp.message.register(get_inf_master_classes, F.text == 'Об мастер-классах')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

