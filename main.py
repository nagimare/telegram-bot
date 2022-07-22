
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import(
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import main_menu_keyboard, makarons_menu_keyboard, bento_menu_keyboard
from key_buttons import tele_button, button, button1



    
     

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFQIdizV_NclIYlEnnBEcEzp-JTyPQqQACl2sBAAFji0YM9zWUj0LtHospBA'
    )
    update.message.reply_text(
        "Добро пожаловать, {username}".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )



ABOUT_US = r"(?=("+(tele_button[0])+r"))"
WHERE_WE = r"(?=("+(tele_button[1])+r"))"
MAKARONS = r"(?=("+(tele_button[2])+r"))"
BENTO = r"(?=("+(tele_button[3])+r"))"
ZAKAZ = r"(?=("+(tele_button[4])+r"))"


FM_KEY = r"(?=("+(button[0])+r"))"
PLOM_KEY = r"(?=("+(button[1])+r"))"
KK_KEY = r"(?=("+(button[2])+r"))"
CK_KEY = r"(?=("+(button[3])+r"))"
GS_KEY = r"(?=("+(button[4])+r"))"
CHK_KEY = r"(?=("+(button[5])+r"))"
SHN_KEY = r"(?=("+(button[6])+r"))"
BACK_KEY = r"(?=("+(button[7])+r"))"


MISHKA_KEY = r"(?=("+(button1[0])+r"))"
CLOUD_KEY = r"(?=("+(button1[1])+r"))"
HEARD_KEY = r"(?=("+(button1[2])+r"))"
AVOKADO_KEY = r"(?=("+(button1[3])+r"))"
KRUJOK_KEY = r"(?=("+(button1[4])+r"))"
BACK = r"(?=("+(button1[5])+r"))"




# def zakazat(update: Update, context:CallbackContext):
#     z = update.message.text
#     print(z[:8])
#     if z[:8] == 'Заказать:':
#         context.bot.send_message(
#             chat_id = '@makaronkg', 
#             text = z
#         )

def zapisat(update: Update, context:CallbackContext):
    z = update.message.text
    print(z[:6])
    if z[:6] == 'Запись':
        context.bot.send_message(
            chat_id = '@makaronkg', 
            text = z
        )

def zakaz(update: Update, context:CallbackContext):
    info=re.match(ZAKAZ, update.message.text)
    update.message.reply_text(
        text = """
1. Напишите сообщение  с "Запись: " и ваше имя.
2.  Ваш номер телефона
3. Выберите время удобный вам.
! После отправки всех заполненных бланок Админ вам позвонит.:)
"""
    )     


def resive_info(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of Street Baker'
    )

    update.message.reply_location(
        # 42.853807, 74.602295
        longitude= 74.602295,
        latitude= 42.853807,
        reply_to_message_id=msg.message_id
    )


def inform_makarons_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=""" 
    
    Первая макаронная в Кыргызстане
    Говорят, они вызывают зависимость
    За год испекли более 650 000 макарон


    """
    )
    
    reply_markup=makarons_menu_keyboard()
     









# def Back_menu(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         'Вернулись назад',
#         reply_markup=main_menu_keyboard()
#     )

def resive_makarons_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите макаронс',
        reply_markup=makarons_menu_keyboard()
    )


def resive_bento_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите бенто-тортик',
        reply_markup=bento_menu_keyboard()
    )

def FM_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='fm_makarons'),
        InlineKeyboardButton('Price', callback_data='fm_price'),
        ]

    ]


    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )

def PLOM_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='plom_makarons'),
        InlineKeyboardButton('Price', callback_data='plom_price'),
        ]

    ]


    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )

    
def KK_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='kk_makarons'),
        InlineKeyboardButton('Price', callback_data='kk_price'),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )


def CK_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='ck_makarons'),
        InlineKeyboardButton('Price', callback_data='ck_price'),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )

def GS_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='gs_makarons'),
        InlineKeyboardButton('Price', callback_data='gs_price'),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )


def CHK_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='chk_makarons'),
        InlineKeyboardButton('Price', callback_data='chk_price'),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )


def SHN_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton('Makapons', callback_data='shn_makarons'),
        InlineKeyboardButton('Price', callback_data='shn_price'),
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )


def Back_menu1(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вернулись назад',
        reply_markup=main_menu_keyboard()
    )


    # reply_markup = InlineKeyboardMarkup(keyboard)
    # update.message.reply_text(
    # ' Выберите опцию',
    # reply_markup=reply_markup
    # )





