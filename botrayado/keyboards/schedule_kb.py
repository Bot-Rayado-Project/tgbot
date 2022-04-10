from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

GROUP_BFI_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BVT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BST_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BEI_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BIB_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BAP_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BMP_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_ZRC_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BRT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BIK_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BEE_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BER_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BBI_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BIN_KB = ReplyKeyboardMarkup(resize_keyboard=True)


FACULTIES_KB = ReplyKeyboardMarkup(resize_keyboard=True)


STREAM_IT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_TSEIMK_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_RIT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_KIIB_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_SISS_KB = ReplyKeyboardMarkup(resize_keyboard=True)


DAYS_OF_WEEK_KB = ReplyKeyboardMarkup(resize_keyboard=True)
CURRENT_OR_NEXT_WEEK_KB = ReplyKeyboardMarkup(resize_keyboard=True)


GROUP_BUTTONS_BFI: list = ['бфи2101', 'бфи2102']
GROUP_BUTTONS_BVT: list = ['бвт2101', 'бвт2102', 'бвт2103', 'бвт2104', 'бвт2105', 'бвт2106', 'бвт2107', 'бвт2108']
GROUP_BUTTONS_BST: list = ['бст2101', 'бст2102', 'бст2103', 'бст2104', 'бст2105', 'бст2106']
GROUP_BUTTONS_BEI: list = ['бэи2101', 'бэи2102', 'бэи2103']
GROUP_BUTTONS_BIB: list = ['биб2101', 'биб2102', 'биб2103', 'биб2104']
GROUP_BUTTONS_BAP: list = ['бап2101']
GROUP_BUTTONS_BMP: list = ['бмп2101']
GROUP_BUTTONS_BUT: list = ['бут2101']
GROUP_BUTTONS_BEE: list = ['бээ2101']
GROUP_BUTTONS_BER: list = ['бэр2101']
GROUP_BUTTONS_BBI: list = ['бби2101']
GROUP_BUTTONS_ZRC: list = ['зрс2101', 'зрс2102']
GROUP_BUTTONS_BRT: list = ['брт2101', 'брт2102']
GROUP_BUTTONS_BIK: list = ['бик2101', 'бик2102', 'бик2103', 'бик2104', 'бик2105', 'бик2106', 'бик2107', 'бик2108', 'бик2109']
GROUP_BUTTONS_BIN: list = ['бин2101', 'бин2102', 'бин2103', 'бин2104', 'бин2105', 'бин2106', 'бин2107', 'бин2108', 'бин2109', 'бин2110']


FACULTIES_BUTTONS: list = ['ИТ', 'КиИБ', 'РиТ', 'ЦЭиМК', 'СиСС']


STREAM_IT_BUTTONS: list = ['бфи', 'бвт', 'бст', 'бэи']
STREAM_TSEIMK_BUTTONS: list = ['бээ', 'бэр', 'бби']
STREAM_KIIB_BUTTONS: list = ['бап', 'бмп', 'бут', 'зрс', 'биб']
STREAM_RIT_BUTTONS: list = ['брт', 'бик']
STREAM_SISS_BUTTONS: list = ['бин']


DAYS_OF_WEEK_BUTTONS: list = ['сегодня', 'завтра', 'вся неделя']
CURRENT_OR_NEXT_WEEK_BUTTONS: list = ['текущая неделя', 'следующая неделя']


DAYS_OF_WEEK_KB.row(
    KeyboardButton(DAYS_OF_WEEK_BUTTONS[0].capitalize()),
    KeyboardButton(DAYS_OF_WEEK_BUTTONS[1].capitalize()),
    KeyboardButton(DAYS_OF_WEEK_BUTTONS[2].capitalize())
)
DAYS_OF_WEEK_KB.row(KeyboardButton('Меню'))


CURRENT_OR_NEXT_WEEK_KB.row(
    KeyboardButton(CURRENT_OR_NEXT_WEEK_BUTTONS[0].capitalize()),
    KeyboardButton(CURRENT_OR_NEXT_WEEK_BUTTONS[1].capitalize())
)
CURRENT_OR_NEXT_WEEK_KB.row(KeyboardButton('Меню'))


FACULTIES_KB.row(
    KeyboardButton(FACULTIES_BUTTONS[0]),
    KeyboardButton(FACULTIES_BUTTONS[1]),
    KeyboardButton(FACULTIES_BUTTONS[2])
)
FACULTIES_KB.row(
    KeyboardButton(FACULTIES_BUTTONS[3]),
    KeyboardButton(FACULTIES_BUTTONS[4])
)
FACULTIES_KB.row(KeyboardButton('Меню'))


STREAM_IT_KB.row(
    KeyboardButton(STREAM_IT_BUTTONS[0].upper()),
    KeyboardButton(STREAM_IT_BUTTONS[1].upper()),
    KeyboardButton(STREAM_IT_BUTTONS[2].upper()),
    KeyboardButton(STREAM_IT_BUTTONS[3].upper())
)
STREAM_IT_KB.row(KeyboardButton('Меню'))


STREAM_TSEIMK_KB.row(
    KeyboardButton(STREAM_TSEIMK_BUTTONS[0].upper()),
    KeyboardButton(STREAM_TSEIMK_BUTTONS[1].upper()),
    KeyboardButton(STREAM_TSEIMK_BUTTONS[2].upper())
)
STREAM_TSEIMK_KB.row(KeyboardButton('Меню'))


