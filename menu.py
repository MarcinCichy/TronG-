import pygame.image

import functions
import main_game
from constants import *
from board import Board
from buttons import Button

# set buttons in menu
button_1pl_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
button_1pl = Button(button_1pl_img, 420, 280, "1 PLAYER")
button_2pl_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
button_2pl = Button(button_2pl_img, 420, 340, "2 PLAYERS")
button_opt_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
button_opt = Button(button_opt_img, 420, 400, "OPTIONS")
button_quit_img = pygame.image.load('pics/emty_button_1.png').convert_alpha()
button_quit = Button(button_quit_img, 420, 460, "QUIT")


class Menu:
	def __init__(self):
		self.menu_background_img = pygame.image.load('pics/menu_background.png')
		self.menu_background_pos = self.menu_background_img.get_rect()
		self.menu_img = pygame.image.load('pics/menu.png').convert_alpha()
		self.menu_size = self.menu_img.get_rect()
		self.menu_size.midtop = (400, 240)
		self.menu_pos = self.menu_size
		self.static_background = Board()
	
	def show_menu(self):
		buttons_list = []
		menu_on = True
		while menu_on:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					menu_on = False
			# show menu
			screen.blit(self.menu_background_img, self.menu_background_pos)
			screen.blit(self.menu_img, self.menu_pos)
			
			# show buttons
			button_1pl.show_button()
			button_2pl.show_button()
			button_opt.show_button()
			button_quit.show_button()
			
			move_arrows = self.switch_between_buttons()
			self.select_button(move_arrows)
			pygame.display.update()
		
		pygame.quit()
		exit()
		
	def switch_between_buttons(self):
		key = None
		global MOVE_MENU
		start_pos_y = 270
		end_pos_y = 450
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					MOVE_MENU += 60
				if event.key == pygame.K_UP:
					MOVE_MENU -= 60
				if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					key = "K_RETURN"
		
		select_arrows = button_font.render(">             <", False, FONT_COLOR)
		select_arrows_pos = select_arrows.get_rect()
		select_arrows_pos.topleft = (320, select_arrows_pos.y)
		select_arrows_pos.y += MOVE_MENU
		if select_arrows_pos.y < start_pos_y:
			select_arrows_pos.y = end_pos_y
			MOVE_MENU = end_pos_y
		elif select_arrows_pos.y > end_pos_y:
			select_arrows_pos.y = start_pos_y
			MOVE_MENU = start_pos_y
		
		screen.blit(select_arrows, (320, select_arrows_pos.y))
		return select_arrows_pos, key
	
	def select_button(self, x):
		colide = pygame.Rect.colliderect(x[0], button_quit.button_pos)
		if colide and x[1] == "K_RETURN":
			pygame.quit()
			exit()
		colide = pygame.Rect.colliderect(x[0], button_1pl.button_pos)
		if colide and x[1] == "K_RETURN":
			print('1 PLAYER')
		colide = pygame.Rect.colliderect(x[0], button_2pl.button_pos)
		if colide and x[1] == "K_RETURN":
			main_game.main_game()
		colide = pygame.Rect.colliderect(x[0], button_opt.button_pos)
		if colide and x[1] == "K_RETURN":
			print('OPTIONS')