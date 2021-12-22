from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

r,x,y=10,0,50
R=40
theta=0.0

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
	global x,y,r,R,theta
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)
	x = (r+R)*math.cos(math.pi*theta/180)
	y = (r+R)*math.sin(math.pi*theta/180)
	theta +=1
		
def display():
	global r,R,x,y
	glClear(GL_COLOR_BUFFER_BIT)
	rgb1=(0.0,1.0,1.0)
	rgb2=(1.0,1.0,0.0)
	drawSphere(R,0,0,rgb1)
	drawSphere(r,x,y,rgb2)
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE) 
	glutInitWindowPosition(50,50)
	glutInitWindowSize(768,768)
	glutCreateWindow("Animation_Rolling ball over the sphere")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	glClearScreen()
	glutMainLoop()
main()
