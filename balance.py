from aiogram import Router, types
from db.database import get_balance
from utils.currency import convert_to_uzs

router = Router()

@router.message(lambda msg: msg.text == "📊 Balans")
async def show_balance(message: types.Message):
    user_id = message.from_user.id
    cash = get_balance(user_id, "N")
    card = get_balance(user_id, "K")
    total = cash + card

    total_usd = total / await convert_to_uzs(1)

    await message.answer(f"""
<b>KASSADAGI BALANSINGIZ:</b> {total_usd:.2f}$
<b>HOZIRGI KURSDA:</b> {int(total):,} so‘m
""", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="OYLIK MIQDORINI O‘ZGARTIRISH")],
            [types.KeyboardButton(text="PUL OLISH")],
        ],
        resize_keyboard=True
    ))
