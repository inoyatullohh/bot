from aiogram import Router, types

router = Router()

@router.message(lambda msg: msg.text == "🔄 Yangilanish")
async def settings_menu(message: types.Message):
    await message.answer("⚙️ Sozlamalar:\n1. Kodni o‘zgartirish\n2. Ma’lumotlarni tozalash\n3. Oylikni o‘zgartirish")

@router.message(lambda msg: msg.text == "OYLIK MIQDORINI O‘ZGARTIRISH")
async def change_salary(message: types.Message):
    await message.answer("✍️ Yangi oylik miqdorini kiriting (misol: 300$):")

@router.message(lambda msg: msg.text == "PUL OLISH")
async def withdraw(message: types.Message):
    await message.answer("💵 Qancha pul olmoqchisiz?")
