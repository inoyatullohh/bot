from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.database import add_transaction
from utils.currency import convert_to_uzs
from keyboards import cash_card_keyboard, yes_no_keyboard
from datetime import datetime

router = Router()

# Holatlar
class ExpenseState(StatesGroup):
    waiting_amount = State()
    waiting_method = State()
    waiting_reason = State()
    waiting_chek = State()

# 💸 Rasxod tugmasi
@router.message(F.text == "💸 Rasxod")
async def expense_start(message: types.Message, state: FSMContext):
    await message.answer("💵 Summani kiriting (misol: 2000 yoki 50$):")
    await state.set_state(ExpenseState.waiting_amount)

@router.message(ExpenseState.waiting_amount)
async def expense_amount(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if text.endswith("$"):
        amount = float(text[:-1])
        amount_uzs = await convert_to_uzs(amount)
    else:
        amount_uzs = float(text) * 1000

    await state.update_data(amount=amount_uzs)
    await message.answer("💳 To‘lov usuli?", reply_markup=cash_card_keyboard())
    await state.set_state(ExpenseState.waiting_method)

@router.message(ExpenseState.waiting_method)
async def expense_method(message: types.Message, state: FSMContext):
    method = message.text
    if method not in ["N", "K"]:
        return await message.answer("Faqat N (Naxt) yoki K (Karta) deb yozing.")

    await state.update_data(method=method)
    await message.answer("📝 Sababini yozing:")
    await state.set_state(ExpenseState.waiting_reason)

@router.message(ExpenseState.waiting_reason)
async def expense_reason(message: types.Message, state: FSMContext):
    await state.update_data(reason=message.text)
    await message.answer("🧾 Chek bormi?", reply_markup=yes_no_keyboard())
    await state.set_state(ExpenseState.waiting_chek)

@router.message(ExpenseState.waiting_chek, F.text == "Ha")
async def expense_chek_photo(message: types.Message, state: FSMContext):
    await message.answer("📷 Chek suratini yuboring:")

@router.message(ExpenseState.waiting_chek, F.photo)
async def save_chek_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    add_transaction(message.from_user.id, data["amount"], data["method"], data["reason"], photo)
    await message.answer("✅ Rasxod saqlandi.")
    await state.clear()

@router.message(ExpenseState.waiting_chek, F.text == "Yo‘q")
async def expense_no_chek(message: types.Message, state: FSMContext):
    data = await state.get_data()
    add_transaction(message.from_user.id, data["amount"], data["method"], data["reason"], None)
    await message.answer("✅ Rasxod cheksiz saqlandi.")
    await state.clear()
