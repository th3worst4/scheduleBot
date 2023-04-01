from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from excelFunctions import today, anyday, tomorrow
from getBotData import readData

botTolkien = readData()

application = ApplicationBuilder().token(botTolkien).build()
weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = 609524364,
        text = 'Check your schedule! \nUse one of the following commands: \n/today \n/tomorrow \n/"anyweekday" (e.g. /friday)'
    )

async def todayBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = today()
    message = '\n'.join(info)
    await context.bot.send_message(
        chat_id = 609524364,
        text = message
    )

async def anydayBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/sunday':
        await context.bot.send_message(
            chat_id = 609524364,
            text = 'Do you want to study on SUNDAY??'
        )
    else:
        info = anyday(update.message.text)
        message = '\n'.join(info)
        await context.bot.send_message(
            chat_id = 609524364,
            text = message
        )

async def tomorrowBot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = tomorrow()
    if info == 'sunday':
        await context.bot.send_message(
            chat_id = 609524364,
            text = 'Do you want to study on SUNDAY??'
        )
    else:
        message = '\n'.join(info)
        await context.bot.send_message(
            chat_id = 609524364,
            text = message
        )


start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

today_handler = CommandHandler('today', todayBot)
application.add_handler(today_handler)

anyday_handler = CommandHandler(weekdays, anydayBot)
application.add_handler(anyday_handler)

tomorrow_handler = CommandHandler('tomorrow', tomorrowBot)
application.add_handler(tomorrow_handler)


application.run_polling()

