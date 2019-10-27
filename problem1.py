#Sean Dehghani
#HOMEWORK5-PROBLEM1

import math

class Point():
    """ On this class we are creating a point in 2-dimensional space,
with and X, Y coordinatoors. """
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def translate(self, s, t):#Translates the point by (s, t). 
        self.x = self.x + s #s
        self.y = self.y + t #t
        return self.x, self.y
    
    def rotate(self, θ):# Rotate the point by an angle θ
        θ=math.radians(θ)
        a= (self.x*(math.cos(θ))) - (self.y*(math.sin(θ)))
        b= (self.x*(math.sin(θ))) + (self.y*(math.cos(θ)))
        self.x=a
        self.y=b
        return self.x, self.y

    def distance(self, p):# calculate the distance between the point and another point p
        result=math.sqrt(((self.x - p.x)**2) + ((self.y - p.y)**2))
        return result

    def left_of(self, q, r):#It returns True if the point lieso the left of →r, and False otherwise
        if (((r.x*self.y) - (self.x*r.y)) + ((q.x*r.y) - (q.x*self.y)) + ((q.y*self.x) - (q.y*r.x))) > 0:
            return True
        else:
            return False
        
    def right_of(self, q, r):#It returns True if the pointies to the right of →r, and False otherwise.
        if (((r.x*self.y) - (self.x*r.y)) + ((q.x*r.y) - (q.x*self.y)) + ((q.y*self.x) - (q.y*r.x))) < 0:
            return True
        else:
            return False

    def __str__ (self):
        return "(" + str(self.x) + ", "+ str(self.y)+ ")"
    def __repr__(self):
        return "(" + str(self.x) + ", "+ str(self.y)+ ")"

class SimplePoly():
    """this class is a simple polygons.
The constructor takes an arbitrary number of points as parameters, where
the points are listed in counter-clockwise order about the boundary. The parameter
to the constructor should be of the form *vertices"""
    def __init__(self, *vertices):
        self.pointlist=[]
        for points in vertices:
            self.pointlist.append(points)

    def translate(self, s, t):
        for p in self.pointlist:
            Point.translate(p,s,t)
        return self
        

    def rotate(self, θ):
        for p in self.pointlist:
            Point.rotate(p, θ)
        return self

    def __iter__(self):
        self.count = 0 #self.pointlist
        self.currentpoint = self[0]
        return self

    def __next__(self):
        if self.count == 0: # returning the first item in the list and updating the counter
            self.count += 1
            return self.currentpoint 
        elif self.count< len(self):#return item 1 through the last item
            self.count +=1
            self.currentpoint = self[self.pointlist.index(self.currentpoint)+1]
            return self.currentpoint
        else:
            raise StopIteration
            
    def __len__(self):
        return len(self.pointlist) #return the lenght of the point list

    def __getitem__(self, i):
        if i < len(self) and i >= 0: #self=self.pointlist
            return self.pointlist[i]
        else:
            raise IndexError
        
    def __str__(self):
        points_string = ""
        for i in self:
            points_string += str(i) + " "
        return points_string
        

    def perimeter(self):
        a= 0
        for p in range(len(self)):
            distance= Point.distance(self.pointlist[p-1],self.pointlist[p])
            a+= distance
        return a
            
            

     

class ConvPoly(SimplePoly):
    """compare the points to the previous 2 points in the list"""
    def __init__ (self, *vertices):
        SimplePoly.__init__(self, *vertices)
        for p in range(len(self)):
            if Point.left_of (self[p], self.pointlist[p-2], self.pointlist[p-1]):
                pass
            else:
                raise Error


class EquiTriangle(ConvPoly):
    """, this class is a subclass of the ConvPoly class.
This class customizes one method (the constructor) and
extends one method (area)."""
    def __init__ (self,length):
        self.length = length
        point1=Point(0,0)
        point2=Point(self.length,0)
        point3=Point(self.length/2, self.length/2*math.sqrt(3))
        ConvPoly.__init__(self,point1,point2,point3)
        
    def area(self):#calculates the area of the equilateral triangle
        return math.sqrt(3)*self.length**2/4
        


class Rectangle(ConvPoly):
    """Creating the rectangle class.Since a rectangle is a
convex polygon, this class is a subclass of the ConvPoly class."""
    def __init__(self , length, width):
        self.length = length
        self.width = width
        point1=Point(0,0)
        point2=Point(self.length, 0)
        point3=Point(self.length, self.width)
        point4=Point(0,self.width)
        ConvPoly.__init__(self,point1,point2,point3,point4)
        
    def area(self):#calculating the area of the rectangle
        return self.length*self.width
    
class Square(Rectangle):
    """Craeting the Rectangle class.Since a square is a rectangle,
this class is a subclass of the Rectangle class."""
    def __init__ (self, length):#in square width and length are equal
        Rectangle.__init__(self, length, length)
        self.width = length




