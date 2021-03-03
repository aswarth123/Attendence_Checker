
import csv
import pandas as pd
import datetime

def name_conversion(f):
    names = []
    with open(f, 'r') as file:
        csv_file = csv.DictReader(file)
        i=1
        for row in csv_file:
            temp = []
            if(len(row['Roll no.'])==0):
                continue
            elif(i<9):
                temp.append(row['Full Name']+'-'+'AM.EN.U4CSE1900'+row['Roll no.'])
            else:
                temp.append(row['Full Name']+'-'+'AM.EN.U4CSE190'+row['Roll no.'])
            temp.append(0)
            temp.append(0)
            names.append(temp)
            del temp
            i+=1
    return(names)

def absentees_list_generator(names,attcsv,classDur,percent_att):
    with open("attendenceLists/"+ attcsv, 'r',encoding='utf16', errors='ignore') as file:
        csv_file = csv.DictReader(file)
        i=1
        att_list = []
        for row in csv_file:
            temp = (row['Full Name\tUser Action\tTimestamp']+row[None][0]).split('\t')
            date = temp.pop()
            format = '%m/%d/%Y %H:%M:%S %p'
            obj_date = datetime.datetime.strptime(date, format)
            temp.append(obj_date)
            att_list.append(temp)

    for row in att_list:
        if('-' not in row[0]):
            teacher_tstamp = row[2]
            print()
            print("Teacher Timestamp: ",teacher_tstamp)
            print()
        else:
            f=0
            for i in range(0,len(names)):
                if(names[i][0]==row[0]):
                    f=1
                    break
            if(f==1 and (names[i][1]==0 or names[i][1]==-1) and row[1]=="Joined"):
                names[i][1] = row[2]
            elif(f==1 and row[1]=="Left"):
                names[i][2] += (((row[2]-names[i][1]).seconds)//60)
                names[i][1] = -1
    class_end = teacher_tstamp+datetime.timedelta(hours = classDur)
    for name in names:
        if(name[1]!=-1 and name[1]!=0):
            name[2] += (((class_end - name[1]).seconds)//60)

    for name in names:
        if(name[2]<((percent_att*classDur)//100)):
            print(name[0],name[2])


if __name__ == "__main__":
    names = name_conversion("classList/names.csv")
    print("Enter file_name.csv")
    attcsv = input()
    print("Enter the duration of class in minutes")
    duration = int(input())
    print("Enter minimum attendence percentage criteria")
    per = int(input())
    absentees_list_generator(names,attcsv,duration,per)
