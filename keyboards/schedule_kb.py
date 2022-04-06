from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

GROUP_BUTTONS_BFI_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BVT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BST_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BEI_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BIB_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BAP_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BMP_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BUT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_ZRC_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BRT_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BIK_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BEE_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BER_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BBI_KB = ReplyKeyboardMarkup(resize_keyboard=True)
GROUP_BUTTONS_BIN_KB = ReplyKeyboardMarkup(resize_keyboard=True)


FACULTIES_BUTTONS_KB = ReplyKeyboardMarkup(resize_keyboard=True)


STREAM_IT_BUTTONS_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_TSEIMK_BUTTONS_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_RIT_BUTTONS_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_KIIB_BUTTONS_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_SISS_BUTTONS_KB = ReplyKeyboardMarkup(resize_keyboard=True)
STREAM_KB = ReplyKeyboardMarkup(resize_keyboard=True)


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


FACULTIES_BUTTONS_KB.row(
    KeyboardButton(FACULTIES_BUTTONS[0].capitalize()),
    KeyboardButton(FACULTIES_BUTTONS[1].capitalize()),
    KeyboardButton(FACULTIES_BUTTONS[2].capitalize())
)
FACULTIES_BUTTONS_KB.row(
    KeyboardButton(FACULTIES_BUTTONS[3].capitalize()),
    KeyboardButton(FACULTIES_BUTTONS[4].capitalize())
)
FACULTIES_BUTTONS_KB.row(KeyboardButton('Меню'))


STREAM_IT_BUTTONS_KB.row(
    KeyboardButton(STREAM_IT_BUTTONS[0].capitalize()),
    KeyboardButton(STREAM_IT_BUTTONS[1].capitalize()),
    KeyboardButton(STREAM_IT_BUTTONS[2].capitalize()),
    KeyboardButton(STREAM_IT_BUTTONS[3].capitalize())
)
STREAM_IT_BUTTONS_KB.row(KeyboardButton('Меню'))


STREAM_TSEIMK_BUTTONS_KB.row(
    KeyboardButton(STREAM_TSEIMK_BUTTONS[0].capitalize()),
    KeyboardButton(STREAM_TSEIMK_BUTTONS[1].capitalize()),
    KeyboardButton(STREAM_TSEIMK_BUTTONS[2].capitalize())
)
STREAM_TSEIMK_BUTTONS_KB.row(KeyboardButton('Меню'))


STREAM_KIIB_BUTTONS_KB.row(
    KeyboardButton(STREAM_KIIB_BUTTONS[0].capitalize()),
    KeyboardButton(STREAM_KIIB_BUTTONS[1].capitalize()),
    KeyboardButton(STREAM_KIIB_BUTTONS[2].capitalize())
)
STREAM_KIIB_BUTTONS_KB.row(
    KeyboardButton(STREAM_KIIB_BUTTONS[3].capitalize()),
    KeyboardButton(STREAM_KIIB_BUTTONS[4].capitalize())
)
STREAM_KIIB_BUTTONS_KB.row(KeyboardButton('Меню'))


STREAM_SISS_BUTTONS_KB.row(KeyboardButton(STREAM_SISS_BUTTONS[0].capitalize()))
STREAM_SISS_BUTTONS_KB.row(KeyboardButton('Меню'))


STREAM_RIT_BUTTONS_KB.row(
    KeyboardButton(STREAM_RIT_BUTTONS[0].capitalize()),
    KeyboardButton(STREAM_RIT_BUTTONS[1].capitalize())
)
STREAM_RIT_BUTTONS_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BFI_KB.row(
    KeyboardButton(GROUP_BUTTONS_BFI[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BFI[1].capitalize())
)
GROUP_BUTTONS_BFI_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BVT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BVT[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BVT[1].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BVT[2].capitalize())
)
GROUP_BUTTONS_BVT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BVT[3].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BVT[4].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BVT[5].capitalize())
)
GROUP_BUTTONS_BVT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BVT[6].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BVT[7].capitalize())
)
GROUP_BUTTONS_BVT_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BST_KB.row(
    KeyboardButton(GROUP_BUTTONS_BST[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BST[1].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BST[2].capitalize())
)
GROUP_BUTTONS_BST_KB.row(
    KeyboardButton(GROUP_BUTTONS_BST[3].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BST[4].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BST[5].capitalize())
)
GROUP_BUTTONS_BST_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BEI_KB.row(
    KeyboardButton(GROUP_BUTTONS_BEI[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BEI[1].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BEI[2].capitalize())
)
GROUP_BUTTONS_BEI_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BIB_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIB[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIB[1].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIB[2].capitalize())
)
GROUP_BUTTONS_BIB_KB.row(KeyboardButton(GROUP_BUTTONS_BIB[3].capitalize()))
GROUP_BUTTONS_BIB_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BAP_KB.row(KeyboardButton(GROUP_BUTTONS_BAP[0].capitalize()))
GROUP_BUTTONS_BAP_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BBI_KB.row(KeyboardButton(GROUP_BUTTONS_BBI[0].capitalize()))
GROUP_BUTTONS_BBI_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BMP_KB.row(KeyboardButton(GROUP_BUTTONS_BMP[0].capitalize()))
GROUP_BUTTONS_BMP_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BUT_KB.row(KeyboardButton(GROUP_BUTTONS_BUT[0].capitalize()))
GROUP_BUTTONS_BUT_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BEE_KB.row(KeyboardButton(GROUP_BUTTONS_BEE[0].capitalize()))
GROUP_BUTTONS_BEE_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BER_KB.row(KeyboardButton(GROUP_BUTTONS_BER[0].capitalize()))
GROUP_BUTTONS_BER_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_ZRC_KB.row(
    KeyboardButton(GROUP_BUTTONS_ZRC[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_ZRC[1].capitalize())
)
GROUP_BUTTONS_ZRC_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BRT_KB.row(
    KeyboardButton(GROUP_BUTTONS_BRT[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BRT[1].capitalize())
)
GROUP_BUTTONS_BRT_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BIK_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIK[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIK[1].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIK[2].capitalize())
)
GROUP_BUTTONS_BIK_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIK[3].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIK[4].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIK[5].capitalize())
)
GROUP_BUTTONS_BIK_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIK[6].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIK[7].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIK[8].capitalize())
)
GROUP_BUTTONS_BIK_KB.row(KeyboardButton('Меню'))


GROUP_BUTTONS_BIN_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIN[0].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIN[1].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIN[2].capitalize())
)
GROUP_BUTTONS_BIN_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIN[3].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIN[4].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIN[5].capitalize())
)
GROUP_BUTTONS_BIN_KB.row(
    KeyboardButton(GROUP_BUTTONS_BIN[6].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIN[7].capitalize()),
    KeyboardButton(GROUP_BUTTONS_BIN[8].capitalize())
)
GROUP_BUTTONS_BIN_KB.row(KeyboardButton(GROUP_BUTTONS_BIN[9]))
GROUP_BUTTONS_BIN_KB.row(KeyboardButton('Меню'))