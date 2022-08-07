import tkinter as tk
import os
from tkinter import messagebox
import sqlite3 as sql
root=tk.Tk()
l=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.wm_attributes('-fullscreen', 1)
root.title("Voting Program V.1")
img=tk.PhotoImage(file="image2.png")
img2=tk.PhotoImage(file="f.png")
img3=tk.PhotoImage(file="f2.png")
root.iconbitmap('icon2.ico')
background1=tk.Label(root,image=img).place(x=0,y=0,relwidth=1,relheight=1)
def show():
    File=open("file.File","r",newline='')
    List1=[]
    for x in File:
        List1.append(x.strip('\n'))
    File.close()
    List1.pop(0)
    return(List1)
def close():
    root.destroy()
def post():
    connect=sql.connect("data.db")
    querry=connect.cursor()
    q="SELECT name FROM sqlite_master WHERE type='table';"
    querry.execute(q)
    data=querry.fetchall()
    List=[]
    for x in data:
        List.append(x[0])
    return List
    connect.close()

def next():
    def vote_other():
        global ask
        ask=tk.Frame(root,width=800,height=l)
        background1=tk.Label(ask,image=img3).place(x=0,y=0,relwidth=1,relheight=1)
        k=0
        candidate=[]
        for c in g:
            candidate.append(c.get())
        y=10
        for x in List:
            lab=tk.Label(ask,text="You Have selected {} for the Post of {}".format(candidate[k],x),font=("Arial Black",13),bg="grey",fg="white")
            lab.place(x=10,y="{}".format(y))
            k=k+1
            y=y+40
        info=tk.Label(ask,text="You have selected {} for the post of House Captain".format(Captain.get()),font=("Arial Black",13),bg="grey",fg="white")
        info.place(x=10,y=y+40)
        info2=tk.Label(ask,text="You have selected {} for the post of House Vice Captain".format(Vice_Captain.get()),font=("Arial Black",13),bg="grey",fg="white")
        info2.place(x=10,y=y+80)
        btn3=tk.Button(ask,text="Vote",width=50,height=6,font=5,command=vote)
        btn3.place(x=150,y=500)
        btn4=tk.Button(ask,text="Back",width=50,height=6,font=5,command=lambda:destroy(ask))
        btn4.place(x=150,y=650)
        p2=(int('{}'.format(w))/2)-400
        ask.place(x='{}'.format(p2),y=0)

        
    global g
    global fr
    candidate=[]
    connect=sql.connect("data.db")
    querry=connect.cursor()
    fr=tk.Frame(root,width=500,height=l)
    background3=tk.Label(fr,image=img2).place(x=0,y=0,relwidth=1,relheight=1)
    other=tk.Frame(fr,bg="Black")
    List=post()
    g=[]
    for x in List:
        q="select candidate_name from {}".format(x)
        querry.execute(q)
        data=querry.fetchall()
        a="List_"+"{}".format(x)
        a=[]
        for y in data:
            a.append(y[0])   
        label4=tk.Label(other,text="Select "+"{}".format(x),width=23,height=1,font=20,bg="Pink")
        label4.pack(fill=tk.X)   
        option_c=a
        b="{}".format(x)
        b=tk.StringVar(other)
        b.set(option_c[0])
        d="sel_"+"{}".format(x)
        d=tk.OptionMenu(other,b,*option_c)
        d.config(width=20,height=2)
        d.pack(fill=tk.X)
        g.append(b)
        label5=tk.Label(other,image=img2,width=23,height=20)
        label5.pack(fill=tk.X)
    
    close_btn=tk.Button(other,text="Cancel",width=20,font=10,command=lambda:destroy(fr))
    close_btn.pack(side=tk.BOTTOM,fill=tk.X)
    label7=tk.Label(other,image=img2,width=23,height=20)
    label7.pack(side=tk.BOTTOM,fill=tk.X)
    vote_btn2=tk.Button(other,text="Next",width=20,height=3,font=10,command=vote_other)
    vote_btn2.pack(side=tk.BOTTOM,fill=tk.X)
    other.place(x=140,y=10)
    
    p1=(int('{}'.format(w))/2)-250
    fr.place(x='{}'.format(p1),y=0)









