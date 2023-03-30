from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton(text="👥 Sherik kerak"),KeyboardButton(text="📍 Ish joyi kerak"))
markup.row("👤 Hodim Kerak","👨🏻‍🏫 Ustoz kerak")
markup.add(KeyboardButton(text="👨🏻‍🎓 Shogird kerak"))

number=ReplyKeyboardMarkup(resize_keyboard=True)
number.add(KeyboardButton(text="Raqamni Ulashish",request_contact=True))

tekshirish = ReplyKeyboardMarkup(resize_keyboard=True)
tekshirish.row("✅ Ha","❌ Yo'q")