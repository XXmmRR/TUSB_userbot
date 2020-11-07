from pyrogram.errors import FloodWait
from time import time
from pyrogram.errors import MessageEmpty
from time import sleep
from random import randint
from pyowm import OWM
import os
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from filter import Filter

app = Client("my_account")
owm = OWM('17c13f27c44dbe3359f65d3b5499a704')

REPLACEMENT_MAP = {
    "я": "ʁ",
    "ю": "oı",
    "э": "є",
    "ъ": "q",
    "ы": "ıq",
    "ь": "q",
    "щ": "m",
    "ш": "m",
    "ч": "Һ",
    "ц": "ǹ",
    "х": "х",
    "ф": "ȸ",
    "у": "ʎ",
    "т": "⊥",
    "с": "ɔ",
    "р": "d",
    "п": "u",
    "о": "о",
    "н": "н",
    "м": "w",
    "л": "v",
    "к": "ʞ",
    "й": "и",
    "и": "и",
    "з": "є",
    "ж": "ж",
    "ё": "ǝ",
    "е": "ǝ",
    "д": "6",
    "г": "L",
    "в": "ʚ",
    "б": "g",
    "а": "ɐ",
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}


def get_wr():
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Moskva')
    w = observation.weather
    temperature = w.temperature('celsius')
    return temperature


@app.on_message(filters.command('help', prefixes='.') & filters.me)
def help(_, msg):
    msg.edit("**TUSB** - это FOSS проект абсолютно бесплатный его цель увеличить количество возможностей в телеграмм\n"
             "**.com** - список команд \n"
             "**github** - https://github.com/XXmmRR/TUSB_tg_bot\n"
             "**telegram** - @obfserver\n"
             "**.donate** - реквизиты для поддержки проекта")


@app.on_message(filters.command('donate', prefixes='.') & filters.me)
def don(_, msg):
    msg.edit('**payeer** - P1010500299\n'
             '**Webmoney**(wmz) - Z792545865033\n'
             '**Webmoney**(wmr) - R182458813554')



@app.on_message(filters.command('com', prefixes='.') & filters.me)
def guide(_, msg):
    msg.edit("Список команд юзер бота 'TUSB'\n"
             ".hack - Взлом мамы обидчика   \n"
             ".l_hack - Взлом сердечка      \n"
             ".flip - Переворачивает буквы\n"
             ".type - Эффект печати текста  \n"
             ".block - Блокировка пользователя \n"
             ".spam Количество {@} - спамит\n"
             ".poto (1, 2) - Получает фото профиля по позиции \n"
             ".tag - Тегает всех в группе \n"
             ".info_group - О группе\n"
             ".joindate - Дата присоединения к группе\n"
             ".d_del - Удаляет удаленные аккаунты из группы\n"
             ".vax Количество - Делает ВАХ \n"
             ".yare Количество - Делает YARE \n"
             ".ure Количество - Делает УРЕ \n"
             ".neg - Накладывает фильтр негатива \n"
             ".gray - Делает фото серым \n"
             ".cont - Накладывает контуры на фото \n"
             ".auf - Сердце вора \n"
             ".ping - Задержка бота \n"
             ".donate - Реквизиты для поддержки проекта\n"
             ".dem - рандомный демотиватор на фото \n"
             "BY XMMR")


@app.on_message(filters.command('l_hack', prefixes='.') & filters.me)
def hack(_, msg):
    i = 1
    while i < 101:
        msg.edit(f"Взлом твоего сердечка {i}%❤️❤️❤️")
        i = i + randint(1, 3)
    msg.edit("Твоё сердечко взломано❤️❤️❤️❤️❤️")


@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)


@app.on_message(filters.command('hack', prefixes='.') & filters.me)
def hack(_, msg):
    i = 1
    try:
        while i < 101:
            msg.edit(f"Взлом твоей мамы чорт {i}%😈😈😈😈😈")
            i = i + randint(1, 3)
        msg.edit("Твоя Мама Взломана")
    except FloodWait:
        print('wait')

@app.on_message(filters.command('type', prefixes='.') & filters.me)
def typing(_, msg):
    original_mess = msg.text.split('.type', maxsplit=1)[1]
    text = original_mess
    tbp = ''
    typesim = '▒'

    while tbp != original_mess:
        try:
            msg.edit(tbp + typesim)
        except MessageEmpty:
            msg.edit(tbp + typesim + "▒")


        tbp = tbp + text[0]
        text = text[1:]

        try:
            msg.edit(tbp)
        except MessageEmpty:
            msg.edit(tbp + typesim + "▒")


@app.on_message(filters.command('wt', prefixes='.') & filters.me)
def send_wr(_, msg):
    weather = get_wr()
    msg.edit("Погода в Москве Сейчас  " + str(weather['temp']))


@app.on_message(filters.command('spam', prefixes='.') & filters.me)
def spam(_, msg):
    original = msg['text'].split(' ')[1]
    user = "@" + msg['text'].split(' ')[2]
    a = 1
    while a != int(original):
        app.send_message(user, '.')
        a = a + 1


