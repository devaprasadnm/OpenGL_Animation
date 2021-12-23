from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

xc,yc=20,50
x1,y1,x2,y2=20,50,20,20
x3,y3,x4,y4=20,40,15,35 #left hand
x5,y5,x6,y6=20,40,25,35 # right hand
x7,y7,x8,y8=20,20,15,15
x9,y9,x0,y0=20,20,25,15

state =1
down=1
angle=0

def clearScreen():
	gluOrtho2D(0,100,0,100)
	glClearColor(0,0,0,0)
	

def drawSphere(r,xc,yc):
	i=0.0
	glBegin(GL_TRIANGLE_FAN)
	while i<360.0:
		glVertex2f(r*math.cos(math.radians(i))+xc, r*math.sin(math.radians(i))+yc)
		i=i+0.1
	glEnd()
	glFlush()
	
def drawLines(x1,y1,x2,y2):
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()
	
	
def update(values):
	global xc,yc,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x0,y0,state,down,angle
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)
	
	if down ==1:
		if angle<10:
			x4,y4=rotation(x4,y4,x3,y3,angle)
			x6,y6=rotation(x6,y6,x5,y5,-angle)
			x8,y8=rotation(x8,y8,x7,y7,angle)
			x0,y0=rotation(x0,y0,x9,y9,-angle)
			angle=angle+1
		else:
			down=0
	else:
		if angle>-10:
			x4,y4=rotation(x4,y4,x3,y3,angle)
			x6,y6=rotation(x6,y6,x5,y5,-angle)
			x8,y8=rotation(x8,y8,x7,y7,angle)
			x0,y0=rotation(x0,y0,x9,y9,-angle)
			angle=angle-1
		else:
			down=1
	
	if state==1:
		if x6<100:
			speed=1
			xc,x1,x2,x3,x4,x5,x6,x7,x8,x9,x0=xc+speed,x1+speed,x2+speed,x3+speed,x4+speed,x5+speed,x6+speed,x7+speed,x8+speed,x9+speed,x0+speed
		else:
			state=2
	else:
		if x5>0:
			speed=-1
			xc,x1,x2,x3,x4,x5,x6,x7,x8,x9,x0=xc+speed,x1+speed,x2+speed,x3+speed,x4+speed,x5+speed,x6+speed,x7+speed,x8+speed,x9+speed,x0+speed
		else:
			state=1
	

def rotation(x1,y1,xc,yc,angle):
	X1=(x1-xc)*math.cos(math.radians(angle))-(y1-yc)*math.sin(math.radians(angle))+xc
	Y1=(x1-xc)*math.sin(math.radians(angle))+(y1-yc)*math.cos(math.radians(angle))+yc	
	
	return X1,Y1
	
def display():
	global xc,yc,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x0,y0
	glClear(GL_COLOR_BUFFER_BIT)
	drawSphere(5,xc,yc)#head
	drawLines(x1,y1,x2,y2)# body x1,y1
	drawLines(x3,y3,x4,y4)# left Hand
	drawLines(x5,y5,x6,y6)# right hand
	drawLines(x7,y7,x8,y8)# left leg
	drawLines(x9,y9,x0,y0)# right leg
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	glutInitWindowSize(800,800)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Man_Walking")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	clearScreen()
	glutMainLoop()
	
main()
