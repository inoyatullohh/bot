from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards import main_menu

router = Router()

class AuthState(StatesGroup):
    waiting_for_code = State()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("🛡 Kirish kodi: ")
    await state.set_state(AuthState.waiting_for_code)

@router.message(AuthState.waiting_for_code)
async def check_code(message: types.Message, state: FSMContext):
    if message.text == "2303":
        await message.answer("✅ Kirdingiz.", reply_markup=main_menu())
        await state.clear()
    else:
        await message.answer("❌ Noto‘g‘ri kod.")
