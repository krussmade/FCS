# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import telebot
from logging import log
import time
from telebot.custom_filters import StateFilter
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from bot import config
from bot.models import Profile, FAQ, Cat
import markdown
import os
import random


class Command(BaseCommand):
	help = 'Телеграм бот'

	def handle(self, *args, **options):
		state_storage = StateMemoryStorage()
		bot = telebot.TeleBot(config.token, state_storage=state_storage)

		@bot.message_handler(commands=['start'])
		def start(message):
			try:
				profile = Profile.objects.get(tg_id=message.chat.id)
			except:
				profile = Profile.objects.create(
					tg_id = message.chat.id,
					username = message.chat.username,
					first_name = message.chat.first_name,
					last_name = message.chat.last_name
					)
				profile.save()

			start_menu = telebot.types.ReplyKeyboardMarkup(True)
			for question in FAQ.objects.all():
				start_menu.row(question.question)
			start_menu.row('Фотографии котиков для снижения тревожности')

			bot.send_message(message.chat.id, 'Привет, здесь ты найдешь ответы на все частые вопросы', reply_markup=start_menu)

		@bot.message_handler(content_types=['text'])
		def text(message):
			try:
				profile = Profile.objects.get(tg_id=message.chat.id)
			except:
				profile = Profile.objects.create(
					tg_id = message.chat.id,
					username = message.chat.username,
					first_name = message.chat.first_name,
					last_name = message.chat.last_name
					)
				profile.save()
			start_menu = telebot.types.ReplyKeyboardMarkup(True)
			for question in FAQ.objects.all():
				start_menu.row(question.question)
			start_menu.row('Фотографии котиков для снижения тревожности')

			for question in FAQ.objects.all():
				if question.question == message.text:
					answer = question.answer
					bot.send_message(message.chat.id, answer, reply_markup=start_menu, parse_mode='html')

			if message.text == 'Фотографии котиков для снижения тревожности':
				media_group = []
				for cat in Cat.objects.all():
					media_group.append(open(cat.image.url[1:], 'rb'))
				index = random.randint(0, len(media_group)-1)
				bot.send_photo(message.chat.id, media_group[index])


		while True:
			try:
				log(msg='Bot running..', level=30)
				bot.polling(none_stop=True, interval=0)
				break

			except Exception as e:
				log(msg=e, level=30)
				log(msg='Restarting..',level=30)
				bot.stop_polling()
				time.sleep(1)
				log(msg='Running again!',level=30)






















