import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

TOKEN = "8546210786:AAHKpQotNPJvbYpnU7cfqF7PZBh2bD0NcnI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ---------- ЯЗЫКОВОЕ МЕНЮ ----------
lang_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Русский 🇷🇺")],
        [KeyboardButton(text="Кыргызча 🇰🇬")],
        [KeyboardButton(text="O‘zbekcha 🇺🇿")]
    ],
    resize_keyboard=True
)

# ---------- КОНТАКТЫ ----------
WHATSAPP_NUMBER = "+996558148484"
WHATSAPP_LINK = "https://wa.me/996556611162"

# ---------- СПИСОК ТОВАРОВ ----------
products = [
    ["Картошка", "Картошка", "Kartoshka"],
    ["Лук", "Пияз", "Piyoz"],
    ["Желтая морковь", "Сары сабиз", "Sari sabzi"],
    ["Красная морковь", "Кызыл сабиз", "Qizil sabzi"],
    ["Лимон", "Лимон", "Limon"],
    ["Яблоко", "Алма", "Olma"],
    ["Зеленое яблоко", "Жашыл алма", "Yashil olma"],
    ["Банан", "Банан", "Banan"],
    ["Виноград", "Жүзүм", "Uzum"],
    ["Гранат", "Анор", "Anor"],
    ["Дыня", "Коон", "Qovun"],
    ["Масло подсолнечное", "Май", "Yog'"],
    ["Кызылча", "Кызылча", "Lavlagi"],
    ["Шолгом", "Шалгам", "Shalg‘am"],
    ["Туруп", "Турп", "Turp"],
    ["Хурма", "Хурма", "Xurmo"],
    ["Грейпфрут", "Грейпфрут", "Greypfrut"],
    ["Ананас", "Ананас", "Ananas"],
    ["Брокли", "Брокколи", "Brokoli"],
    ["Киви", "Киви", "Kivi"],
    ["Капуста", "Капуста", "Karam"],
    ["Корейская капуста", "Корейче капуста", "Koreyscha karam"],
    ["Помидор", "Помидор", "Pomidor"],
    ["Огурец", "Бадыран", "Bodring"],
    ["Зелень", "Жашылча", "Ko‘kat"],
    ["Рис (сорт уточнить по телефону)", "Аш (сортун телефон менен сураңыз)", "Guruch (telefon orqali aniqlang)"]
]

# ---------- ТЕКСТЫ ----------
def get_text(lang_index):
    product_list = "\n".join([f"• {p[lang_index]}" for p in products])
    return (
        f"📋 *Меню:*\n\n"
        f"{product_list}\n\n"
        f"📞 Чтобы узнать цену, наличие и доставку — свяжитесь:\n"
        f"👉 *{WHATSAPP_NUMBER}*\n"
        f"WhatsApp: {WHATSAPP_LINK}"
    )

# ---------- START ----------
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Выберите язык / Тилди тандаңыз / Tilni tanlang:",
        reply_markup=lang_menu
    )

# ---------- ВЫБОР ЯЗЫКА ----------
@dp.message()
async def language_handler(message: types.Message):
    txt = message.text

    if txt == "Русский 🇷🇺":
        await message.answer(get_text(0), parse_mode="Markdown")
    elif txt == "Кыргызча 🇰🇬":
        await message.answer(get_text(1), parse_mode="Markdown")
    elif txt == "O‘zbekcha 🇺🇿":
        await message.answer(get_text(2), parse_mode="Markdown")
    else:
        await message.answer("Пожалуйста, выберите язык из меню.")

# ---------- ЗАПУСК ----------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