def mishka_inline_menu(update: Update, context: CallbackContext):
    keyboard1 = [
        [
        InlineKeyboardButton('Bento', callback_data='mishka_bento'),
        InlineKeyboardButton('Price', callback_data='mishka_price'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard1)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )


def cloud_inline_menu(update: Update, context: CallbackContext):
    keyboard1 = [
        [
        InlineKeyboardButton('Bento', callback_data='cloud_bento'),
        InlineKeyboardButton('Price', callback_data='cloud_price'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard1)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )

def heard_inline_menu(update: Update, context: CallbackContext):
    keyboard1 = [
        [
        InlineKeyboardButton('Bento', callback_data='heard_bento'),
        InlineKeyboardButton('Price', callback_data='heard_price'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard1)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )


def avokada_inline_menu(update: Update, context: CallbackContext):
    keyboard1 = [
        [
        InlineKeyboardButton('Bento', callback_data='avokada_bento'),
        InlineKeyboardButton('Price', callback_data='avokada_price'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard1)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )

def krujok_inline_menu(update: Update, context: CallbackContext):
    keyboard1 = [
        [
        InlineKeyboardButton('Bento', callback_data='krujok_bento'),
        InlineKeyboardButton('Price', callback_data='krujok_price'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard1)
    update.message.reply_text(
    ' Выберите опцию',
    reply_markup=reply_markup
    )

def Back_menu2(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вернулись назад',
        reply_markup=main_menu_keyboard()
    )



def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'fm_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/5.jpe', 'rb'),
            caption = """
 'Фисташка-малина'

            """
        )

    if query.data == 'fm_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som 
                """
            )


    query = update.callback_query
    if query.data == 'plom_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/6.jpe', 'rb'),
            caption = """
'Пломбир'

            """
        )

    if query.data == 'plom_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som
                """
            )


    query = update.callback_query
    if query.data == 'kk_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/1.jpe', 'rb'),
            caption = """
 'Криспи-карамель'

            """
        )

    if query.data == 'kk_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som
                """
            )


    query = update.callback_query
    if query.data == 'ck_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/3.jpe', 'rb'),
            caption = """
 'Сникерс'

            """
        )

    if query.data == 'ck_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som
                """
            )

            
    query = update.callback_query
    if query.data == 'gs_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/4.jpe', 'rb'),
            caption = """
 'Голубика-смородина'

            """
        )
    if query.data == 'gs_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som
                """
            )
            
    query = update.callback_query
    if query.data == 'chk_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/2.jpe', 'rb'),
            caption = """
 'Чизкейк-клубника'

            """
        )

    if query.data == 'chk_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som
                """
            )

    query = update.callback_query
    if query.data == 'shn_makarons':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/7.jpe', 'rb'),
            caption = """
 'Шоколад-нутелла'

            """
        )

    if query.data == 'shn_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  180som
                """
            )

    if query.data == 'mishka_bento':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/12.jpe', 'rb'),
            caption = """
 'Мишка'

            """
        )

    if query.data == 'mishka_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  1300som 
                """
            )


    
    if query.data == 'cloud_bento':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/10.jpe', 'rb'),
            caption = """
 'Облачко'

            """
        )

    if query.data == 'cloud_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  1300som 
                """
            )


    
    if query.data == 'heard_bento':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/9.jpe', 'rb'),
            caption = """
 'Сердечко'

            """
        )

    if query.data == 'heard_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  1300som 
                """
            )


    
    if query.data == 'avokada_bento':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/8.jpe', 'rb'),
            caption = """
 'Авокада'

            """
        )

    if query.data == 'avokada_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  1300som 
                """
            )


   
    if query.data == 'krujok_bento':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/11.jpe', 'rb'),
            caption = """
 'Кружок'

            """
        )

    if query.data == 'krujok_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
  1300som 
                """
            )



updater = Updater(TOKEN,persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT_US),
    inform_makarons_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(WHERE_WE),
    resive_info
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MAKARONS),
    resive_makarons_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(FM_KEY),
    FM_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PLOM_KEY),
    PLOM_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KK_KEY),
    KK_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CK_KEY),
    CK_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GS_KEY),
    GS_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CHK_KEY),
    CHK_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SHN_KEY),
    SHN_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_KEY),
    Back_menu1
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BENTO),
    resive_bento_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MISHKA_KEY),
    mishka_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CLOUD_KEY),
    cloud_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(AVOKADO_KEY),
    avokada_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HEARD_KEY),
    heard_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KRUJOK_KEY),
    krujok_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAKAZ),
    zakaz
))



updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    Back_menu2
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
    ))


updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()









