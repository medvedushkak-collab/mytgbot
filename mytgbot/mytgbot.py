import telebot
import os
from telebot import types
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
dayTask = []
weekTask = []
yearTask = []
# основа меню
def send_Menu(chat_id):
    # контейнер чтобы кнопки передались
    markup = types.InlineKeyboardMarkup()
    # само добавление кнопок
    btnAddDayButton = types.InlineKeyboardButton("Добавить на день", callback_data = "add_day")
    btnAddWeekButton = types.InlineKeyboardButton("Добавить на неделю", callback_data = "add_week")
    btnAddYearButton = types.InlineKeyboardButton("Добавить на год", callback_data = "add_year")
    markup.add(btnAddDayButton, btnAddWeekButton,btnAddYearButton)
    bot.send_message(chat_id, "Выберите куда добавить задачу", reply_markup = markup)
# обрабатывает нажатие кнопок
# Кнопка добавление в задачи дня
@bot.callback_query_handler(func = lambda  call: call.data == "add_day")
def ButtonDay(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введите задачу на день")
    bot.register_next_step_handler_by_chat_id(call.message.chat.id,UpdateDayTask)
#Кнопка добавление в задачи недели
@bot.callback_query_handler(func = lambda call: call.data == "add_week")
def ButtonWeek(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введите задачу на неделю")
    bot.register_next_step_handler_by_chat_id(call.message.chat.id,UpdateWeekTask)
#кнопка добавление в задачи года
@bot.callback_query_handler(func = lambda call: call.data == "add_year")
def ButtonYear(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введите задачу на год")
    bot.register_next_step_handler_by_chat_id(call.message.chat.id,UpdateYearTask)
#старт
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,"Вы можете сюда записывать задачи на день, на неделю, или на год")
    send_Menu(message.chat.id)
#Функция меню
@bot.message_handler(commands = ['menu'])
def Menu(message):
    send_Menu(message.chat.id)
@bot.message_handler(commands = ["adddaytask"])
#Функции на добавление задач с помощью команд(вывод)
#вывод задачи дня
def TaskDay(message):
    bot.send_message(message.chat.id,"Вы можете сюда записывать задачи на день")
    bot.register_next_step_handler(message,UpdateDayTask)
#вывод задачи недели
def TaskWeek(message):
    bot.send_message(message.chat.id,"Введите задачу на неделю")
    bot.register_next_step_handler(message,UpdateWeekTask)
# =вывод задачи на год
def TaskYear(message):
    bot.send_message(message.chat.id,"Введите задачу на год")
    bot.register_next_step_handler(message,UpdateYearTask)
# Функции на удаление задач с помощью команд
@bot.message_handler(commands = ["FinishTask"])
def FinsihTask(message):
    bot.send_message(message.chat.id,"Выберете какой список хотите обновит: ")
    bot.send_message(message.chat.id,"1 - Ежедневную задачу")
    bot.send_message(message.chat.id,"2 - Еженедельную задачу")
    bot.send_message(message.chat.id,"3 - Годовую задачу")
    bot.register_next_step_handler(message, DeleteSomethingTask)
def DeleteSomethingTask(message):
    choise = message.text.strip()
    if(choise=='1'):
        bot.send_message(message.chat.id,"Напишите задачу которую хотите удалить")
        bot.register_next_step_handler(message,DayTaskDelete)
    elif(choise == '2'):
        bot.register_next_step_handler(message,WeekTaskDelete)
    elif(choise == '3'):
        bot.register_next_step_handler(message,YearTaskDelete)
    else:
        bot.send_message(message.chat.id," введите число 1 2 или 3")
#обновление массивов
#записываем задчу дня в массив
def UpdateDayTask(message):
    dayTask.append(message.text)
    bot.send_message(message.chat.id, str(dayTask))
@bot.message_handler(commands = ["addweektask"])
#записываем задачу недели в массив
def UpdateWeekTask(message):
    weekTask.append(message.text)
    bot.send_message(message.chat.id, str(weekTask))
@bot.message_handler(commands = ["addyeartask"])
#записываем задачу на год
def UpdateYearTask(message):
    yearTask.append(message.text)
    bot.send_message(message.chat.id, str(yearTask))
def DayTaskDelete(message):
    print("Функция запустилась")
    dayTask.remove(message.text)
    bot.send_message(message.chat.id, str(dayTask))
def WeekTaskDelete(message):
    print("Функция запустилась")
    dayTask.remove(message.text)
    bot.send_message(message.chat.id, str(dayTask))
def YearTaskDelete(message):
    print("Функция запустилась")
    dayTask.remove(message.text)
    bot.send_message(message.chat.id, str(dayTask))
bot.infinity_polling()