@app.on_message(filters.command('block', prefixes='.') & filters.me)
def block_user(_, msg):
    try:
        username = msg["reply_to_message"]["from_user"]["username"]
        app.block_user(username)
    except TypeError:
        msg.edit('reply_message for block user')


@app.on_message(filters.command('poto', prefixes='.') & filters.me)
def get_poto(_, msg):
    ms_id = msg["message_id"]
    try:
        id = msg['chat']['id']
        count = msg['text'].split(' ')[1]
        name_id = msg['reply_to_message']['from_user']['id']
        pt = app.get_profile_photos(name_id)
        photo_id = []
        photo_ref = []
        selector = int(count) - 1
        for fotos in pt:
            photo_id.append(fotos['file_id'])
            photo_ref.append(fotos['file_ref'])
        app.send_photo(id, photo=photo_id[selector], file_ref=photo_ref[selector])
        app.delete_messages(id, ms_id)
    except:
        app.send_message('reply message like photo 1')


@app.on_message(filters.command('info_group', prefixes='.') & filters.me)
def info(_, msg):
    full = []
    title = msg['chat']['title']
    id = msg['chat']['id']
    typy = msg['chat']['type']
    scam = msg['chat']['is_scam']
    chat = app.get_chat(id)
    members = chat["members_count"]
    All = "Кол-во участников " + str(members) + "\n" + "Название группы " + title + "\nid:" + str(id) + "\nТип: " + typy + '\nСкам: ' + str(scam) + '\n' + "Admins:"
    adm = app.get_chat_members(id, filter="administrators")
    for l_adm in adm:
        full.append(l_adm['user']['first_name'] )
    f_str = str(full)
    send_adm = All + '\n' + "" +f_str[1: -1].replace(',','').replace("'", "")
    msg.edit(send_adm)


@app.on_message(filters.command("joindate", prefixes='.') & filters.me)
def join_date(app, message: Message):
    members = []
    for m in app.iter_chat_members(message.chat.id):
        members.append(
            (
                m.user.first_name,
                m.joined_date or app.get_messages(message.chat.id, 1).date,
            )
        )

    members.sort(key=lambda member: member[1])

    with open("joined_date.txt", "w", encoding="utf8") as f:
        f.write("Join Date      First Name\n")
        for member in members:
            f.write(
                str(datetime.fromtimestamp(member[1]).strftime("%y-%m-%d %H:%M"))
                + f" {member[0]}\n"
            )
    app.send_document(message.chat.id, "joined_date.txt")
    os.remove("joined_date.txt")


@app.on_message(filters.command('tag', prefixes='.') & filters.me)
def tag(_, msg):
    id = msg['chat']['id']
    mentionn = []
    for member in app.iter_chat_members(id):
        try:
            mentionn.append(member.user.mention)
        except:
            continue
    while len(mentionn) != 0:
        f5 = (mentionn[0:5])
        app.send_message(id, str(f5)[1:-1].replace(',', '\n').replace("'", ''))
        del mentionn[0:5]


@app.on_message(filters.command('d_del', prefixes='.') & filters.me)
def delete(_, msg):
    id = msg['chat']['id']
    deleted = [x for x in app.iter_chat_members(id) if x.user.is_deleted]
    print(len(deleted), "deleted accounts found")
    for u in deleted:
        try:
            app.kick_chat_member(id, u.user.id, int(time() + 60))
        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command('neg', prefixes='.') & filters.me)
def neg(_, msg):
    id = msg['chat']['id']
    try:
        photo = msg['reply_to_message']['photo']
        file_id = photo['file_id']
        file_ref = photo['file_ref']
        app.download_media(file_ref=file_ref, message=file_id , file_name='1.jpg',)
    except:
        msg.edit('Reply photo')
    try:
        c_obj = Filter()
        c_obj.filter_negative('downloads/1.jpg')
        app.send_photo(id, 'filtred.jpg')
        os.remove('filtred.jpg')
        os.remove('downloads/1.jpg')
    except:
        app.send_message(id, 'Some Error occured')


@app.on_message(filters.command('gray', prefixes='.') & filters.me)
def sepia(_, msg):
    id = msg['chat']['id']
    try:
        photo = msg['reply_to_message']['photo']
        file_id = photo['file_id']
        file_ref = photo['file_ref']
        app.download_media(file_ref=file_ref, message=file_id, file_name='2.jpg')
    except TypeError:
        msg.edit('Reply photo')
    try:
        c_obj = Filter()
        c_obj.filter_sepia('downloads/2.jpg')
        app.send_photo(id, 'filtred1.jpg')
        os.remove('filtred1.jpg')
        os.remove('downloads/2.jpg')
    except:
        app.send_message(id, "Some error occured")


@app.on_message(filters.command('blur', prefixes='.') & filters.me)
def blured(_, msg):
    id = msg['chat']['id']
    try:
        photo = msg['reply_to_message']['photo']
        file_id = photo['file_id']
        file_ref = photo['file_ref']
        app.download_media(file_ref=file_ref, message=file_id, file_name='3.jpg')
    except TypeError:
        msg.edit('Reply photo')
    try:
        c_obj = Filter()
        c_obj.filter_blur('downloads/3.jpg')
        app.send_photo(id, 'filtred2.jpg')
        os.remove('filtred2.jpg')
        os.remove('downloads/3.jpg')
    except:
        app.send_message(id, "Some error occured")


