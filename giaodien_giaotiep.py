from keyword import iskeyword
import pygame
import main_moudle

# cau hinh
pygame.init()
pygame.display.set_caption('Code-mau-giao-dien')
screen = pygame.display.set_mode((600, 600))

running = True
Color_BackGorund = (23, 62, 130)
color_button1 = (232, 53, 21)
color_button2 = (232, 232, 21)
color_draw = (10, 210, 255) # mau cho button
blue_light = (21, 232, 204)
blue_drark = (2, 38, 102)

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2] and mouse_y > self.position[1] and mouse_y < self.position[1] + self.text_box[3]:
			return True
		else:
			return False

	def draw(self):
		font = pygame.font.SysFont('sans',30)
		text_render = font.render(self.text, True, color_draw)
		self.text_box = text_render.get_rect()

		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, (0,0,255))
			pygame.draw.rect(screen,(100,100,100), (self.position[0],self.position[1],self.text_box[2],self.text_box[3]))
			pygame.draw.line(screen, (0,0,255), (self.position[0], self.position[1] + self.text_box[3]), (self.position[0]+self.text_box[2], self.position[1] + self.text_box[3]))
		else:
			text_render = font.render(self.text, True, color_draw)

		screen.blit(text_render,self.position)

class DrawRectangle:
	def __int__(self,position_x, position_y, dai, rong):
		self.position_x = position_x
		self.position_y = position_y
		self.dai = dai
		self.rong = rong
	#def draw(self,position_x, position_y, dai, rong):


def creat_text_word(a : str):
	'''Ham de tao ghi chu~'''
	font = pygame.font.SysFont("sans",30)
	return  font.render(a,True, blue_light)

clock = pygame.time.Clock()

def get_Button(mouse_x,mouse_y):
	x = 0
	if (120 < mouse_x < 170) and (350 < mouse_y < 400):
		x = 1

	if (120 < mouse_x < 170) and (500 < mouse_y < 550):
		x = 2

	if (50 < mouse_x < 100) and (430 < mouse_y < 480):
		x = 3

	if (190 < mouse_x < 240) and (430 < mouse_y < 480):
		x = 4

	if (120 < mouse_x < 170) and (430 < mouse_y < 480):
		x = 0
	return x

def print_something(a :str):
	print(a)

# define variable
type_move = 0
huong =0
trot_button = TextButton("   Trotting   ", (170,42))
crawl_button = TextButton("   Crawling   ", (300,42))
while running:		
	clock.tick(60) # 60
	screen.fill(Color_BackGorund)

	#trot_button.draw()
	#crawl_button.draw()
	mouse_x,mouse_y = pygame.mouse.get_pos()
	'''Giao dien man hinh'''
	# button chuc nang di chuyen 
	#pygame.draw.rect(screen,color_button2,(120,350,50,50))

	#Ve cac information
	#screen.blit(creat_text_word('Name Robot:'),(12,12))


	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				print(event.unicode)
			if event.key == pygame.K_LEFT:
				print('qua trai')
			if event.key == pygame.K_RIGHT:
				print('qua phai')
			if event.key == pygame.K_UP:
				print('di len')
			if event.key == pygame.K_DOWN:
				print("di xuong")
	
	pygame.display.flip()

pygame.quit()