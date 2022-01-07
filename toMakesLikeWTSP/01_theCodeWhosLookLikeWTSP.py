
#this is having our full line as a string, and then cut the msg according to 30 and minuses.....
def sort(haved):
        lst=[];
        well=haved;
        tracker=0
        while(1):
                val=30;
                if(len(well)+1>val):
                        if(well[val]==" "):
                                lst.append(well[:val]);
                                for j in range(val,len(well)):
                                        if(well[j]!=" " and well[j-1]==" "):
                                                well=well[j:]; tracker+=j
                                                break;
                        else:
                                for i in range(val-1,-1,-1):
                                        if(well[i]==" "):
                                                lst.append(well[:i])
                                                for j in range(i,len(well)):
                                                        if(well[j]!=" " and well[j-1]==" "):
                                                                well=well[j:]; tracker+=j
                                                                break;
                                                break;
                else:
                        lst.append(well); tracker+=len(well)

                if(len(haved)==tracker):
                        return lst;
                

#there manage all the msg, who's sanding by me(as registered people).....
def sender(msg,l,what,why):
        permanentSpace="                                        ";
        specialSpace="|    ";
        anotherSpace="|>  "
        lst=sort(msg);
        if(what!=0 or why==1):
                print("\n",permanentSpace+"You:")
        for i in range(0,len(lst)):
                if(i==len(lst)-1 and len(lst)==1):
                        print(permanentSpace+anotherSpace+lst[i],end='')
                elif(len(lst)!=1 and i==len(lst)-1):
                        print(permanentSpace+specialSpace+lst[i],end='')
                elif(len(lst)!=1 and i==0):
                        print(permanentSpace+anotherSpace+lst[i])
                else:
                        print(permanentSpace+specialSpace+lst[i])


#there manage all the msg, recieving by me(as registered people).....
def reciever(msg,name,what,why):
        specialSpace="|    ";
        anotherSpace="|>  "
        lst=sort(msg);
        if(what!=0 or why==1):
                print("\n",name+":")
        for i in range(0,len(lst)):
                if(i==len(lst)-1 and len(lst)==1):
                        print(anotherSpace+lst[i],end='')
                elif(len(lst)!=1 and i==len(lst)-1):
                        print(specialSpace+lst[i],end='')
                elif(len(lst)!=1 and i==0):
                        print(anotherSpace+lst[i])
                else:
                        print(specialSpace+lst[i])


#here check DataBase where all the chat availabled.....
def find(your,another):
        file=open(having+"\having.txt","r");
        specialCount=yourValue=anotherValue=0
        for have1 in file:
                l=-1;
                for have2 in have1:
                        if(have2==':'):
                                break;
                        l+=1;
                if(have1[:l]==your):
                        sender(have1[l+3:],l,0 if(specialCount==yourValue) else 1,1 if(specialCount==0) else 0);
                        yourValue=specialCount=str(int(specialCount)+1);
                elif(have1[:l]==another):
                        reciever(have1[l+3:],another,0 if(specialCount==anotherValue) else 1,1 if(specialCount==0) else 0);
                        anotherValue=specialCount=str(int(specialCount)+1);
                else:
                        pass


#here check DataBase who's number you entered, is in a database or not.....
def findDatabase(having,mNo):
        file=open(having+"\DataBase.txt","r");
        lst=[]; k=0;
        for haved in file:
                if(int(haved[:10])==mNo):
                        lst.insert(0,haved[13:])
                        k=1
                else:
                        lst.append(haved[13:])
        for i in range(0,len(lst)):
                data=lst[i]
                length=len(lst[i]);
                if(lst[i][length-1]=='\n'):
                        lst[i]=lst[i][:length-1]
        if(k==1):
                return lst
        else:
                return 0


#its nothing, only for a designing. who's decorate in starting.....
def designing(design,times):
        for i in range(0,times):
                if(i==times-1):
                        print(design);
                        break;
                print(design,end='')





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


having="E:\pythonFileHandlingProgramsLocation\BasicWTSP_onlyTwoWay";
having="E:\\";

while(1):
        design="-----------------------------------------------" #47
        times=5
        print('\n\n\n\n')
        designing(design,times);
        print("for Now, it's works only for twoNumber's. as Shivam(7898565074) and as Shri(7898000000) only. so Enjoy it.....");
        mNo=int(input("Enter a Mobile No : "));
        designing(design,times);
        print('\n\n',end='')
        lst=findDatabase(having,mNo);
        if(lst==0):
                print("It's Invalied Number. try again.....")
        else:
                find(lst[0],lst[1]);



