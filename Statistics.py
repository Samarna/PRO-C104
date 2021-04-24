import csv
import collections
import statistics

with open ('HeightWeight.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)

    new_data = []
    for i in range(len(file_data)):
        weight = file_data[i][2]
        new_data.append(float(weight))

    # Calculating Mean
    sum = 0
    for i in new_data:
        sum+=i 
        
    mean = sum/len(new_data)
    print("Mean : "+str(mean))
    print(f"Mean : {mean:f}")

    # Calculating Median
    new_data.sort()
    n = len(new_data)
    if len(new_data)%2==0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2-1])
        median = (median1+median2)/2
    else:
        median = new_data[n//2]
    print(str(median))
    print(n)
    
    print(str(statistics.mode(new_data)))
