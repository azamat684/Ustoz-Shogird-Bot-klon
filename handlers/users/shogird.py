from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from states.state import Shogird_Kerak
from keyboards.default.button import markup,tekshirish
from data.config import ADMINS
from states.state import Shogird_Kerak
@dp.message_handler(text="👨🏻‍🎓 Shogird kerak",state="*")
async def create_Shogird_Kerak_list(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer(text="Shogird topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer(text="<b>Ism, familiyangizni kiriting</b>")
    await Shogird_Kerak.full_name.set()


@dp.message_handler(state=Shogird_Kerak.full_name)
async def get_Shogird_Kerak_full_name(message: types.Message, state: FSMContext):
    await state.update_data({"full_name": message.text})
    await message.answer(text="🕑 Yosh:\n\nYoshingizni kiriting\nMasalan, 19")
    await Shogird_Kerak.age.set()


@dp.message_handler(state=Shogird_Kerak.age)
async def get_Shogird_Kerak_age(message: types.Message, state: FSMContext):
    await state.update_data({"age": message.text})
    await message.answer(text="📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n<i>Python, C++, C#</i>")
    await Shogird_Kerak.technology.set()


@dp.message_handler(state=Shogird_Kerak.technology)
async def get_Shogird_Kerak_techs(message: types.Message, state: FSMContext):
    try:
        technologies = message.text.split(",")
        text = str()
        if len(technologies) >= 2:
            for tech in technologies:
                text += f"{tech.title()}, "
            await state.update_data({"technologies": text[:-2]})
        elif len(technologies) == 1:
            await state.update_data({"technologies": technologies[0].title()})
    except:
        technologies = message.text
        await state.update_data({"technologies": technologies.title()})
    await message.answer(text="📞 Aloqa:\n\nBog`lanish uchun raqamingizni kiriting\nMasalan, +998 90 123 45 67")
    await Shogird_Kerak.phone.set()


@dp.message_handler(state=Shogird_Kerak.phone)
async def get_Shogird_Kerak_phone(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        phone = ""
    else:
        phone = message.text
    await state.update_data({"phone": phone})
    await message.answer(text="🌐 Hudud:\n\nQaysi hududdansiz\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await Shogird_Kerak.location.set()


@dp.message_handler(state=Shogird_Kerak.location)
async def get_Shogird_Kerak_location(message: types.Message, state: FSMContext):
    await state.update_data({"location": message.text})
    await message.answer(text="💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await Shogird_Kerak.price.set()


@dp.message_handler(state=Shogird_Kerak.price)
async def get_Shogird_Kerak_price(message: types.Message, state: FSMContext):
    await state.update_data({"price": message.text})
    await message.answer(text="👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o`qiysizmi?Masalan, Dasturchi")
    await Shogird_Kerak.job.set()



@dp.message_handler(state=Shogird_Kerak.job)
async def get_Shogird_Kerak_job(message: types.Message, state: FSMContext):
    await state.update_data({"job": message.text})
    await message.answer(text="🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await Shogird_Kerak.time.set()


@dp.message_handler(state=Shogird_Kerak.time)
async def get_Shogird_Kerak_time(message: types.Message, state: FSMContext):
    await state.update_data({"time": message.text})
    await message.answer(text="🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering.")
    await Shogird_Kerak.goal.set()


@dp.message_handler(state=Shogird_Kerak.goal)
async def get_Shogird_Kerak_goal(message: types.Message, state: FSMContext):
    await state.update_data({"goal": message.text})
    data = await state.get_data()
    full_name = data.get("full_name")
    age = data.get("age")
    technologies = data.get("technologies")
    phone = data.get("phone")
    location = data.get("location")
    price = data.get("price")
    job = data.get("job")
    time = data.get("time")
    goal = data.get("goal")
    text = f"<b>Shogird kerak:</b>\n\n🎓 Ustoz: {full_name}\n🌐 Yosh: {age}\n📚 Texnologiya: {technologies}\n🇺🇿 Telegram: @{message.from_user.username}\n📞 Aloqa: {phone}\n🌐 Hudud: {location}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {job}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}"
    await message.answer(text=text)
    await message.answer(text="Barcha ma'lumotlar to'g'rimi?", reply_markup=tekshirish)
    await Shogird_Kerak.confirm.set()
    
@dp.message_handler(text="✅ Ha",state=Shogird_Kerak.confirm)
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
    

@dp.message_handler(text="❌ Yo'q",state=Shogird_Kerak.confirm)
async def haa(message: types.Message,state: FSMContext):
    await message.answer("Qabul qilinmadi",reply_markup=markup)
    await state.finish()
