from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/ура')
button3 = types.KeyboardButton(text='/fox')
button4 = types.KeyboardButton(text='/лиса')
button5 = types.KeyboardButton(text='num')
button6 = types.KeyboardButton(text='/prof')

keybord =[
    [button1, button2],
    [button3, button4],
    [button5, button6]
]

kb = types.ReplyKeyboardMarkup(keyboard=keybord, resize_keyboard=True)
