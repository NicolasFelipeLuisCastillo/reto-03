class Point:
    def __init__(self, x:float, y:float):
        self.x: float = x
        self.y: float = y
        
class Rectangle:
    def __init__(self, method:int):
        self.method = method

    def inicialice_rectangle(self, point1:Point, point2:Point, width:float, height:float):
      if self.method == 1:  
        print(f"""Rectangle with width {width} and height {height}:
              Point 1: {point1.x},{point1.y}
              Point 2: {point1.x + width},{point1.y}
              Point 3: {point1.x},{point1.y + height}
              Point 4: {point1.x + width},{point1.y + height}""")
      elif self.method == 2:
        print(f"""Rectangle with width {width} and height {height}:
              Point 1: {point1.x-(width/2)},{point1.y-(height/2)}
              Point 2: {point1.x+(width/2)},{point1.y-(height/2)}
              Point 3: {point1.x+(width/2)},{point1.y+(height/2)}
              Point 4: {point1.x-(width/2)},{point1.y+(height/2)}""")
      elif self.method == 3:
        if point2.x > point1.x and point2.y > point1.y:
          print(f"""Rectangle with width {width} and height {height}:
                Point 1: {point1.x},{point1.y}
                Point 2: {point2.x},{point1.y}
                Point 3: {point2.x},{point2.y}
                Point 4: {point1.x},{point2.y}""")
        elif point2.x < point1.x and point2.y < point1.y:
          print(f"""Rectangle with width {width} and height {height}:
                  Point 1: {point2.x},{point2.y}
                  Point 2: {point1.x},{point2.y}
                  Point 3: {point1.x},{point1.y}
                  Point 4: {point2.x},{point1.y}""")
        elif point2.x > point1.x and point2.y < point1.y:
          print(f"""Rectangle with width {width} and height {height}:
                  Point 1: {point1.x},{point2.y}
                  Point 2: {point2.x},{point2.y}
                  Point 3: {point2.x},{point1.y}
                  Point 4: {point1.x},{point1.y}""")
        elif point2.x < point1.x and point2.y > point1.y:
          print(f"""Rectangle with width {width} and height {height}:
                  Point 1: {point2.x},{point1.y}
                  Point 2: {point1.x},{point1.y}
                  Point 3: {point1.x},{point2.y}
                  Point 4: {point2.x},{point2.y}""")
          
    def compute_area(self, width:float, height:float):
        return width * height
    
    def compute_perimeter(self, width:float, height:float):
        return 2 * (width + height)
    
class Square(Rectangle):
    def __init__(self, method:int):
        super().__init__(method)
        
    def inicialice_square(self, point:Point, side:float):
        if self.method == 1:
          print(f"""Square with side {side}:
                Point 1: {point.x},{point.y}
                Point 2: {point.x + side},{point.y}
                Point 3: {point.x},{point.y + side}
                Point 4: {point.x + side},{point.y + side}""")
        elif self.method == 2:
          print(f"""Square with side {side}:
                Point 1: {point.x-(side/2)},{point.y-(side/2)}
                Point 2: {point.x+(side/2)},{point.y-(side/2)}
                Point 3: {point.x+(side/2)},{point.y+(side/2)}
                Point 4: {point.x-(side/2)},{point.y+(side/2)}""")
        elif self.method == 3:
          print(f"""Square with side {side}:
                Point 1: {point.x},{point.y}
                Point 2: {point.x + side},{point.y}
                Point 3: {point.x + side},{point.y + side}
                Point 4: {point.x},{point.y + side}""")
                
    def compute_area(self, side:float):
        return side * side
    
    def compute_perimeter(self, side:float):
        return 4 * side
point1 = Point(0,0)
point2= Point(-5,3)
rectangle1 = Rectangle(3)

print(rectangle1.inicialice_rectangle(point1, point2, -5, -3))