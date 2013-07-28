from kivy.config import Config
Config.set('graphics','resizable',0)



from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse
from random import random, randint
from kivy.core import window
import time

#balls are what bounce around the screen. They turn into bubbles upon 
#colliding with a bubble.
numballs = 5

class Ball(Widget):
	def __init__(self,width,height):
		self.ball_size = 20
		self.x = randint(0,width-self.ball_size)
		self.y = randint(0,height-self.ball_size)
		self.windowWidth = width
		self.windowHeight = height
		print "created ball at: ",self.x,":",self.y
		self.colorRGB = [random(),random(),random()]
		self.velX = 3
		self.velY = 3

	def draw(self):
		Color(self.colorRGB[0],self.colorRGB[1],self.colorRGB[2])
		Ellipse(pos=(self.x,self.y), size = (self.ball_size,self.ball_size))

	def collision(self,bubbles):
		#calculate center of ball
		#ballCenterX = 
		pass
	def update(self):
		self.x += self.velX
		self.y +=  self.velY
		if self.x < 0 or self.x > self.windowWidth-self.ball_size:
			self.velX *= -1
		if self.y < 0 or self.y > self.windowHeight-self.ball_size:
			self.velY *= -1
		self.draw()

class Bubble(Widget):

	def __init__(self,x,y):
		self.colorRGB = [random(),random(),random()]
		self.x = x
		self.y = y
		self.createdTime = time.clock()
		self.size = 80
		isAlive = True
		lifespan = 3 #seconds to stay alive

	def draw(self):
		Color(self.colorRGB[0],self.colorRGB[1],self.colorRGB[2])
		Ellipse(pos=(self.x, self.y), size=(size, size))

	def update(self):
		if time.clock() - createdTime > lifespan:
			isAlive = False
		else:
			self.draw()



class BubblePop(Widget):
	balls = []
	bubbles = []
	levelSize = 0
	def test(self):
		self.levelSize = 5

	def SetupLevel(self,numballs):
		for x in xrange(numballs):
			print self.width,self.height
			ball = Ball(self.width,self.height)
			self.balls.append(ball)

	def on_resize(self,width, height):
		print "window resized" * 100
		for ball in balls:
			ball.windowHeight = height
			ball.windowWidth = width
	def on_touch_down(self,touch):
		with self.canvas:
			pass


	def update(self,dt):
		if len(self.balls) == 0:
			levelSize = 5
			BubblePop.SetupLevel(self,levelSize)
			levelSize += 5
		with self.canvas:
			self.canvas.clear()
			for ball in self.balls:
				ball.update()

class BubblePopApp(App):
	def build(self):
		print "test"
		game = BubblePop()
		game.test()
		game.levelSize = 5
		Clock.schedule_interval(game.update, 1.0/60.0)
		return game


if __name__ == '__main__':
	BubblePopApp().run()