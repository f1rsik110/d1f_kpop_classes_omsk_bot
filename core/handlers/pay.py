from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from core.settings import settings

import emoji


async def order_master_class(message: Message, bot: Bot):
    await message.answer(f'Чтобы купить мастер класс, нажмите на кнопку оплатить, которая находится ниже,'
                         f'там же вы можете ознакомитья с кратким описанием мастер-класса!')
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Мастер-класс',
        description='Разбираем танец',
        provider_token=settings.bots.pay_token,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к мастер-классу',
                amount=30000
            )
        ],
        max_tip_amount=50000,
        suggested_tip_amounts=[5000, 10000, 15000, 20000],
        start_parameter='nztcoder',
        photo_url='https://klike.net/uploads/posts/2020-03/1583661621_1.jpg',
        photo_size=100,
        photo_width=500,
        photo_height=500,
        need_name=True,
        need_email=True,
        need_phone_number=True,
        need_shipping_address=False,
        request_timeout=15,
        payload='Payment through a bot'
    )


async def order_subscribe(message: Message, bot: Bot):
    await message.answer(f'Чтобы купить абонемент, нажмите на кнопку оплатить, которая находится ниже,'
                         f'там же вы можете ознакомитья с кратким описанием абонемента!')
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Абонемент',
        description='Практикуемся и улучшаем навыки танцев',
        provider_token=settings.bots.pay_token,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к занятиям',
                amount=100000
            )
        ],
        max_tip_amount=50000,
        suggested_tip_amounts=[5000, 10000, 15000, 20000],
        start_parameter='nztcoder',
        photo_url='https://i.imgur.com/fXzrKNr.png',
        photo_size=100,
        photo_width=500,
        photo_height=500,
        need_name=True,
        need_email=True,
        need_phone_number=True,
        need_shipping_address=False,
        request_timeout=15,
        payload='Payment through a bo'
    )


async def pr_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def succesful_payment(message: Message):
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}' \
          f'\u2764\ufe0f.' \
          f'\n\nМы получили вашу заявку, приходите в указанное время в указанное место по расписанию.'
    await message.answer(msg)




