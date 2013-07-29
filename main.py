from kivy.config import Config
Config.set('graphics','resizable',0)


from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line
from random import random, randint
from kivy.core import window
import time
from math import sqrt
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
		self.alive = True

	def draw(self):
		Color(self.colorRGB[0],self.colorRGB[1],self.colorRGB[2])
		Ellipse(pos=(self.x,self.y), size = (self.ball_size,self.ball_size))

	def getCenter(self):
		ballCenterX = self.x+(self.ball_size/2)
		ballCenterY = self.y+(self.ball_size/2)	
		return ballCenterX,ballCenterY

	def collision(self,bubbles):
		#calculate center of ball
		ballX,ballY = self.getCenter()
		for bubble in bubbles:
			if bubble.isAlive:
				bubX,bubY = bubble.getCenter()
				print "test",(sqrt((bubX-ballX)**2 * (bubY + ballY)**2))
				if sqrt((bubX-ballX)**2 + (bubY - ballY)**2) < ((self.ball_size + bubble.size1)/2):
					self.alive = False
					return True
		return False

	def update(self):
		if self.alive:
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
		self.size1 = 80
		self.x = x-(self.size1/2)
		self.y = y-(self.size1/2)
		self.createdTime = time.clock()
		self.size1 = 80
		self.isAlive = True
		self.lifespan = 2 #seconds to stay alive

	def getCenter(self):
		bubbleCenterX = self.x+(self.size1/2)
		bubbleCenterY = self.y+(self.size1/2)	
		return bubbleCenterX,bubbleCenterY

	def draw(self):
		Color(self.colorRGB[0],self.colorRGB[1],self.colorRGB[2])
		Ellipse(pos=(self.x, self.y), size=(self.size1, self.size1))

	def update(self):
		if time.clock() - self.createdTime > self.lifespan:
			self.isAlive = False
		else:
			self.draw()


class BubblePop(Widget):
	balls = []
	bubbles = []
	levelSize = 0
	def test(self):
		self.levelSize = 5

	def SetupLevel(self,numballs):
		self.btn1 = Button(text='Hello world 1')
		self.btn1.bind(on_press=self.callback)
		balls = []
		bubbles = []
		for x in xrange(numballs):
			ball = Ball(self.width,self.height)
			self.balls.append(ball)

	def callback(self,instance):
		self.SetupLevel()

	def on_resize(self,width, height):
		print "window resized" * 100
		for ball in balls:
			ball.windowHeight = height
			ball.windowWidth = width
	def on_touch_down(self,touch):
		with self.canvas:
			temp = Bubble(touch.x,touch.y)
			self.bubbles.append(temp)


	def update(self,dt):
		self.btn1 = Button(text='Hello world 1')
		if len(self.balls) == 0:
			levelSize = 5
			BubblePop.SetupLevel(self,levelSize)
			levelSize += 5
		with self.canvas:
			self.canvas.clear()
			for ball in self.balls:
				if not ball.alive:
					continue
				ball.update()
				if ball.collision(self.bubbles):
					temp = Bubble(ball.x,ball.y)
					self.bubbles.append(temp)
			for bubble in self.bubbles:
				bubble.update()

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