STREAM_KIIB_KB.row(
    KeyboardButton(STREAM_KIIB_BUTTONS[0].upper()),
    KeyboardButton(STREAM_KIIB_BUTTONS[1].upper()),
    KeyboardButton(STREAM_KIIB_BUTTONS[2].upper())
)
STREAM_KIIB_KB.row(
    KeyboardButton(STREAM_KIIB_BUTTONS[3].upper()),
    KeyboardButton(STREAM_KIIB_BUTTONS[4].upper())
)
STREAM_KIIB_KB.row(KeyboardButton('Меню'))


STREAM_SISS_KB.row(KeyboardButton(STREAM_SISS_BUTTONS[0].upper()))
STREAM_SISS_KB.row(KeyboardButton('Меню'))


STREAM_RIT_KB.row(
    KeyboardButton(STREAM_RIT_BUTTONS[0].upper()),
    KeyboardButton(STREAM_RIT_BUTTONS[1].upper())
)
STREAM_RIT_KB.row(KeyboardButton('Меню'))


GROUP_BFI_KB.row(
    KeyboardButton(GROUP_BUTTONS_BFI[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BFI[1].upper())
)
GROUP_BFI_KB.row(KeyboardButton('Меню'))


GROUP_BVT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BVT[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BVT[1].upper()),
    KeyboardButton(GROUP_BUTTONS_BVT[2].upper())
)
GROUP_BVT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BVT[3].upper()),
    KeyboardButton(GROUP_BUTTONS_BVT[4].upper()),
    KeyboardButton(GROUP_BUTTONS_BVT[5].upper())
)
GROUP_BVT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BVT[6].upper()),
    KeyboardButton(GROUP_BUTTONS_BVT[7].upper())
)
GROUP_BVT_KB.row(KeyboardButton('Меню'))


GROUP_BST_KB.row(
    KeyboardButton(GROUP_BUTTONS_BST[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BST[1].upper()),
    KeyboardButton(GROUP_BUTTONS_BST[2].upper())
)
GROUP_BST_KB.row(
    KeyboardButton(GROUP_BUTTONS_BST[3].upper()),
    KeyboardButton(GROUP_BUTTONS_BST[4].upper()),
    KeyboardButton(GROUP_BUTTONS_BST[5].upper())
)
GROUP_BST_KB.row(KeyboardButton('Меню'))


GROUP_BEI_KB.row(
    KeyboardButton(GROUP_BUTTONS_BEI[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BEI[1].upper()),
    KeyboardButton(GROUP_BUTTONS_BEI[2].upper())
)
GROUP_BEI_KB.row(KeyboardButton('Меню'))


GROUP_BIB_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIB[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BIB[1].upper()),
    KeyboardButton(GROUP_BUTTONS_BIB[2].upper())
)
GROUP_BIB_KB.row(KeyboardButton(GROUP_BUTTONS_BIB[3].upper()))
GROUP_BIB_KB.row(KeyboardButton('Меню'))


GROUP_BAP_KB.row(KeyboardButton(GROUP_BUTTONS_BAP[0].upper()))
GROUP_BAP_KB.row(KeyboardButton('Меню'))


GROUP_BBI_KB.row(KeyboardButton(GROUP_BUTTONS_BBI[0].upper()))
GROUP_BBI_KB.row(KeyboardButton('Меню'))


GROUP_BMP_KB.row(KeyboardButton(GROUP_BUTTONS_BMP[0].upper()))
GROUP_BMP_KB.row(KeyboardButton('Меню'))


GROUP_BUT_KB.row(KeyboardButton(GROUP_BUTTONS_BUT[0].upper()))
GROUP_BUT_KB.row(KeyboardButton('Меню'))


GROUP_BEE_KB.row(KeyboardButton(GROUP_BUTTONS_BEE[0].upper()))
GROUP_BEE_KB.row(KeyboardButton('Меню'))


GROUP_BER_KB.row(KeyboardButton(GROUP_BUTTONS_BER[0].upper()))
GROUP_BER_KB.row(KeyboardButton('Меню'))


GROUP_ZRC_KB.row(
    KeyboardButton(GROUP_BUTTONS_ZRC[0].upper()),
    KeyboardButton(GROUP_BUTTONS_ZRC[1].upper())
)
GROUP_ZRC_KB.row(KeyboardButton('Меню'))


GROUP_BRT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BRT[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BRT[1].upper())
)
GROUP_BRT_KB.row(KeyboardButton('Меню'))


GROUP_BIK_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIK[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BIK[1].upper()),
    KeyboardButton(GROUP_BUTTONS_BIK[2].upper())
)
GROUP_BIK_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIK[3].upper()),
    KeyboardButton(GROUP_BUTTONS_BIK[4].upper()),
    KeyboardButton(GROUP_BUTTONS_BIK[5].upper())
)
GROUP_BIK_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIK[6].upper()),
    KeyboardButton(GROUP_BUTTONS_BIK[7].upper()),
    KeyboardButton(GROUP_BUTTONS_BIK[8].upper())
)
GROUP_BIK_KB.row(KeyboardButton('Меню'))


GROUP_BIN_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIN[0].upper()),
    KeyboardButton(GROUP_BUTTONS_BIN[1].upper()),
    KeyboardButton(GROUP_BUTTONS_BIN[2].upper())
)
GROUP_BIN_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIN[3].upper()),
    KeyboardButton(GROUP_BUTTONS_BIN[4].upper()),
    KeyboardButton(GROUP_BUTTONS_BIN[5].upper())
)
GROUP_BIN_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIN[6].upper()),
    KeyboardButton(GROUP_BUTTONS_BIN[7].upper()),
    KeyboardButton(GROUP_BUTTONS_BIN[8].upper())
)
GROUP_BIN_KB.row(KeyboardButton(GROUP_BUTTONS_BIN[9].upper()))
GROUP_BIN_KB.row(KeyboardButton('Меню'))