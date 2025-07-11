from aiogram import Router, types
from db.database import conn
import pandas as pd
from io import BytesIO

router = Router()

@router.message(lambda msg: msg.text == "📚 Jurnal")
async def show_journal(message: types.Message):
    user_id = message.from_user.id
    df = pd.read_sql_query("SELECT amount, method, reason, date FROM transactions WHERE user_id = ? ORDER BY date DESC", conn, params=(user_id,))
    
    text = ""
    for i, row in df.head(20).iterrows():
        text += f"{row['date'][:10]} - {row['amount']:.0f} so‘m ({row['method']}) - {row['reason']}\n"

    await message.answer(f"📄 <b>Jurnal (1-sahifa):</b>\n{text}")
    
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    await message.answer_document(types.BufferedInputFile(file=output.read(), filename="jurnal.xlsx"))
