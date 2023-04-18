from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import emoji

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text=emoji.emojize('Расписание :tear-off_calendar:')
        ),
    ],
    [
        KeyboardButton(
            text='\u2728 Абонемент \u2728'
        ),
        KeyboardButton(
            text=emoji.emojize(':collision: Мастер-класс :collision:')
        ),
    ],
    [
        KeyboardButton(
            text=emoji.emojize("Контакты :open_book:")
        ),
        KeyboardButton(
            text='Помощь'
        ),
        KeyboardButton(
            text='\U0001f514'
        ),
    ],
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выберите кнопку ↓')

schedule_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='По абонементу'
        ),
        KeyboardButton(
            text='По матер-классам'
        )
    ],
    [
        KeyboardButton(
            text='Назад \u21a9\ufe0f'
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выберите кнопку ↓')

subscription_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text=emoji.emojize('Купить абонемент :credit_card:')
        ),
    ],
    [
        KeyboardButton(
            text='Об абонементе'
        ),
        KeyboardButton(
            text='Ещё чето тута :p'
        )
    ],
    [
        KeyboardButton(
            text='Назад \u21a9\ufe0f'
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выберите кнопку ↓')

master_class_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text=emoji.emojize('Купить мастер-класс :credit_card:')
        ),
    ],
    [
        KeyboardButton(
            text='Об мастер-классах'
        ),
        KeyboardButton(
            text='Ещё чето тута :p'
        )
    ],
    [
        KeyboardButton(
            text='Назад \u21a9\ufe0f'
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выберите кнопку ↓')

notification_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text= 'Вкл. \ud83d\udd14'
        ),
        KeyboardButton(
            text= 'Выкл. \ud83d\udd14'
        ),
    ],
    [
        KeyboardButton(
            text='Назад \u21a9\ufe0f'
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выберите кнопку ↓')


