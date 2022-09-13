import math
import csv

def fizz_buzz_game():
    flag = False
    for i in range (1,101):
        flag = True
        if(i % 3 == 0):
            print("Fizz", end = "")
            flag = False
        if i % 5 == 0:
            print("Buzz", end = "")
            flag = False
        if flag:
            print(i, end = "")
        print("\n")

def sphere_volume(radius):
    return(4.0 / 3.0 * math.pi * radius * radius * radius)

def divide_with_error_handling(a,b):
    try:
        return a/b
    except:
        print("Warning, can't divide by zero")
    return 1

def decode_csv_data_into_dictionary(filename):
    destination_dict = []
    filereader = csv.DictReader(open(filename))
    for line in filereader:
        destination_dict.append(line)
    
    #with open(filename) as csvfile:
        #destination_dict = dict(csv.DictReader(csvfile))
        #destination_dict = dict(filter(None, csv.reader(file)))

    #data_file = csv.DictReader(open("data.csv", "r"))
    #for row in data_file:
    #    a,b = row
    #    destination_dict[a] = b
    print(destination_dict)
    return destination_dict


decode_csv_data_into_dictionary("data.csv")
        
