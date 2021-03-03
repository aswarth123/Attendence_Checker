
import csv
import pandas as pd
import datetime

def name_conversion(f):
    names = []
    with open(f, 'r') as file:
        csv_file = csv.DictReader(file)
        i=1
        for row in csv_file:
            if(len(row['Roll no.'])==0):
                continue
            elif(i<10):
                names.append(row['Full Name']+'-'+'AM.EN.U4CSE1900'+row['Roll no.'])
            else:
                names.append(row['Full Name']+'-'+'AM.EN.U4CSE190'+row['Roll no.'])
    return(names)

def absentees_list_generator(names,attcsv,classDur,percent_att):
    with open("attendenceLists/"+ attcsv, 'r',encoding='utf16', errors='ignore') as file:
        csv_file = csv.DictReader(file)
        i=1
        final_list = []
        for row in csv_file:
            temp = (row['Full Name\tUser Action\tTimestamp']+row[None][0]).split('\t')
            date = temp.pop()
            format = '%m/%d/%Y %H:%M:%S %p'
            obj_date = datetime.datetime.strptime(date, format)
            temp.append(obj_date)
            final_list.append(temp)
    '''df = pd.read_csv("attendenceLists/"+ attcsv)
    print(df.head())'''
    print(final_list)
    

if __name__ == "__main__":
    names = name_conversion("classList/names.csv")
    print(names[5])
    print(names[15])
    attcsv = input()
    absentees_list_generator([],attcsv,1,70)
