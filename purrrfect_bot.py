import  telebot
from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv('AUT_TOKEN')

bot = telebot.TeleBot(token)

def get_url():
    contents = requests.get('https://thatcopy.pw/catapi/rest/').json()
    image_url = contents['url']
    return image_url

def get_fact():
    contents = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1').json()
    fact = contents['text']
    if len(fact) < 10:
        return get_fact()
    return fact

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hello, how are you? 
Send /meow to get a cat image.
Send /fact to get random Cat Fact.'''
    bot.send_message(message.chat.id, msg) 



@bot.message_handler(commands = ['meow'])
@bot.message_handler(regexp=r'meow')
def meow(message):
    url = get_url()
    print(message.chat.id)
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['fact'])
@bot.message_handler(regexp=r'fact')
def fact(message):
    fact = get_fact()
    print(message.chat.id)
    bot.send_message(message.chat.id, fact)

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)

def main():
    bot.polling()

if __name__ == '__main__':
    main()