connect1=sql.connect("vote.db")
querry1=connect1.cursor()
connect2=sql.connect("candidate.db")
querry2=connect2.cursor()
connect3=sql.connect("code.db")
querry3=connect3.cursor()
house_list=['yellow','red','blue','green']
length1=len(house_list)
y1=0
for x in ["voted_for_red","voted_for_blue","voted_for_green","voted_for_yellow"]:
    z="DELETE FROM {}".format(x)
    querry3.execute(z)
    connect3.commit()
    
for x in range(0,length1):
    name="candidates_for_{}".format(house_list[y1])
    z="SELECT House_Captain FROM {} WHERE House_Captain NOT LIKE 'None'".format(name)
    querry2.execute(z)
    List_captain=querry2.fetchall()
    List_captain_Final=[]
    for x in List_captain:
        for y in x:
            List_captain_Final.append(y)
    #(List_captain_Final)
    z="SELECT House_Vice_Captain FROM {} WHERE House_Vice_Captain NOT LIKE 'None'".format(name)
    querry2.execute(z)
    List_Vice_captain=querry2.fetchall()
    List_Vice_captain_Final=[]
    for x in List_Vice_captain:
        for y in x:
            List_Vice_captain_Final.append(y)
    #(List_Vice_captain_Final)

    z="DROP TABLE IF EXISTS vote_for_captain_{}".format(house_list[y1])
    querry1.execute(z)
    connect1.commit()
    z="DROP TABLE IF EXISTS vote_for_vice_captain_{}".format(house_list[y1])
    querry1.execute(z)
    connect1.commit()
    z="create table vote_for_captain_{} (none text DEFAULT 0)".format(house_list[y1])
    querry1.execute(z)
    connect1.commit()
    z="create table vote_for_vice_captain_{} (none text DEFAULT 0)".format(house_list[y1])
    querry1.execute(z)
    connect1.commit()
    length=len(List_Vice_captain_Final)
    n=0
    for x in range(0,length):
        z="ALTER TABLE vote_for_vice_captain_{} ADD {} text DEFAULT 0".format(house_list[y1],List_Vice_captain_Final[n])
        querry1.execute(z)
        connect1.commit()
        z="INSERT INTO vote_for_vice_captain_{}({}) VAlUES (0)".format(house_list[y1],List_Vice_captain_Final[n])
        querry1.execute(z)
        connect1.commit()
        n=n+1

    length=len(List_captain_Final)
    #(length)
    n=0
    for x in range(0,length):
        z="ALTER TABLE vote_for_captain_{} ADD {} text DEFAULT 0".format(house_list[y1],List_captain_Final[n])
        querry1.execute(z)
        connect1.commit()
        z="INSERT INTO vote_for_captain_{}({}) VAlUES (0)".format(house_list[y1],List_captain_Final[n])
        querry1.execute(z)
        connect1.commit()
        n=n+1
    y1=y1+1
connect=sql.connect("data.db")
querry=connect.cursor()
List=post()
for x in List:
    z="UPDATE {} SET Votes = 0".format(x)
    querry.execute(z)
    connect.commit()
connect.close()


def alt_f4(event):
    global pressed_f4
    #('Alt-F4 pressed')
    pressed_f4 = True

global vote_btn

def destroy(frame):
    frame.destroy()
def vote():
    connect=sql.connect("vote.db")
    querry=connect.cursor()
    house_captain=Captain.get()
    house_vice_captain=Vice_Captain.get()
    z="UPDATE vote_for_vice_captain_{} SET {} = {}+1 ".format(tkvarq.get(),house_vice_captain,house_vice_captain)
    querry.execute(z)
    connect.commit()
    z="UPDATE vote_for_captain_{} SET {} = {}+1 ".format(tkvarq.get(),house_captain,house_captain)
    querry.execute(z)
    connect.commit()
    connect=sql.connect("data.db")
    querry=connect.cursor()
    candidate=[]
    List=post()
    for c in g:
        candidate.append(c.get())
    n=0  
    for x in List:
        y=candidate[n]
        z="UPDATE {} SET Votes = Votes+1 WHERE candidate_name='{}'".format(x,y)
        querry.execute(z)
        connect.commit()
        n=n+1
    connect.close()
    
    t="You have SUCCESSFULLY VOTED!"
    warning(t)
    code.delete(0, 'end')
    vote_btn.destroy()
    sel_Captain.destroy()
    sel_Vice_Captain.destroy()
    lc.destroy()
    lvc.destroy()
    vote_btn.destroy()
    destroy(fr)
    destroy(ask)





