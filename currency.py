import aiohttp
from config import API_KEY

async def convert_to_uzs(amount_usd: float) -> float:
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base=USD&symbols=UZS"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            kurs = data["rates"]["UZS"]
            return amount_usd * kurs