@app.on_message(filters.command('cont', prefixes='.')& filters.me)
def contur(_, msg):
    id = msg['chat']['id']
    try:
        photo = msg['reply_to_message']['photo']
        file_id = photo['file_id']
        file_ref = photo['file_ref']
        app.download_media(file_ref=file_ref, message=file_id, file_name='4.jpg')
    except TypeError:
        msg.edit('Reply photo')
    try:
        c_obj = Filter()
        c_obj.filter_contour('downloads/4.jpg')
        app.send_photo(id, 'filtred3.jpg')
        os.remove('filtred3.jpg')
        os.remove('downloads/4.jpg')
    except:
        app.send_message(id, "Some error occured")


@app.on_message(filters.command('vax', prefixes='.')& filters.me)
def VAX(_, msg):
    id = msg['chat']['id']
    count = msg['text'].split(' ')[1]
    vaax = "ВАХ " * int(count)
    try:
        msg.edit(vaax)
    except ValueError:
        app.send_message(id, vaax)


@app.on_message(filters.command('yare', prefixes='.')& filters.me)
def yar(_, msg):
    id = msg['chat']['id']
    count = msg['text'].split(' ')[1]
    yare = "YARE " * int(count)
    try:
        msg.edit(yare)
    except ValueError:
        app.send_message(id, yare)


@app.on_message(filters.command('ure', prefixes='.')& filters.me)
def Ure(_, msg):
    id = msg['chat']['id']
    count = msg['text'].split(' ')[1]
    UREE = "УРЕ " * int(count)
    try:
        msg.edit(UREE)
    except ValueError:
        app.send_message(id, UREE)


@app.on_message(filters.command('auf', prefixes='.')& filters.me)
def volk(_, msg):
    msg.edit('.◢🐺◣            ◢🐺◣\n'
             '🐺🐺🐺◣ ◢🐺🐺🐺\n'
             '◥🐺🐺🐺🐺🐺🐺◤\n'
             '    ◥🐺🐺🐺🐺◤\n'
             '         ◥☝️☝️◤\n'
             '             ◥ ◤')


@app.on_message(filters.command('yes', prefixes='.')& filters.me)
def Ure(_, msg):
    count = msg['text'].split(' ')[1]
    UREE = "YES " * int(count)
    msg.edit(UREE)


@app.on_message(filters.command('ping', prefixes='.')& filters.me)
def ping(_, msg):
    start_time = time()
    id = msg['chat']['id']
    app.send_message(id, ("Задержка бота %s seconds " % (time() - start_time)))


@app.on_message(filters.command('dota', prefixes='.') & filters.me)
def send_gos(_, msg):
    try:
        app.send_message('@DotaGosuBot', '/start')
        text = app.get_history('@DotaGosuBot', limit=1)
        done = text[0]['text']
        msg.edit(done)
    except:
        app.send_message('бот не работает')


@app.on_message(filters.command('dem', prefixes='.') & filters.me)
def demotivation(_, msg):
    msg.edit('**Демотивируем...**')
    ms_id = msg["message_id"]
    try:
        id = msg['chat']['id']
        mess_id = msg['reply_to_message']['message_id']
        app.forward_messages(from_chat_id=id, chat_id="@super_rjaka_demotivator_bot", message_ids=mess_id,
                        as_copy=True, remove_caption=True)
        sleep(2)
        demovat = app.get_history('@super_rjaka_demotivator_bot', limit=1)
        fimaly = demovat[0]["message_id"]
        while demovat == mess_id:
            sleep(1)
        app.forward_messages(from_chat_id='@super_rjaka_demotivator_bot', chat_id=id, message_ids=fimaly,
                         as_copy=True, remove_caption=True)
        app.delete_messages(id, ms_id)
    except TypeError:
        msg.edit("reply media for demotivation")


@app.on_message(filters.command('calc', prefixes='.') & filters.me)
def calculate(_, msg):
    id = msg['chat']['id']
    ms_id = msg['message_id']
    original_txt = msg['text']
    try:
        first = original_txt.split(' ')[1]
        operator = original_txt.split(' ')[2]
        second = original_txt.split(' ')[3]
        print(first, operator, second)
        try:
            c = 0
            if operator == '+':
                c = int(first) + int(second)
                app.send_message(id, f'Ответ равен {c}')
            if operator == '-':
                c = int(first) + int(second)
                app.send_message(id, f'Ответ равен {c}')
            if operator == '*':
                c = int(first) * int(second)
                app.send_message(id, f'Ответ равен {c}')
            if operator == '/':
                c = int(first) / int(second)
                app.send_message(id, f'Ответ равен {c}')
            if operator == '**':
                c = int(first) ** int(second)
                app.send_message(id, f'Ответ равен {c}')
            app.delete_messages(id, ms_id)
        except:
            app.send_message(id, "Invalid syntax")
    except TypeError:
        app.send_message(id, 'Error')


if __name__ == '__main__':
    app.run()