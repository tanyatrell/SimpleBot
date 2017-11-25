import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem 
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(bot, update):
    print(update)
    mytext = """Привет, {}!

Я простой бот и понимаю только команды /start и /planet <имя планеты на английском>
Например, /planet mars
    """.format(update.message.chat.first_name)
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)
    
    
def planet(bot, update):
    date = datetime.datetime.now()
    planet_name = update.message.text[7:]
    planet_name = planet_name.replace(' ', '')

    if planet_name =='mars':
        planet = ephem.Mars(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    elif planet_name =='jupiter':
        planet = ephem.Jupiter(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    elif  planet_name =='venus':
        planet = ephem.Venus(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    elif  planet_name =='mercury':
        planet = ephem.Mercury(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    elif  planet_name =='saturn':
        planet = ephem.Saturn(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    elif  planet_name =='uranus':
        planet = ephem.Uranus(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    elif  planet_name =='neptune':
        planet = ephem.Neptune(date)
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text('Не могу найти созвездие.')
        

def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
    updtr.dispatcher.add_handler(CommandHandler('planet', planet))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()

