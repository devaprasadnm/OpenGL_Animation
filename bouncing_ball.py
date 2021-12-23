from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

r,x,y=10,-90,10
state = 1


def glClearScreen():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
	
def drawSphere(rad,xc,yc,rgb):
	glColor3f(rgb[0],rgb[1],rgb[2])
	glVertex2f(xc,yc)
	i=0
	glBegin(GL_TRIANGLE_FAN)
	while(i<360.0):
	
		glVertex2f(rad*math.cos(math.pi*i/180)+xc,rad*math.sin(math.pi*i/180)+yc)
		i=i+0.1
	glEnd()
	glFlush()
	
def update(value):
	global x,y,r,state
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)
	if state ==1 :
		if y<70:
			y+=1.5
			x+=0.5
		else:
			state = 0
	else:
		if y>10:
			y-=1.5
			x+=0.5
		else:
			state=1
			
def drawLine():
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_LINES)
	glVertex2f(-100,0)
	glVertex2f(100,0)
	glEnd()	

def display():
	global r,x,y
	glClear(GL_COLOR_BUFFER_BIT)
	rgb1=(0.0,1.0,1.0)
	drawSphere(r,x,y,rgb1)
	drawLine()
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE) 
	glutInitWindowPosition(50,50)
	glutInitWindowSize(768,768)
	glutCreateWindow("Animation_Bouncing ball")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	glClearScreen()
	glutMainLoop()
main()
