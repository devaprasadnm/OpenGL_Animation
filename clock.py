from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

r,x,y=10,0,50
R=40
thetas=0.0
thetah=0.0
thetam=0.0
x1,y1,s2,S2,m2,M2,h2,H2=0,0,0,20,0,30,15,0

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
		i=i+6
	glEnd()
	glFlush()



def update(value):
	global thetas,thetah,thetam,s2,S2,m2,M2,h2,H2
	glutPostRedisplay()
	glutTimerFunc(int(1000),update,0)
	thetas =(6)
	s2,S2 =rotation(s2,S2,0,0,thetas)
	thetam =(0.1)
	m2,M2 =rotation(m2,M2,0,0,thetam)
	thetas =(360/(60*60*60))
	h2,H2 =rotation(h2,H2,0,0,thetah)
	
	
	
def setline(x1,y1,x2,y2,rgb):
	glColor3f(rgb[0],rgb[1],rgb[2])
	glPointSize(10)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()
	
def rotation(x1,y1,xr,yr,theta):
	X1=(x1-xr)*math.cos(math.pi*theta/180)+(y1-yr)*math.sin(math.pi*theta/180)+xr
	Y1=-(x1-xr)*math.sin(math.pi*theta/180)+(y1-yr)*math.cos(math.pi*theta/180)+yr
	return(X1,Y1)

def drawline(x1,y1,x2,y2):
	rgb=(1.0,0.0,0.0)
	setline(x1,y1,x2,y2,rgb)
	
		
def display():
	global r,R,x,y,x1,y1,s2,S2,m2,M2,h2,H2
	glClear(GL_COLOR_BUFFER_BIT)
	rgb1=(0.0,1.0,1.0)
	rgb2=(0.0,0.0,0.0)	
	drawSphere(R,0,0,rgb1)
	drawSphere(35,0,0,rgb2)
	drawline(x1,y1,s2,S2)
	drawline(x1,y1,m2,M2)
	drawline(x1,y1,h2,H2)
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB) 
	glutInitWindowPosition(50,50)
	glutInitWindowSize(768,768)
	glutCreateWindow("clock")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	glClearScreen()
	glutMainLoop()
main()
