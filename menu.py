import telegram
from key_buttons import tele_button, button, button1

def main_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(tele_button[0]),],
    [telegram.KeyboardButton(tele_button[1]),],
    [telegram.KeyboardButton(tele_button[2]),],
    [telegram.KeyboardButton(tele_button[3]),],
    [telegram.KeyboardButton(tele_button[4]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def makarons_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(button[0]),],
    [telegram.KeyboardButton(button[1]),],
    [telegram.KeyboardButton(button[2]),],
    [telegram.KeyboardButton(button[3]),],
    [telegram.KeyboardButton(button[4]),],
    [telegram.KeyboardButton(button[5]),],
    [telegram.KeyboardButton(button[6]),],
    [telegram.KeyboardButton(button[7]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def bento_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(button1[1]),],
    [telegram.KeyboardButton(button1[2]),],
    [telegram.KeyboardButton(button1[3]),],
    [telegram.KeyboardButton(button1[4]),],
    [telegram.KeyboardButton(button1[5]),],
    
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

