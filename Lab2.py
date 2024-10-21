print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temperature= input() 
    y=temperature.split(",")
    z= [float(item) for item in y]
    calc_average_temperature(z)
    calc_min_max_temperature(z)
    median_temperature(z)


def display_main_menu():
    print("Temperature calculation, input all the temperatures gathered by separating with a comma ","")



def median_temperature(z):
    sorted=z.sort()
    length= len(z)

    if length%2==1:
        median_value= z[length//2]
    else: 
        median_value=(z[length // 2 - 1] + z[length // 2]) / 2

    print("The median temperature: "+ str(median_value))

def calc_average_temperature(z): 
     total_sum=sum(z)
     count= len(z)
     average= total_sum/count
     print("The calculated average value of all temperature: "+ str(average))


def calc_min_max_temperature(z): 
    max_value= max(z)
    min_value= min(z)
    print("Maximum Value "+ str(max_value))
    print("Minimum Value "+ str(min_value))

if __name__ == "__main__":
    main()