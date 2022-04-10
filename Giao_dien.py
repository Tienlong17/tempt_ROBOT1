import pygame
import test_thu_ham_ve

pygame.init()
pygame.display.set_caption('Code-mau-giao-dien')
screen = pygame.display.set_mode((700, 700))

running = True
Color_BackGorund = (23, 62, 130)
color_button = (252, 186, 3)
clock = pygame.time.Clock()
while running:		
	clock.tick(60)
	screen.fill(Color_BackGorund)

	mouse_x,mouse_y = pygame.mouse.get_pos()
	# button chuc nang di chuyen 
	pygame.draw.rect(screen,color_button,(120,330,50,50))
	pygame.draw.rect(screen,color_button,(120,400,50,50))
	pygame.draw.rect(screen,color_button,(120,470,50,50))
	pygame.draw.rect(screen,color_button,(50,400,50,50))
	pygame.draw.rect(screen,color_button,(190,400,50,50))

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (120 < mouse_x < 170) and (330 < mouse_y < 380):
					'''Di toi '''
					test_thu_ham_ve.in_ra(1)

				if (120 < mouse_x < 170) and (470 < mouse_y < 520):
					'''Di lui '''
					test_thu_ham_ve.in_ra(2)

				if (50 < mouse_x < 100) and (400 < mouse_y < 450):
					'''Di trai '''
					test_thu_ham_ve.in_ra(3)

				if (190 < mouse_x < 240) and (400 < mouse_y < 450):
					'''Di phai '''
					test_thu_ham_ve.in_ra(4)

				if (120 < mouse_x < 170) and (400 < mouse_y < 450):
					'''Dung lai'''
					test_thu_ham_ve.in_ra(5)
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()