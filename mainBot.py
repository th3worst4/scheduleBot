from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters
from excelFunctions import today, anyday, tomorrow
from getBotData import readData
import sys

botTolkien = readData()

application = ApplicationBuilder().token(botTolkien).build()
weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
    chat_id = update.effective_chat.id,
    text = 'Check your schedule! \nUse one of the following commands: \n/today \n/tomorrow \n/{anyweekday} (e.g. /friday)'
    )

async def todayBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = today()
    if info == 'sunday':    
        await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'Do you want to study on SUNDAY??'
    )
    else:
        message = '\n'.join(info)
        await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = message
        )

async def anydayBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/sunday':
        await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'Do you want to study on SUNDAY??'
        )
    else:
        info = anyday(update.message.text)
        message = '\n'.join(info)
        await context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = message
        )

async def tomorrowBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = tomorrow()
    if info == 'sunday':
        await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'Do you want to study on SUNDAY??'
        )
    else:
        message = '\n'.join(info)
        await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = message
        )

async def turnPcServer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.message.text == "Y":
            sys.exit("Terminal was closed")
        elif update.message.text == "N":
            await context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Right them..."
            )
        else:
            await context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "I didn't understand, so I will do nothing."
            )

    await update.message.reply_text(
        'Are you sure you want to turn off the server?(Y/N)',
    )
    turn_off_answer = MessageHandler(filters.TEXT , answer)
    application.add_handler(turn_off_answer)


start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

today_handler = CommandHandler('today', todayBot)
application.add_handler(today_handler)

anyday_handler = CommandHandler(weekdays, anydayBot)
application.add_handler(anyday_handler)

tomorrow_handler = CommandHandler('tomorrow', tomorrowBot)
application.add_handler(tomorrow_handler)

turn_offpc_handler = CommandHandler("pcoff", turnPcServer)
application.add_handler(turn_offpc_handler)




application.run_polling()

