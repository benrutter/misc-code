import pygame
import random

pygame.init()

class Ball:

        def __init__(self, board_width, board_height):
                self.center = {'x':int(board_width/2), 'y':int(board_height/2)}
                self.location = self.center.copy()
                self.velocity = {'x':random.randint(-20,20), 'y':random.randint(-20,20)}
                while ((self.velocity['y'] < 10) and (self.velocity['y'] > -10)) or (self.velocity['x'] == 0):
                    self.velocity = {'x':random.randint(-20,20), 'y':random.randint(-20,20)}
                self.size = 10
                self.count = 0
                self.recently_hit = 0
        
        def move(self, board_size, paddle):

                if (self.location['x'] + self.size >= board_size['x']) or (self.location['x'] <= 0):
                        self.velocity['x'] *= -1
                if (self.location['y'] + self.size <= 0):
                        self.velocity['y'] *= -1
                
                if (self.location['y'] + self.size > board_size['y'] + 100):
                        self.count = 0;
                        self.velocity = {'x':random.randint(-20,20), 'y':random.randint(-20,20)}
                        while  ((self.velocity['y'] < 10) and (self.velocity['y'] > -10)) or (self.velocity['x'] == 0):
                            self.velocity = {'x':random.randint(-20,20), 'y':random.randint(-20,20)}
                        self.location = self.center.copy()
                        self.recently_hit = 0
                
                if ((self.location['x'] + self.size >= paddle.location['x']) and (self.location['x'] <= paddle.location['x'] + paddle.size['x'])):
                    if ((self.location['y'] + self.size >= paddle.location['y']) and (self.location['y'] <= paddle.location['y'] + paddle.size['y'])):
                        if self.recently_hit <= 0:
                            self.velocity['y'] *= -1
                            self.count += 1;
                            self.recently_hit += 50


                self.location['x'] += self.velocity['x']
                self.location['y'] += self.velocity['y']
                self.recently_hit -= 1

class Paddle:

        def __init__(self, location, board_size):
                self.location = location;
                self.size = {'x':int(board_size['x']*0.2), 'y':10}
        
        def move(self, key_pressed, board_size):
                if key_pressed[pygame.K_LEFT]:
                    self.location['x'] = max(0, self.location['x']-20)
                if key_pressed[pygame.K_RIGHT]:
                    self.location['x'] = min(board_size['x']-self.size['x'], self.location['x']+20)

board = {'size': {'x':500, 'y':600}}
ball = Ball(board['size']['x'], board['size']['y'])
paddle = Paddle({'x':board['size']['x']/2, 'y': board['size']['y']-50}, board['size'])

screen = pygame.display.set_mode((board['size']['x'], board['size']['y']))
being_played = True

#font = pygame.font.Font('freesansbold.ttf', 32) 


clock = pygame.time.Clock()

while being_played == True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        being_played = False

        screen.fill((0, 0, 0))

        #if ball.count > 0:
        #    message = str(ball.count)
        #else:
        #    message = 'You are terrible at life.'

        #text = font.render(message, True, (255, 255, 255), (0, 0, 0)) 
        #text_box = text.get_rect() 
        #text_box.center = (int(board['size']['x']/2), int(board['size']['y']/2))
        #screen.blit(text, text_box)

        paddle.move(pygame.key.get_pressed(), board['size'])
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(int(paddle.location['x']) , int(paddle.location['y']), int(paddle.size['x']), int(paddle.size['y'])))

        ball.move(board['size'], paddle)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(int(ball.location['x']) , int(ball.location['y']), ball.size, ball.size))

        pygame.display.flip()
        clock.tick(60)