def toglle2():
    global Captain
    global Vice_Captain
    global sel_Captain
    global sel_Vice_Captain
    global lc
    global lvc
    global vote_btn
    connect=sql.connect("candidate.db")
    querry=connect.cursor()
    name="candidates_for_{}".format(tkvarq.get())
    z="SELECT House_Captain FROM {} WHERE House_Captain NOT LIKE 'None'".format(name)
    querry.execute(z)
    List_captain=querry.fetchall()
    List_captain_Final=[]
    for x in List_captain:
        for y in x:
            List_captain_Final.append(y)
            #(List_captain_Final)
    z="SELECT House_Vice_Captain FROM {} WHERE House_Vice_Captain NOT LIKE 'None'".format(name)
    querry.execute(z)
    List_Vice_captain=querry.fetchall()
    List_Vice_captain_Final=[]
    for x in List_Vice_captain:
        for y in x:
            List_Vice_captain_Final.append(y)
            #(List_Vice_captain_Final)

    
    p3=(int('{}'.format(w))/2)-250
    p4=(int('{}'.format(w))/2)+150
    if len(List_captain_Final)==0:
        t="No House Captain Found"
        warning(t)
        
        lc=tk.Label(root,text="No House Captain Found",width=23,height=1,bg="Pink")
        lc.place(x='{}'.format(p3),y=380)
    else:
        lc=tk.Label(root,text="Select House Captain",width=23,height=1,bg="Pink")
        lc.place(x='{}'.format(p3),y=380)
        option_list_c=List_captain_Final
        Captain=tk.StringVar(root)
        Captain.set(option_list_c[0])
        sel_Captain=tk.OptionMenu(root,Captain,*option_list_c)
        sel_Captain.config(width=20,height=2)
        sel_Captain.place(x='{}'.format(p3),y=410)


    if len(List_Vice_captain_Final)==0:
        t="No Vice Captain Found"
        warning(t)
        
        lvc=tk.Label(root,text="No Vice Captain Found",width=23,height=1,bg="Pink")
        lvc.place(x='{}'.format(p4),y=380)
    else:
        lvc=tk.Label(root,text="Select House House Captain",width=23,height=1,bg="Pink")
        lvc.place(x='{}'.format(p4),y=380)
        option_list_vc=List_Vice_captain_Final
        Vice_Captain=tk.StringVar(root)
        Vice_Captain.set(option_list_vc[0])
        sel_Vice_Captain=tk.OptionMenu(root,Vice_Captain,*option_list_vc)
        sel_Vice_Captain.config(width=20,height=2)
        
        sel_Vice_Captain.place(x='{}'.format(p4),y=410)
    p10=(int('{}'.format(w))/2)-20
    if len(List_captain_Final)!=0 and len(List_Vice_captain_Final)!=0:
        vote_btn=tk.Button(root,text="NEXT",width=10,height=2,font=10,command=next)
        vote_btn.place(x='{}'.format(p10),y=500)
    else:
        pass
    connect.commit()


def otvc_check():
    connect=sql.connect('code.db')
    querry=connect.cursor()
    name1="code_for_{}".format(tkvarq.get())
    name2="voted_for_{}".format(tkvarq.get())
    z="SELECT * FROM {}".format(name1)
    querry.execute(z)
    List=querry.fetchall()
    List_Final=[]
    #(List_Final)
    for x in List:
        for y in x:
            List_Final.append(y)
    z="SELECT * FROM {}".format(name2)
    querry.execute(z)
    List=querry.fetchall()
    List_voted_Final=[]
    for x in List:
        for y in x:
            List_voted_Final.append(y)
    if code.get()=="" or code.get()==" ":
        t="please enter your code"
        warning(t)
        code.delete(0, 'end')
    elif code.get() not in List_Final:
        t="Please Input Correct Code For Your House"
        warning(t)
        code.delete(0, 'end')
    elif code.get() in List_voted_Final:
        t="Sorry! You have allready Voted"
        warning(t)
        code.delete(0, 'end')
    else :
        toglle2()
        z="INSERT INTO {} VALUES ('{}')".format(name2,code.get())
        querry.execute(z)

    connect.commit()





    






