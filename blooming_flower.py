from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
ang1=0
theta1=0
a1,b1,x1,y1,p1,q1=-10,10,10,10,0,50
a2,b2,x2,y2,p2,q2=-10,10,10,10,0,50
a3,b3,x3,y3,p3,q3=-10,10,10,10,0,50
a4,b4,x4,y4,p4,q4=-10,10,10,10,0,50
a5,b5,x5,y5,p5,q5=-10,10,10,10,0,50

def clearScreen():
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
	glClearColor(0,0,0,0)
	
def drawTriangle(x1,y1,x2,y2,x3,y3):
	glColor3f(1,0,0)
	glBegin(GL_POLYGON)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glEnd()
	glFlush()
	
def drawCircle(xc,yc,r):
	#glColor3f(1,1,0)
	i=0.0
	glBegin(GL_TRIANGLE_FAN)
	while i<360.0:
		glVertex2f(r*math.cos(math.radians(i))+xc,r*math.sin(math.radians(i))+yc)
		i+=0.1
	glEnd()
	glFlush()
	
def update(values):
	global a1,b1,x1,y1,p1,q1,a2,b2,x2,y2,p2,q2,a3,b3,x3,y3,p3,q3,a4,b4,x4,y4,p4,q4,ang1,theta1
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)
	
	if ang1<30:
		ang1=ang1+0.2
		a1,b1,x1,y1,p1,q1=rotation(a1,b1,x1,y1,p1,q1,0,0,0.1)
		a2,b2,x2,y2,p2,q2=rotation(a2,b2,x2,y2,p2,q2,0,0,-0.1)
		a3,b3,x3,y3,p3,q3=rotation(a3,b3,x3,y3,p3,q3,0,0,0.2)
		a4,b4,x4,y4,p4,q4=rotation(a4,b4,x4,y4,p4,q4,0,0,-0.2)
		
	
	
	
	
	
def rotation(x1,y1,x2,y2,x3,y3,xc,yc,angle):
	cosT=math.cos(math.radians(angle))
	sinT=math.sin(math.radians(angle))
	X1 = (x1-xc)*cosT-(y1-yc)*sinT+xc
	Y1 = (x1-xc)*sinT+(y1-yc)*cosT+yc
	X2 = (x2-xc)*cosT-(y2-yc)*sinT+xc
	Y2 = (x2-xc)*sinT+(y2-yc)*cosT+yc
	X3 = (x3-xc)*cosT-(y3-yc)*sinT+xc
	Y3 = (x3-xc)*sinT+(y3-yc)*cosT+yc
	
	return X1,Y1,X2,Y2,X3,Y3
	
def drawLines(x1,y1,x2,y2):
	glColor3f(0,1,0)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)	
	glEnd()
	glFlush()
	
def display():
	global a1,b1,x1,y1,p1,q1,a2,b2,x2,y2,p2,q2,a3,b3,x3,y3,p3,q3,a4,b4,x4,y4,p4,q4
	glClear(GL_COLOR_BUFFER_BIT)
	drawTriangle(a1,b1,x1,y1,p1,q1)
	drawTriangle(a2,b2,x2,y2,p2,q2)
	drawTriangle(a3,b3,x3,y3,p3,q3)
	drawTriangle(a4,b4,x4,y4,p4,q4)
	drawTriangle(a5,b5,x5,y5,p5,q5)
	drawTriangle(a1,b1,x1,y1,p1,q1)
	drawCircle(0,0,15)
	drawLines(0,-10,0,-50)
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(800,800)
	glutCreateWindow("flower")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	clearScreen()
	glutMainLoop()
	
main()
