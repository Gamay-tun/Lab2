def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    calculate_bmi()
    # display_main_menu()
    # get_user_input()

def calculate_bmi(height,weight):
    print("Height= "+str(height))
    print("Weight= "+str(weight))

    bmi= weight/(height*height)
    print("BMI is "+ str(bmi) )

    if(bmi< 18.5):
        print("Under Weight")
        return -1
    elif(18.5<=bmi<= 25.0):
        print("Normal Weight")
        return 0
    elif(bmi>25.0):
        print("Over Weight")
        return 1
<<<<<<< HEAD

=======
>>>>>>> f15d1d301eae0f2f79cb95597200b98c7a8783f9
# def display_main_menu():
#     print("Enter some numbers separated by commas (e.g. 5,67, 32)")

# def calc_average():
#     print("calc_average")

# def get_user_input():
#     x=input()
#     y=x.split(",")

#     z= [float(item) for item in y]
#     print("your input numbers: "+str(z))


calculate_bmi(weight=57, height=1.73)

# main()