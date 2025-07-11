from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 🏠 Asosiy menyu tugmalari
def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💸 Rasxod"), KeyboardButton(text="📊 Balans")],
            [KeyboardButton(text="💰 Naxt"), KeyboardButton(text="💳 Karta")],
            [KeyboardButton(text="📚 Jurnal"), KeyboardButton(text="🔄 Yangilanish")],
        ],
        resize_keyboard=True
    )

# 💰 Naxt/Karta tanlovi (Rasxod va kirimlar uchun)
def cash_card_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="N"), KeyboardButton(text="K")],
        ],
        resize_keyboard=True
    )

# ✅ Ha/Yo‘q tugmalari (chek bormi kabi savollar uchun)
def yes_no_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ha"), KeyboardButton(text="Yo‘q")],
        ],
        resize_keyboard=True
    )

# ➕ Plus tugmasi (balans o‘tkazma qilish uchun)
def plus_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Pul o‘tkazish")],
            [KeyboardButton(text="🏠 Orqaga")],
        ],
        resize_keyboard=True
    )

# 🔁 Oylik va pul olish menyusi (balansda ko‘rsatiladi)
def balance_options_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="OYLIK MIQDORINI O‘ZGARTIRISH")],
            [KeyboardButton(text="PUL OLISH")],
        ],
        resize_keyboard=True
    )

# 🔄 Yangilanish (sozlamalar menyusi)
def settings_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛡 Kodni o‘zgartirish")],
            [KeyboardButton(text="🧹 Ma’lumotlarni tozalash")],
            [KeyboardButton(text="✍️ Oylikni o‘zgartirish")],
        ],
        resize_keyboard=True
    )
