import random
import tkinter as tk
import  math


class Projekt:
    def __init__(self, window, center_x = 400, center_y = 400):
        self.window = window
        self.window.title("Projekt")
        self.canvas = tk.Canvas(height = 2 * center_y, width = 2 * center_x)
        self.canvas.pack()
        
        self.center_x = center_x
        self.center_y = center_y
        self.r_bigger = round(9/10 * center_x)  # radius of bigger circle 
        self.r_smaller = round(5/10 * center_x) # radius of smaller circle

        self.create_points() # calls funtion to create list of points

    def create_points(self, number_points = 40): #creates desired number of points
        self.list_points = []
        while len(self.list_points) < number_points:
            x = random.uniform(1/10 * self.center_x, 19/10 * self.center_x) # randomly selected x
            y = random.uniform(1/10 * self.center_y, 19/10 * self.center_y) # randomly selected y
            R = self.r_bigger
            r = self.r_smaller
            if (400 - x) ** 2 + (400 - y) ** 2 <= R**2 and (400 - x) ** 2 + (400 - y) ** 2 >= r**2: # checks if point (x,y) is in annulus 
                point = (x,y)
                self.list_points.append(point) # adds point (x,y) to list of points called list_points
        
        self.arrange() # calls funtion arrange
    
    def arrange(self): # sorts list to get leftmost point
        self.list_points.sort(key=lambda tup: tup[0])

        # start functions
        self.draw_points()
        self.draw_bigger_circle()
        self.draw_smaller_circle()
        self.convex_hull()
        
    def draw_points(self): # draws all points
        for point in self.list_points:
            x = point[0]
            y = point[1]
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2)
            
    def draw_bigger_circle(self): #makes outer circle
        self.canvas.create_oval(self.center_x - self.r_bigger,
                                self.center_y - self.r_bigger,
                                self.center_x + self.r_bigger,
                                self.center_y + self.r_bigger
                                )
        
    def draw_smaller_circle(self): #makes inner circle
        self.canvas.create_oval(self.center_x - self.r_smaller,
                                self.center_y - self.r_smaller,
                                self.center_x + self.r_smaller,
                                self.center_y + self.r_smaller
                                )

    def convex_hull(self): #returns points of convex hull (with gift-wraping algorithm)
        
        # add first point (most left of all)
        first_point = self.list_points[0]
        self.end_list = [first_point]
        x = first_point[0]
        y = first_point[1]

        # add second point
        max_angle = 90
        counter = 1
        length_list = len(self.list_points)
        while counter < length_list:
            point = self.list_points[counter]
            try:
                angle = round(math.degrees(math.atan((y - point[1]) / (x - point[0]))),4)
            except:
                if y < point[1]:
                    angle = 0
                else:
                    angle = 180
            if angle <= max_angle:
                max_angle = angle
                new_point = point
                index = counter
            counter += 1
        self.end_list.append(new_point)            
        del self.list_points[index]
        
        previous_angle = max_angle
        if point[1] > y  and point[0] > x:
            previous_angle += 90
        elif point[1] > y  and point[0] < x:
            previous_angle += 270
        elif point[1] < y  and point[0] < x:
            previous_angle += 270
        else: # point[1] < y  and point[0] > x:
            previous_angle += 90

        # add all other points of convex hull
        while new_point != self.end_list[0]:
            max_angle = 360
            counter = 0
            index = 0
            length_list = len(self.list_points)

            last_in_end = self.end_list[-1]
            x = last_in_end[0]
            y = last_in_end[1]

            while counter < length_list:
                point = self.list_points[counter]
                try: # if poins are not one above the other do this
                    angle = round(math.degrees(math.atan((y - point[1]) / (x - point[0]))),4)
                    if point[1] > y  and point[0] > x:
                        angle = angle + 90
                    elif point[1] > y  and point[0] < x:
                        angle = angle + 270
                    elif point[1] < y  and point[0] < x:
                        angle = angle + 270
                    else: # point[1] < y  and point[0] > x:
                        angle = angle + 90
                except: 
                    if point[1] > y:
                        angle = 180
                    else:
                        angle = 360
                
                    
                if angle < previous_angle: # angles get bigger every time (or at least don't get smaller)
                    angle += 360
                else:
                    angle = angle
                    
                if angle <= max_angle:
                    max_angle = angle
                    new_point = point
                    index = counter
                
                counter += 1
            previous_angle = max_angle
            self.end_list.append(new_point)
            del self.list_points[index]

        # start two functions
        self.draw_lines()
        self.hull_length()
        self.hull_area()

                
    def draw_lines(self): # draws lines between points
        counter = 0
        length_list = len(self.end_list)
        
        while counter < length_list - 1:
            point1 = self.end_list[counter]
            point2 = self.end_list[counter + 1]
            x1 = point1[0]
            y1 = point1[1]
            x2 = point2[0]
            y2 = point2[1]

            self.canvas.create_line(x1, y1, x2, y2)
            counter += 1

    def hull_length(self): # calcules hull length
        counter = 0
        length_list = len(self.end_list)
        total_length = 0
        
        while counter < length_list - 1:
            point1 = self.end_list[counter]
            point2 = self.end_list[counter + 1]
            
            x1 = point1[0]
            y1 = point1[1]
            x2 = point2[0]
            y2 = point2[1]

            line = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
            total_length += line
            counter += 1
            
        print("Length of convex hull is: ", round(total_length,2))
        print("Length of outer circle is: ",round((math.pi) * 2 * self.r_bigger,2))

    def hull_area(self): # calculates hull area
        total_area = 0
        counter = 1
        number_of_points = len(self.end_list)
        while counter < number_of_points - 2:
            point1 = self.end_list[0]
            point2 = self.end_list[counter]
            point3 = self.end_list[counter + 1]
            
            x1 = point1[0]
            y1 = point1[1]
            x2 = point2[0]
            y2 = point2[1]
            x3 = point3[0]
            y3 = point3[1]

            side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
            side2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1/2)
            side3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1/2)

            kot_cos = (side1 ** 2 + side2 ** 2 - side3 ** 2) / (2 * side1 * side2) 
            kot = math.degrees(math.acos(kot_cos))
            kot_sin =  abs(math.sin(math.acos(kot_cos)))
            
            area = side1 * side2 * kot_sin / 2
            total_area += area
            counter += 1

            
        print("Area of smaller circle is: ", round(math.pi * (self.r_smaller ** 2),2))
        print("Convex hull area is:", round(total_area,2))
        print("Area of bigger circle is: ", round(math.pi * (self.r_bigger ** 2),2)) 
            






    

window = tk.Tk()
moj_stevec = Projekt(window)
window.mainloop()
