from aiogram.fsm.state import State, StatesGroup

class CourseForm(StatesGroup):
    waiting_name = State()
    waiting_credits = State()
    waiting_grade = State()
    waiting_choice = State()