def warning(t):
    messagebox.showwarning("Warning","{}".format(t))
   

def message(t):
    a=messagebox.askokcancel('Quit','{}'.format(t))
    return a
def toggle(event):
    t="do you want to quit"
    o=message(t)
    if o==True:
        t="Are you sure to quit"
        p=message(t)
        if p==True:
            t="Finally You Want To Quit"
            q=message(t)
            if q==True:
                close()
            else:
                pass
        else:
            pass
    else:
        pass

def update(event):
    color=tkvarq.get()
    if color in ["red","green","blue"]:
        l2.config(text="You are voting for {} house".format(tkvarq.get()),
                                                bg="{}".format(tkvarq.get()),
                                                        fg="white")
    else:
        l2.config(text="You are voting for {} house".format(tkvarq.get()),
                                                bg="{}".format(tkvarq.get()),
                                                        fg="black")
    code.delete(0, 'end')
    lc.destroy()
    lvc.destroy()
    vote_btn.destroy()
    sel_Captain.destroy()
    sel_Vice_Captain.destroy()
    vote_btn.destroy()


heading=tk.Label(root,text="Vote 1.0",width='{}'.format(w),height=2,font=("Arial Black",13),bg="Pink")
heading.place(x=0,y=0,relwidth=1)

l1=tk.Label(root,text="Please Select your house",font=50)
p1=(int('{}'.format(w))/2)-60
l1.place(x='{}'.format(p1),y=125)

l2=tk.Label(root,text="You are voting for yellow house",font=50,bg="yellow")
p2=(int('{}'.format(w))/2)-80
l2.place(x='{}'.format(p2),y=230)

l3=tk.Label(root,text="Please keep (Caps Lock ON) while entering code",font=("Arial Black",15),fg="white",bg="red")

l3.place(x=50,y=80)

p5=(int('{}'.format(w))/2)-500
l3=tk.Label(root,text="Enter your OTVC Code",width=50,height=2,bg="Pink",font=20)
l3.place(x='{}'.format(p5),y=300)

p6=(int('{}'.format(w))/2)+80
code=tk.Entry(root,width=12,font=25)
code.place(x="{}".format(p6),y=300)
p7=(int('{}'.format(w))/2)+230
btn1=tk.Button(root,text="Next",width=20,height=1,command=otvc_check)
btn1.place(x='{}'.format(p7),y=300)




option_list=["yellow","green","red","blue"]
tkvarq=tk.StringVar(root)
tkvarq.set(option_list[0])
sel_house=tk.OptionMenu(root,tkvarq,*option_list,command=update)
sel_house.config(width=20,height=2)
sel_house.place(x='{}'.format(p1),y=170)

credit2=tk.Label(root,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(w))
credit2.pack(side=tk.BOTTOM)

info=tk.Label(root,text='''Key points to be noted:-
1.Please keep Caps Lock ON while entering code
2.DO NOT CLOSE THE PROGRAM UNTILL VOTING IS DONE
3.IF YOU WILL CLOSE THE PROGRAM ENTIRE DATA WILL BE LOST''',height=5,width='{}'.format(w),font=("Arial Black",12),bg="red",fg="white")
info.pack(side=tk.BOTTOM)

pressed_f4 = False  # Is Alt-F4 pressed?
def do_not_exit():
    global pressed_f4
    #('Trying to close application')
    if pressed_f4:  # Deny if Alt-F4 is pressed
        #('Denied!')
        pressed_f4 = False  # Reset variable  


root.bind('<Escape>',toggle)
root.bind('<Alt-F4>', alt_f4)
root.protocol("WM_DELETE_WINDOW",do_not_exit)
root.mainloop()
