# encoding: utf-8
import sys
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import unicodedata
import urllib2
import time
import datetime
from time import gmtime, strftime, sleep
import re
import os
from bs4 import BeautifulSoup
import configparser

token = 'insira seu token aqui'

def getDolar(chat_id, comando):
    bot.sendMessage(chat_id, 'Aguarde, coletando informações...')
    page = urllib2.urlopen('http://www.dolarhoje.net.br/')
    soup = BeautifulSoup(page, "html5lib")
    dados = soup.find('div', {'id': 'divSpdInText'})
    dolarc = dados.contents[1].contents[3].contents[1].contents[3].find(text=True).encode('utf-8')
    dolart = dados.contents[1].contents[3].contents[3].contents[3].find(text=True).encode('utf-8')
    dolarc = re.search('\d{1,3},\d{1,2}', dolarc).group(0)
    dolart = re.search('\d{1,3},\d{1,2}', dolart).group(0)
    bot.sendMessage(chat_id,'''Dolar Comercial em: R$ %s
Dolar Turismo em: R$ %s''' % (dolarc, dolart))
    
    
def getEuro(chat_id, comando):
    bot.sendMessage(chat_id, 'Aguarde, coletando informações...')
    page = urllib2.urlopen('http://www.dolarhoje.net.br/')
    soup = BeautifulSoup(page, "html5lib")
    dados = soup.find('div', {'id': 'divSpdInText'})
    euroco = dados.contents[1].contents[3].contents[7].contents[3].find(text=True).encode('utf-8')
    eurotu = dados.contents[1].contents[3].contents[9].contents[3].find(text=True).encode('utf-8')
    euroc = re.search('\d{1,3},\d{1,2}', euroco).group(0)
    eurot = re.search('\d{1,3},\d{1,2}', eurotu).group(0)
    bot.sendMessage(chat_id,'''Euro comercial em: R$ %s
Euro turismo em: R$ %s''' %(euroc, eurot))
    
def getBitcoin(chat_id, comando):
    bot.sendMessage(chat_id, 'Aguarde, coletando informações...')
    page = urllib2.urlopen('http://dolarhoje.com/bitcoin/')
    soup = BeautifulSoup(page, "html5lib")
    dados = soup.find('table', {'id': 'conversao'})
    bitcoin_ = dados.contents[3].contents[3].contents[3].find(text=True).encode('utf-8')
    bitcoin = re.search('\d{1,},\d{1,}', bitcoin_).group(0)
    bot.sendMessage(chat_id,'BitcoinToYou em: R$ %s' %bitcoin)

def getEbanx(chat_id, comando):
    bot.sendMessage(chat_id, 'Indisponível no momento')
    #bot.sendMessage(chat_id, 'Aguarde, coletando informações...')
    #pagina = urllib2.urlopen('https://www.ebanx.com/br/ebanx-dollar-card')
    #texto = pagina.read().decode('utf-8')
    #onde = texto.find('tax">')
    #inicio = onde + 8
    #fim = inicio + 4
    #ebanx = texto[inicio:fim].encode('utf-8')
    #bot.sendMessage(chat_id, 'Cotação Ebanx em: R$ %s' %ebanx)

def handle(msg):
    
    comando = msg['text'].encode('utf-8')
    content_type, chat_type, chat_id = telepot.glance(msg)
    msg = telepot.namedtuple.Message(**msg)
    usrname = msg.chat[3].encode('ascii','ignore')

    keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Dólar"), KeyboardButton(text="Euro")],
            [KeyboardButton(text="Bitcoin"),  KeyboardButton(text="Cotação Ebanx")],
            [KeyboardButton(text="Ajuda")],
        ])
    
    if comando == '/start':
        bot.sendMessage(chat_id, '''Bem Vindo!! %s
Bot desenvolvido por @bergpb!
/start - Inicie o Bot
Use os comandos do teclado abaixo:
Dólar - Cotacao atual do dólar
Euro - Cotacao atual do euro
Bitcoin - Cotacao atual do bitcoin
Cotacao Ebanx - Cotacao atual do dolar no site do Ebanx''' %usrname, reply_markup=keyboard)
        inf(chat_id)
            
    elif comando == 'Dólar':
        getDolar(chat_id, comando)
        
    elif comando == 'Euro':
        getEuro(chat_id, comando)
        
    elif comando == 'Bitcoin':
        getBitcoin(chat_id, comando)
        
    elif comando == 'Cotação Ebanx':
        getEbanx(chat_id, comando)
        
    else:
        bot.sendMessage(chat_id, '''Ative o teclado e selecione os comandos.''')

 
bot = telepot.Bot(token)

bot.message_loop(handle)
              
print 'Aguardando comandos...'

while 1:
    time.sleep(5)



