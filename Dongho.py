#Thư viện
import pygame
import time 
import math
#Khởi tạo các hàm pygame
pygame.init()
#Tạo màn hình
screen = pygame.display.set_mode((500,600))
#Đặt tên chương trình
pygame.display.set_caption('BOM HEN GIO')
#Màu
YELLOW=(237, 219, 128)
RED=(255,0,0)
WHITE=(225,225,225)
BLACK=(0,0,0)
VIOLET=(136, 134, 240)
#Tạo font
font=pygame.font.SysFont('sans',40)
font_1=pygame.font.SysFont('sans',20)
font_2=pygame.font.SysFont('sans',35)
#Biến chạy
running	= True
#Tạo chữ
text_1=font.render('+',True,BLACK)
text_2=font.render('-',True,BLACK)
text_3=font.render('+',True,BLACK)
text_4=font.render('-',True,BLACK)
text_5=font.render('Start',True,BLACK)
text_6=font.render('Reset',True,BLACK)
text_7=font_1.render('RicotKey',True,VIOLET)
#Biến tổng số giây
total_secs = 0
total = 0
#Biến chạy nút Start
start = False
#File âm thanh
sound = pygame.mixer.Sound('BOMB.wav')
sound_2 = pygame.mixer.Sound('clock.wav')
#Giảm fbs 
clock = pygame.time.Clock()
#Vòng lặp vẽ màn hình
while running:
	#Giảm fbs
	clock.tick(60)
	#Màn hình bao quát màu
	screen.fill(YELLOW)
	#Định vị con trỏ
	mouse_x,mouse_y=pygame.mouse.get_pos()
	#Tạo ô + - phút
	pygame.draw.rect(screen, BLACK,(100,400,50,50))
	pygame.draw.rect(screen, WHITE,(105,405,40,40))
		#Bỏ dấu - vào ô
	screen.blit(text_2,(120,400))
	pygame.draw.rect(screen, BLACK,(100,300,50,50))
	pygame.draw.rect(screen, WHITE,(105,305,40,40))
		#Bỏ dấu + vào ô	
	screen.blit(text_1,(115,300))

	#Tạo ô cộng trừ giây
	pygame.draw.rect(screen, BLACK,(200,400,50,50))
	pygame.draw.rect(screen, WHITE,(205,405,40,40))
		#Bỏ dấu - vào ô
	screen.blit(text_4,(220,400))
	pygame.draw.rect(screen, BLACK,(200,300,50,50))
	pygame.draw.rect(screen, WHITE,(205,305,40,40))
		#Bỏ dấu + vào ô
	screen.blit(text_3,(215,300))
	#Tạo nút Start
	pygame.draw.rect(screen, BLACK,(300,300,100,50))
	pygame.draw.rect(screen, WHITE,(305,305,90,40))
		#Viết chữ Start vào ô
	screen.blit(text_5,(315,300))
	#Tạo nút Resert
	pygame.draw.rect(screen, BLACK,(300,400,100,50))
	pygame.draw.rect(screen, WHITE,(305,405,90,40))
	screen.blit(text_6,(305,400))
	#Tên tác giả
	screen.blit(text_7,(10,10))
	#Tạo thanh thời gian
	pygame.draw.rect(screen, BLACK,(50,500,400,50))
	pygame.draw.rect(screen, WHITE,(55,505,390,40))
	#Tạo đồng hồ
	pygame.draw.circle(screen, BLACK,(250,150),125)
	pygame.draw.circle(screen, WHITE,(250,150),120)
	#Tâm đồng hồ
	pygame.draw.circle(screen, BLACK,(250,150),5)
	#Các sự kiện của chương trình
	for event in pygame.event.get():
		#Bấm nút X thoát chương trình
		if event.type == pygame.QUIT:
			running = False 
		#Bấm nút +
		if event.type == pygame.MOUSEBUTTONDOWN:
			#Khi bấm chuột trái
			if event.button == 1:
				#Bấm nút để dừng file nhạc
				pygame.mixer.pause()
				#Dấu cộng phút
				if (105 < mouse_x < 145) and (305 < mouse_y <345):
					total_secs += 60
					total = total_secs
					print('+ 1m')
				#Dấu trừ phút
				if (105 < mouse_x < 145) and (405 < mouse_y <445):
					total_secs -= 60
					total = total_secs
					print('- 1m')
				#Dấu trừ giây
				if (205 < mouse_x < 245) and (405 < mouse_y <445):
					total_secs -= 1
					total = total_secs
					print('- 1s')				
				#Dấu cộng giây
				if (205 < mouse_x < 245) and (305 < mouse_y <345):
					total_secs += 1
					total = total_secs
					print('+ 1s')
				#Nút Start
				if (305 < mouse_x < 395) and (305 < mouse_y <345):
					start = True
					total = total_secs
					print('Start')
				#Nút Reset
				if (305 < mouse_x < 395) and (405 < mouse_y <445):
					total_secs =0
					print('Reset')
				print('total_secs:'+ str(total_secs))
	#Bắt đầu tính giờ
	if start:
		pygame.mixer.Sound.play(sound_2)
		total_secs -= 1
		#Dừng
		if total_secs == 0:
			start = False
			#Chạy nhạc khi hết thời gian
			pygame.mixer.Sound.play(sound)
		time.sleep(1)
	#Fix số âm
	if total_secs < 0 :
		start = False
		total_secs = 0
	#Tính phút và giây
	mins= int(total_secs/60)
	secs= total_secs-(mins*60) 
	#Hiển thị thời gian				
	text_time = font_2.render(str(mins)+'m', True, BLACK)
	text_time_1 = font_2.render(str(secs)+'s', True, BLACK)
	screen.blit(text_time, (105,355))
	screen.blit(text_time_1, (205,355))	
	#Quay kim giây
	x_sec = 250 + 110 * math.sin(6*secs*math.pi/180)
	y_sec = 150 - 110 * math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,150),(int(x_sec),int(y_sec)))
	#Quay kim phút
	x_mins = 250 + 90 * math.sin(6*mins*math.pi/180)
	y_mins = 150 - 90 * math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen,RED,(250,150),(int(x_mins),int(y_mins)))
	#Tạo thanh chạy thời gian
	if total != 0 :
		pygame.draw.rect(screen,RED,(60,510,int (380*(total_secs/total)),30))	
	#Vẽ lên màn hình
	pygame.display.flip()
#Chạy xong chương trình thì xóa bộ nhớ
pygame.quit()
		