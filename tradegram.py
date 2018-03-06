# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
 
TOKEN = '334761788:AAGoxtYTU6j1VX2prgqvYop2uu0CIzi4CVU' # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
    #Teclado
	keyboard = types.ReplyKeyboardMarkup(row_width=3)
	button1 = types.KeyboardButton('XBT')
	button2 = types.KeyboardButton('ETH')
	button3 = types.KeyboardButton('LTC')
	keyboard.row(button1, button2, button3)
	button4 = types.KeyboardButton('ETC')
	button5 = types.KeyboardButton('XRP')
	button6 = types.KeyboardButton('XMR')
	keyboard.row(button4, button5, button6)
	button7 = types.KeyboardButton('ZEC')
	button8 = types.KeyboardButton('REP')
	button9 = types.KeyboardButton('BCH')
	keyboard.row(button7, button8, button9)
	bot.send_message(cid, "¿Qué precio quieres saber?", reply_markup = keyboard)
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################

#Funciones
@bot.message_handler(commands=['start']) 
def command_hola(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Hola, soy el bot de Kraken.')
    
@bot.message_handler(commands=['hola']) 
def command_kraken(m):
    cid = m.chat.id
    bot.send_photo( cid, open( './res/kraken.jpg', 'rb')) 



#############################################


#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
