
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

xc=0
yc=0
r=10
r1=80
r2=40
angle=0
def clearscreen():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-100.0,100.0,100.0,-100.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(5.0)

def update(value):
	global xc,yc,angle	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))
	xc=80*math.cos(angle)
	yc=40*math.sin(angle)
	angle=angle+0.1
	



def setpixel(x,y):
	glBegin(GL_POINTS)
	glColor3f(0.0,0.0,1.0)
	glVertex2f(x,y)
	glEnd()
	glFlush()
	

def drawcircle(xc,yc,r):
	i=0.0
	glColor3f(1.0,1.0,0.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(xc,yc)
	
	while i<360:
	
		glVertex2f(r*math.cos(math.pi*i/180)+xc,r*math.sin(math.pi*i/180)+yc)
		i=i+0.1
		 
	glEnd()
	glFlush()
	
 
def drawellipse(r1,r2,xc,yc):
	x,y=r1,0
	angle=0
	while angle<360:
	
		x=r1*math.cos(angle)
		y=r2*math.sin(angle)
		angle=angle+0.1
		setpixel(x,y)
			
	


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	global xc,yc,r
	drawcircle(0,0,20)
	drawellipse(80,40,0,0)
	drawcircle(xc,yc,r)
	glutSwapBuffers()
	







def main():
       
	    glutInit()
	    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	    
	    glutInitWindowSize(500,500)
	    glutInitWindowPosition(200,200)
	    
	    glutCreateWindow("Solar system")
	    
	   
	    glutDisplayFunc(display)
	    glutTimerFunc(0,update,0)	     
	    clearscreen()
	    glutMainLoop()
main()	     
	     
	     
	     
	     
	              
	    
	    
	    
	    	