from aiogram.dispatcher.filters.state import State,StatesGroup


class Sherik_kerak(StatesGroup):
    full_name=State()
    texnalogiya=State()
    aloqa=State()
    hudud=State()
    Narxi=State()
    Kasbi=State()
    vaqti=State()
    maqsad=State()
    confirm=State()

class Ish_joy_kerak(StatesGroup):
    ism=State()
    yosh = State()
    texnalogiya_2=State()
    aloqa_2=State()
    hudud_2=State()
    Narxi_2=State()
    Kasbi_2=State()
    vaqti_2=State()
    maqsad_2=State()
    confirm_2=State()


class Shogird_Kerak(StatesGroup):
    full_name = State()
    age = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    time = State()
    goal = State()
    confirm = State()