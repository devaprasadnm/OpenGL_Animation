from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math


r=20

x1=-70
y1=0
x2=70
y2=0

angle=0
STATE=1

def clearscreen():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-100,100,-100,100)
	glColor3f(0.0,0.0,1.0)

def update(value):
	global x1,y1,x2,y2,angle,STATE
	glutPostRedisplay()
	glutTimerFunc(int(1000/10),update,0)
	
	
	if STATE==1:
		if angle<10:
			x1,y1,x2,y2=rotation(x1,y1,x2,y2,0,0,angle)
			angle=30
		else:
			STATE=-1
			
	else:
		if angle>-10:
			x1,y1,x2,y2=rotation(x1,y1,x2,y2,0,0,angle)
			angle=-30
			
		else:
			STATE=1
		
		
	
	
	
	
	
	
	
def rotation(x1,y1,x2,y2,xr,yr,angle):
	rad_angle=(math.pi*angle)/180
	
	cosT=math.cos(rad_angle)
	sinT=math.sin(rad_angle)
	
	X1=cosT*(x1-xr)-sinT*(y1-yr)+xr
	Y1=sinT*(x1-xr)+cosT*(y1-yr)+xr
	
	X2=cosT*(x2-xr)-sinT*(y2-yr)+xr
	Y2=sinT*(x2-xr)+cosT*(y2-yr)+xr
	
	return X1,Y1,X2,Y2
	
	
		
	
	
	
	
def drawline(x1,y1,x2,y2):
	glBegin(GL_LINES)	
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()


def drawcircle(x,y,r):
	i=0.0
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_TRIANGLE_FAN)
	
	glVertex2f(x,y)
	while i<360:
		glVertex2f(r*math.cos(math.pi*i/180)+x,r*math.sin(math.pi*i/180)+y)
		i=i+1
	
	glEnd()
	glFlush()

		


def display():
        
	global x1,y1,x2,y2,r
	glClear(GL_COLOR_BUFFER_BIT)
	drawcircle(x1,y1,r)
	drawline(x1,y1,x2,y2)
	drawcircle(x2,y2,r)
	glutSwapBuffers()




def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Seesaw")
	glutDisplayFunc(display)
	glutTimerFunc(0,update,0)
	clearscreen()
	glutMainLoop()
	
main()	