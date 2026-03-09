from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from app.bot.states import CourseForm
from app.calculator.gpa import calculate_gpa
from app.model.course import Course
from app.bot.keyboards import credits_keyboard, grades_keyboard, choice_keyboard

router = Router()

@router.message(Command("Start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(CourseForm.waiting_name)
    await message.answer("Name of the course...")

@router.message(CourseForm.waiting_name)
async def credits(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(CourseForm.waiting_credits)
    await message.answer("Weight of the course(credits)...", reply_markup=credits_keyboard())

@router.message(CourseForm.waiting_credits)
async def grade(message: Message, state: FSMContext):
    await state.update_data(credits=message.text)
    await state.set_state(CourseForm.waiting_grade)
    await message.answer("What is your grade?", reply_markup=grades_keyboard())

@router.message(CourseForm.waiting_grade)
async def save_grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    data = await state.get_data()
    new_course = Course(data["name"], data["credits"], data["grade"])
    courses = data.get("courses", [])
    courses.append(new_course)
    await state.update_data(courses=courses)
    await state.set_state(CourseForm.waiting_choice)
    await message.answer("Do you want to add more courses or evaluate GPA?", reply_markup=choice_keyboard())
    
    # result = calculate_gpa([new_course])
    # text = (
    #     f"That is your GPA - {result}"
    # )
    # await message.answer(text)

