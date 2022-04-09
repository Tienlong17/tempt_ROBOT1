import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Code-mau-giao-dien')
running = True
Color_BackGorund = (23, 62, 130)
clock = pygame.time.Clock()

while running:		
	clock.tick(60)
	screen.fill(Color_BackGorund)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()