def show():
    File=open("file.File","r",newline='')
    List1=[]
    for x in File:
        List1.append(x.strip('\n'))
    File.close()
    List1.pop(0)
    return(List1)

a=show()
print(a)




