Pi=3.142
radius=int(input("Enter the value of the radius: "))
height=int(input("Enter thr value of the height: "))
def main():
    
    area_of_surfaces()

def area_of_circle():
    circle_area=2 * Pi * (radius **2)
    return circle_area

def area_of_rectangle():
    rectangle_area=Pi * (radius + radius) * height
    return rectangle_area

def area_of_surfaces():
    surface_area= area_of_circle() + area_of_rectangle()
    return surface_area


main()

