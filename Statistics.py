import csv
import collections
import statistics

with open ('HeightWeight.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)

    new_data = []
    for i in range(len(file_data)):
        height = file_data[i][1]
        new_data.append(float(height))

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

    #Calculating Mode
    data = collections.Counter(new_data)
    mode_range = {"50-60":0,"60-70":0,"70-80":0}
    for height,occurance in data.items():
        if 50<float(height)<60:
            mode_range["50-60"]+=occurance

        elif 60<float(height)<70:
            mode_range["60-70"]+=occurance
        
        elif 70<float(height)<80:
            mode_range["70-80"]+=occurance
    #print(mode_range)

    m_range,m_occurance = 0,0
    for range,occurance in mode_range.items():
        if occurance>m_occurance:
            m_range,m_occurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance
    mode = float((m_range[0]+m_range[1])/2)
    print(mode)

    print(str(statistics.mode(new_data)))