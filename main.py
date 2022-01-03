from telegram.ext import CommandHandler, Updater, CallbackContext
from telegram import Update
import logging
import constants

# function to execute for start command


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello, I am python bot. Try /help command to know more')

# function to execute for help command


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("List of commands:")
    update.message.reply_text('/add <1st number> <2nd number>')
    update.message.reply_text('/subtract <1st number> <2nd number')
    update.message.reply_text('/multiply <1st number> <2nd number>')
    update.message.reply_text("/divide <1st number> <2nd number")

# function to execute for add command


def add(update: Update, context: CallbackContext) -> None:
    try:
        a = int(context.args[0])+int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Sorry I cant understand that')

# function to execute for subtract command


def subtract(update: Update, context: CallbackContext) -> None:
    try:
        a = int(context.args[0])-int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Sorry I cant understand that')

# function to execute for multiply command


def multiply(update: Update, context: CallbackContext) -> None:
    try:
        a = int(context.args[0])*int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Sorry I cant understand that')

# function to execute for divide command


def divide(update: Update, context: CallbackContext) -> None:
    try:
        a = int(context.args[0])/int(context.args[1])
        update.message.reply_text(f'= {a}')
    except:
        update.message.reply_text('Sorry I cant understand that')

# main function


def main():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    updater = Updater(token=constants.key)
    dispatch = updater.dispatcher
    help_handler = CommandHandler('help', help_command)
    subtract_handler = CommandHandler('subtract', subtract)
    multiply_handler = CommandHandler('multiply', multiply)
    add_handler = CommandHandler('add', add)
    divide_handler = CommandHandler('divide', divide)
    start_handler = CommandHandler('start', start)
    dispatch.add_handler(help_handler)
    dispatch.add_handler(add_handler)
    dispatch.add_handler(subtract_handler)
    dispatch.add_handler(multiply_handler)
    dispatch.add_handler(divide_handler)
    dispatch.add_handler(start_handler)
    updater.start_polling(poll_interval=2)
    updater.idle()


main()  # control first calls the main function
