import pygame
import test_thu_ham_ve

pygame.init()
pygame.display.set_caption('Code-mau-giao-dien')
screen = pygame.display.set_mode((1400, 700))

running = True
Color_BackGorund = (23, 62, 130)
color_button = (250,0,0)
clock = pygame.time.Clock()
while running:		
	clock.tick(60)
	screen.fill(Color_BackGorund)
	pygame.draw.polygon(screen, color_button, points=[(1196,410),(1196,290),(1300 ,350)])
	pygame.draw.polygon(screen, color_button, points=[(996,410),(996,290),(892 ,350)])
	pygame.draw.polygon(screen, color_button, points=[(1096,146),(1156,250),(1036 ,250)])
	pygame.draw.polygon(screen, color_button, points=[(1096,550),(1156,450),(1036 ,450)])
	pygame.draw.circle(screen,(235, 64, 52), (1096,350), 65)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			test_thu_ham_ve.in_ra(2)
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()