




def findHowsLines(k,file):
        s=1
        for line in file:
                if(k==s):
                        return [k+1,line]
                s+=1
        return [k]
     



having="E:\pythonFileHandlingProgramsLocation\BasicWTSP_onlyTwoWay";

file=open(having+"\having.txt","r");
k=1;
while(1):
        s=findHowsLines(k,file)
        if(s[0]!=k):
                print(s[1],end='')
                k==s[0];




