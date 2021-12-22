from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
state=1

x1=-20
x2=20
y1=-50
y2=-50
x3=-50
x4=50
y3=20
y4=20

def clearScreen():
	gluOrtho2D(-100,100,-100,100)
	glClearColor(0.0,.0,0.0,0.0)

	
def drawCircle(xc,yc,r):
	i=0.0
	glColor3f(1.0,1.0,1.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(xc,yc)
	while i<360.0:
		glVertex2f(r*math.cos(math.pi*i/180)+xc,r*math.sin(math.pi*i/180)+yc)
		i=i+0.1
	glEnd()
	glFlush()
	
	
def drawPoints(x,y):
	glColor3f(0.0,0.0,0.0)
	glPointSize(15)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()
	
def drawTriangle(x1,y1,x2,y2,x3,y3):
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POLYGON)
	glEnd()
	glFlush()
	
def drawLines(x1,y1,x2,y2):
	glLineWidth(5)
	glColor3f(1,0.29,0)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()	
	
def drawTriangle(x1,y1,x2,y2,x3,y3):
	edges=[
	[0,1],
	[1,2],
	[2,0]
	]
	
	points=[
	[x1,y1],
	[x2,y2],
	[x3,y3]
	]
	
	setTriangle(edges,points)
	
def setTriangle(edges,points):
	glColor3f(1,0,0)
	glBegin(GL_POLYGON)
	for e in edges:
		for v in e:
			glVertex2fv(points[v])
	glEnd()
	glFlush()
	
def display():	
	glClear(GL_COLOR_BUFFER_BIT)
	drawLines(-20,-20,x1,y1)
	drawLines(20,-20,x2,y2)
	drawLines(-20,20,x3,y3)
	drawLines(20,20,x4,y4)
	drawCircle(0,55,15)
	drawTriangle(2,50,-2,54,-15,38)
	drawPoints(-5,60)
	drawPoints(5,60)
	drawCircle(0,0,40)
	drawPoints(0,20)
	drawPoints(0,0)
	drawPoints(0,-20)
	glutSwapBuffers()
	
def rotation(x1,y1,xr,yr,angle):
	X1=(x1-xr)*math.cos(math.radians(angle))-(y1-yr)*math.sin(math.radians(angle))+xr
	Y1=(x1-xr)*math.sin(math.radians(angle))+(y1-yr)*math.cos(math.radians(angle))+yr
	return X1,Y1
	

def update(values):
	global state,x1,y1,x2,y2,x3,y3,x4,y4
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)
	if state==1:
		x1,y1=rotation(x1,y1,-20,-20,5)
		x2,y2=rotation(x2,y2,20,-20,-5)
		x3,y3=rotation(x3,y3,-20,20,5)
		x4,y4=rotation(x4,y4,20,20,-5)
		state=0
	else:
		
		x1,y1=rotation(x1,y1,-20,-20,-5)
		x2,y2=rotation(x2,y2,20,-20,5)
		x3,y3=rotation(x3,y3,-20,20,-5)
		x4,y4=rotation(x4,y4,20,20,5)
		state=1
	
		

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE )
	glutInitWindowPosition(50,50)
	glutInitWindowSize(800,800)
	glutCreateWindow("SnowMan")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	clearScreen()
	glutMainLoop()
	
main()
	
