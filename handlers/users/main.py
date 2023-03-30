import logging
from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards.default.button import markup,number,tekshirish
from states.state import Sherik_kerak
import regex
import re
from loader import dp,bot
from data.config import ADMINS


@dp.message_handler(commands=['help'],state='*')
async def help(message: types.Message):
    await message.answer("UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali.\n\nBu yerda Programmalash bo`yicha\n#Ustoz,  \n#Shogird,\n#oquvKursi,\n#Sherik,  \n#Xodim va \n#IshJoyi \ntopishingiz mumkin. \n\nE'lon berish: @UstozShogirdBot\n\nAdmin @UstozShogirdAdminBot")

@dp.message_handler(text="👥 Sherik kerak",state="*")
async def sherik(message: types.Message,state: FSMContext):
    await message.answer("<b>Sherik topish uchun ariza berish</b>\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to'g'ri bo'lsa,<b> ✅ Ha</b> tugmasini bosing va arizangiz Adminga yuboriladi",parse_mode='HTML')
    await message.answer("<b>Ism, familiyangizni kiriting?</b>",parse_mode='HTML',reply_markup=types.ReplyKeyboardRemove())

    await Sherik_kerak.full_name.set()


@dp.message_handler(state=Sherik_kerak.full_name)
async def techno(message: types.Message,state: FSMContext):
    ismi = message.text
    await state.update_data({"full_name":ismi})
    await message.answer("📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#")
    await Sherik_kerak.next()

@dp.message_handler(state=Sherik_kerak.texnalogiya)
async def techno(message: types.Message,state: FSMContext):
    techno1=message.text
    await state.update_data({"techno":techno1})
    await message.answer("📞 Aloqa: \n\n⚠️ TANISHIB CHIQING\nBog`lanish uchun raqamingizni kiriting \nMasalan, <b>+998971128921</b>\nYoki pastdagi <b>Raqamni Ulashish</b> knopkasi orqali raqaminggizni jo'nating",reply_markup=number,parse_mode='HTML')
    await Sherik_kerak.next()


@dp.message_handler(state=Sherik_kerak.aloqa)
async def techno(message: types.Message,state: FSMContext):
    nomer=message.text
    andoza = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
    if re.match(andoza,nomer):
        await state.update_data({"nomer": nomer})
        await message.answer("🌐 Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting")
        await Sherik_kerak.next()
    else:
        await message.answer("❗️<b>Raqaminggizni faqat sonlarda kiriting</b>❗️\n\n<b>Yoki O'zbekiston telefon raqamini kiriting \nRaqaminggizni namunadagidek qilib yuboring</b>",parse_mode='HTML')

@dp.message_handler(content_types=['contact'],state=Sherik_kerak.aloqa)
async def kantakt(message: types.Message,state: FSMContext):
    get_phone = message.contact.phone_number
    await state.update_data(({"phone_number":get_phone}))
    print(get_phone)
    await message.answer("🌐 Hudud: \n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting")
    await Sherik_kerak.next()

@dp.message_handler(state=Sherik_kerak.hudud)
async def kantakt(message: types.Message,state: FSMContext):
    hududi = message.text
    await state.update_data(({"hududi":hududi}))
    await message.answer("💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await Sherik_kerak.next()

@dp.message_handler(state=Sherik_kerak.Narxi)
async def narxi(message: types.Message,state: FSMContext):
    narxi = message.text
    await state.update_data({'narxi':narxi})
    await message.answer("👨🏻‍💻 Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba")
    await Sherik_kerak.next()

@dp.message_handler(state=Sherik_kerak.Kasbi)
async def narxi(message: types.Message,state: FSMContext):
    kasbi = message.text
    await state.update_data({'kasbi':kasbi})
    await message.answer("🕰 Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await Sherik_kerak.next()

@dp.message_handler(state=Sherik_kerak.vaqti)
async def narxi(message: types.Message,state: FSMContext):
    vaqt = message.text
    await state.update_data({'vaqt':vaqt})
    await message.answer("🔎 Maqsad: \n\nMaqsadingizni qisqacha yozib bering.")
    await Sherik_kerak.next()

@dp.message_handler(state=Sherik_kerak.maqsad)
async def narxi(message: types.Message,state: FSMContext):
    maqsadi = message.text
    await state.update_data({'maqsadi':maqsadi})
    data = await state.get_data()
    user = message.from_user.username
    sherikk = data.get('full_name')
    technoo = data.get("techno")
    aloqaa = data.get('nomer')
    aloqa2 = data.get('phone_number')
    hudud = data.get('hududi')
    narxii = data.get('narxi')
    kasbii = data.get('kasbi')
    vaqtiii = data.get('vaqt')
    maqsadii = data.get('maqsadi')
    await message.answer(f"Sherik kerak:\n\n👥 Sherik: {sherikk}\n📚 Texnologiya: {technoo}\n™️ Telegram: @{user}\n📞 Aloqa: {aloqaa or aloqa2}\n📍 Hudud: {hudud}\n💰 Narxi: {narxii}\n👨🏻‍💻 Kasbi: {kasbii}\n🕰 Murojaat qilish vaqti: {vaqtiii}\n🔎 Maqsad: {maqsadii}")
    await message.answer("Barcha ma'lumotlar to'g'rimi?",reply_markup=tekshirish)
    await Sherik_kerak.next()




   
@dp.message_handler(text="✅ Ha",state=Sherik_kerak.confirm)
async def haa(message: types.Message,state: FSMContext):
    data = await state.get_data()
    kantakt1 = data.get('nomer')
    user = message.from_user.username
    sherikk = data.get('full_name')
    technoo = data.get("techno")
    aloqaa = data.get('nomer')
    aloqa2 = data.get("phone_number")
    hudud = data.get('hududi')
    narxii = data.get('narxi')
    kasbii = data.get('kasbi')
    vaqtiii = data.get('vaqt')
    maqsadii = data.get('maqsadi')
    await message.answer("Sizning arizanggiz muvoffaqiyatli qabul qilindi 😌 \nAdminni o'zi buni ko'rib chiqadi va kanalga joylaydi!",reply_markup=markup)
    
    if aloqaa:
        # print("oh yes")
        s = f"Sherik kerak:\n\n👥 Sherik: {sherikk}\n📚 Texnologiya: {technoo}\n🇺🇿 Telegram: @{user}\n📞 Aloqa: {aloqaa}\n📍 Hudud: {hudud}\n💰 Narxi: {narxii}\n👨🏻‍💻 Kasbi: {kasbii}\n🕰 Murojaat qilish vaqti: {vaqtiii}\n🔎 Maqsad: {maqsadii}"
        for admin in ADMINS:
            await bot.send_message(chat_id=int(admin),text=s,reply_markup=markup)
            await state.finish()
    elif aloqa2:
        # print("oh yes222")
        s1 = f"Sherik kerak:\n\n👥 Sherik: {sherikk}\n📚 Texnologiya: {technoo}\n🇺🇿 Telegram: @{user}\n📞 Aloqa: {aloqa2}\n📍 Hudud: {hudud}\n💰 Narxi: {narxii}\n👨🏻‍💻 Kasbi: {kasbii}\n🕰 Murojaat qilish vaqti: {vaqtiii}\n🔎 Maqsad: {maqsadii}"
        for admin1 in ADMINS:
            await bot.send_message(chat_id=int(admin1),text=s1,reply_markup=markup)
            await state.finish()
    

@dp.message_handler(text="❌ Yo'q",state=Sherik_kerak.confirm)
async def haa(message: types.Message,state: FSMContext):
    await message.answer("Qabul qilinmadi",reply_markup=markup)
    await state.finish()
