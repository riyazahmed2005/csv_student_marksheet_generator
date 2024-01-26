def mark_sheet(f,x,length,collage,department,head):
    for i in x:
        c=i
        l=len(i)
        print()
        print("      *******"+collage+"*******     ")
        print("      *******"+department+"*******     ")
        print("________________________________________________")
        print(head[1]+":",c[1],end="                 ")
        print(head[0]+":",c[0])
        print()
        print("MARK OF THE STUDENT")
        print("______________________")
        print()
        s=0
        for j in range(2,l-1):
            print(head[j]+":",c[j],end="  ")
            if(int(c[j])>45):
                print("-->PASS",end="    ")
            else:
                print("-->FAIL",end="   ")
            if (int(c[j])>=90 and int(c[j])<=100):
                print("-->A+")
            elif(int(c[j])>=80 and int(c[j])<=89):
                  print("-->A")
            elif (int(c[j])>=70 and int(c[j])<=79):
                print("-->B+")
            elif (int(c[j])>=60 and int(c[j])<=69):
                print("-->B")
            elif (int(c[j])>=50 and int(c[j])<=59):
                print("-->C+")
            elif (int(c[j])>=46 and int(c[j])<=49):
                print("-->C")
            else:
                print("no grade")
        for j in range(2,l-1):
            s+=int(c[j])
        print()
        print("TOTAL :",s,"/400")
        c=0
        for k in range(2,length-1):
            c+=1
        avg=s//c
        print("AVERAGE: ",avg)
#main
import csv
f=open("student.csv","r")
x=csv.reader(f)
head=next(x)
length=len(head)
collage=input("enter your collage name in upper case")
department=input("enter your department name in upper case")
mark_sheet(f, x, length, collage, department, head)