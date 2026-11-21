study_menu={}
daily_records={}
while True:
    print("-----------------------------------")
    print("1.for subject:")
    print("2.for view records:")
    print("3.for exist:")
    print("4.total study hours:")
    print("5. all subject reviews:")
    print("6. for top subject:")
    print("7.to find particular subject:")
    print("8.average study hours:")
    print("9. update study hours:")
    print("10.to remove subject:")
    print("11.sort subject from higher to lower study hours:")
    print("12.weekly study progress:")
    print("13.save records:")
    print("14.to read lines:")
    print("15.daily records:")
    print("-----------------------------------")
    
    choice=input("enter choice:")
       
    if choice=="1":
        subject=input("enter subject name:")
        hours=float(input("enter no of hours:"))
        while hours<=0:
         print("enter a valid no!")
         hours=float(input("enter no of hours:"))
        study_menu[subject]=hours
        print("recorded the hours:")
        

    elif choice=="2":
       print("records:",study_menu)

    elif choice=="3":
        break 

    elif choice=="4":
      total=0
      for n in study_menu.values():
          total=total+n
      print("total study hours:",total)

    elif choice=="5":
       for subject,hours in study_menu.items():
        print(subject,":",hours,"hours")

    elif choice=="6":
       if study_menu:
          top_sub=max(study_menu,key=study_menu.get)
          print("top subject:",top_sub)
          print("study hours:",study_menu[top_sub])
       else:
          print("no records avialable:")

    elif choice=="7":
       search=input("enter a subject to find:")
       if search in study_menu:
          print("subject found:",search)
          print("study hours:",study_menu[search])
       else:
          print("search not found!")

    elif choice=="8":
        a=sum(study_menu.values())
        b=len(study_menu)
        c=a/b
        print("average hours:",c)

    elif choice=="9":
       subject=input("enter subject to update:")
       if subject in study_menu:
          hours=float(input("enter new study hours:"))
          while hours<=0:
                print("enter a valid no!")
                hours=float(input("enter no of hours:"))
          study_menu[subject]=hours
          print("recorded the hours:")
       else:
                print("subject not found:") 

    elif choice=="10":
       a=input("enter a subject to remove:")
       if a in study_menu:
          del study_menu[a]
          print("record deleted:")
       else:
          print("subject not in list!")   

    elif choice=="11":
       d=sorted(study_menu.items(),key=lambda x:x[1],reverse=True)
       print(d)

    elif choice=="12":
       print("=====study summary=====")
       f=sum(study_menu.values())
       print("total hours:",f)
       s=max(study_menu,key=study_menu.get)
       print("maximum studied subject:",s)
       print("hours:",study_menu[s])
       y=min(study_menu,key=study_menu.get)
       print("minimum studied subject:",y)
       print("hours:",study_menu[y])
       e=len(study_menu)
       g=f/e
       print("average studued hours:",g)

    elif choice=="13":
       file=open("study.txt","w")
       for subject,hours in study_menu.items():
         file.write(subject+":"+str(hours)+"hours\n")
       file.close()
       print("all records saved successfully")

    elif choice=="14":
       file=open("study.txt","r")
       data=file.readlines()
       file.close()
       for line in data:
          parts=line.strip().split(":")
          subject=parts[0]
          hours=parts[1].replace("hours","").strip()
          print(subject)
          print(hours)
          hours=float(hours)
          study_menu[subject]=hours
       print(study_menu)

    elif choice=="15":
       print("======DATE STUDY SUMMARY======")
       date=input("enter date (DD-MM-YYYY):")
       if date not in daily_records:
          daily_records[date]={}
       subject=input("enter the subjrect:")
       hours=float(input("enter the hours:"))
       daily_records[date][subject]=hours
       print(daily_records)
       print("\n")



    else:
     print("invalid choice:")

