import string 
import csv
import random
import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox
from tkinter import ttk
import os
File100=open("user.docx",'w')
File100.close()

class Window: 
        def __init__(self):

                class Login:
                        def ask(t):
                                a=messagebox.askyesno('Quit','{}'.format(t))
                                return a
                        def warning(t):
                                messagebox.showwarning("Warning","{}".format(t))
                        
                        def back():
                                file1=open("user.docx",'r')
                                a=file1.readline()
                                if a in ['admin yellow','admin red','admin blue','admin green']:
                                        f7.place(x=0,y=0,relwidth=1,relheight=1)
                                        f7.tkraise()
                                else:
                                        f2.place(x=0,y=0,relwidth=1,relheight=1)
                                        f2.tkraise()
                                self.table.delete(*self.table.get_children())
                                self.name.delete(0,'end')

                        def swap(frame):
                                frame.place(x=0,y=0,relwidth=1,relheight=1)
                                frame.tkraise()
                        def logout():
                                file1=open("user.docx",'w')
                                file1.close()
                                self.f1.place(x=0,y=0,relwidth=1,relheight=1)
                                self.f1.tkraise()
                                code_generator.clear()
                                self.table.delete(*self.table.get_children())

                        def Check_user(entry_username,entry_password,f2):
                                connect=sql.connect("User.db")
                                querry=connect.cursor()
                                user_name=entry_username.get()
                                user_pass=entry_password.get()
                                querry.execute("select * from user")
                                a=querry.fetchall()
                                length=len(a)
                                users={}
                                n=0
                                for x in range(0,length):
                                        b=a[n]
                                        u=b[0]
                                        p=b[1]
                                        users[u]=p
                                        n=n+1
                                user=list(users.keys())
                                #(users)
                
                                if user_name in[" ",""] or user_pass in[" ",""]:
                                        t="All Feilds Required"
                                        Login.warning(t)
                                        self.entry_password.delete(0,'end')
                                        self.entry_username.delete(0,'end')
                                elif user_name not in user:
                                        t="invalid username"
                                        Login.warning(t)
                                        self.entry_username.delete(0,'end')
                                elif user_pass!=users[user_name]:
                                        t="Worng Password"
                                        Login.warning(t)
                                        self.entry_password.delete(0,'end')
                                else:
                                        if user_name in ['admin yellow','admin red','admin blue','admin green']:
                                                File=open("user.docx",'w')
                                                File.write(user_name)
                                                File.close()
                                                Login.swap(f7)
                                                self.entry_password.delete(0,'end')
                                                self.entry_username.delete(0,'end')
                                        else:
                                                Login.swap(f2)
                                                self.entry_password.delete(0,'end')
                                                self.entry_username.delete(0,'end')
                                                

                class code_generator:
                        def user_check():
                                File=open("user.docx","r")
                                b=[]
                                a=File.readlines()
                                for x in a:
                                        b=x.split()
                                if len(b)!=0:
                                        if tkvarq.get()!=b[1]:
                                                t="Access Denied!"
                                                Login.warning(t)
                                                number.delete(0,'end')
                                        else:
                                                code_generator.random_code_generator()
                                else:
                                        code_generator.random_code_generator()

                                
                        
                        def openfile():
                                p=os.getcwd()
                                a="{}\codes".format(p)
                                os.system('''Explorer {}'''.format(a))
                        def warning(t):
                                messagebox.showwarning("Warning","{}".format(t))
                        
                        def clear():
                                self.log_frame.destroy()
                                self.clearbtn.destroy()
                        def log():
                                n=int(number.get())
                                data=tk.Label(master=self.log_frame,
                                text="You have generated {} OTVC for {} House".format(n,d))
                                data.pack()
                                number.delete(0,'end')
                        
                        def action1(event):
                                global l2
                                global generate
                                global number
                                File=open("user.docx","r")
                                b=[]
                                a=File.readlines()
                                for x in a:
                                        b=x.split()
                                if len(b)!=0:
                                        if b[1]==tkvarq.get():
                                                l2=tk.Label(master=f3,text="Enter the Number of OTVC (One Time Voting Code) you want to Generate",
                                                        width=70,
                                                        height=2,
                                                        font=("Segoe UI Black",11),
                                                        fg="brown",
                                                        relief=tk.GROOVE)
                                                l2.place(x=150,y=250)

                                                number=tk.Entry(master=f3,width=18,font=50)
                                                number.place(x=800,y=250)

                                                generate=tk.Button(master=f3,text="Generate",width=15,command=code_generator.user_check)
                                                generate.place(x=450,y=350)
                                        else:
                                                t="Access Denied!"
                                                Login.warning(t)
                                else:
                                        l2=tk.Label(master=f3,text="Enter the Number of OTVC (One Time Voting Code) you want to Generate",
                                                        width=70,
                                                        height=2,
                                                        font=("Segoe UI Black",11),
                                                        fg="brown",
                                                        relief=tk.GROOVE)
                                        l2.place(x=150,y=250)

                                        number=tk.Entry(master=f3,width=18,font=50)
                                        number.place(x=800,y=250)

                                        generate=tk.Button(master=f3,text="Generate",width=15,command=code_generator.user_check)
                                        generate.place(x=450,y=350)

                        
                        
                        def new():
                                global l2
                                global generate
                                global number
                                l2.destroy()
                                number.destroy()
                                generate.destroy()
                        
                                l2=tk.Label(master=f3,text="Enter the Number of OTVC (One Time Voting Code) you want to Generate",
                                width=70,
                                height=2,
                                font=("Segoe UI Black",11),
                                fg="brown",
                                relief=tk.GROOVE)
                                l2.place(x=150,y=250)

                                number=tk.Entry(master=f3,width=18,font=50)
                                number.place(x=800,y=250)

                                generate=tk.Button(master=f3,text="Generate",width=15,command=code_generator.user_check)
                                generate.place(x=450,y=350)
                        
                        
                        def random_code_generator():
                                t='''Codes had been already generated
Do you want to overwrite?'''
                                z=Login.ask(t)
                                if z==True:
                                        p=os.getcwd()
                                        connect=sql.connect("code.db")
                                        querry=connect.cursor()
                                        global d
                                        d=tkvarq.get()
                                        f="{}\codes\code_for_".format(p)+d+".txt"
                                        g="code_for_"+d
                                        file=open(r'{}'.format(f),"w")
                                        n=int(number.get())
                                                #(n)
                                        
                                        if n>500:
                                                number.delete(0,'end')
                                                t="Please enter in range 0-500"
                                                Login.warning(t)
                                                        #n=int(number.get())
                                        else:
                                        
                                                querry.execute("DELETE from {}".format(g))
                                                connect.commit()
                                                j=0
                                                while n>0:
                                                        N=6
                                                        res= ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
                                                                #(res)
                                                        querry.execute("INSERT INTO {} values ('{}')".format(g,res))
                                                        if j<4:
                                                                if j==3:
                                                                        file.write(res)
                                                                else:
                                                                        file.write(res)
                                                                        file.write("         ")
                                                                j=j+1
                                                        else:
                                                                file.write("\n")
                                                                file.write("\n")
                                                                file.write("\n")
                                                                file.write("\n")
                                                                file.write(res)
                                                                file.write("         ")
                                                                j=1

                                                        
                                                        n=n-1
                                                        connect.commit()
                                                        
                                                        #(f,"file is in folder random code generator")
                                                file.close()
                                                        
                                                
                                                        
                                                p=self.log_frame.winfo_exists()
                                                q=self.clearbtn.winfo_exists()
                                                if p==1:
                                                        self.log_frame.place(x=150,y=500)
                                                else:
                                                        self.log_frame=tk.Frame(f3,width=400,
                                                        height=200)
                                                        self.log_frame.place(x=150,y=500)
                                                        self.label=tk.Label(self.log_frame,text="LOG")
                                                        self.label.pack()
                                                if q==1:
                                                        self.clearbtn.place(x=850,y=500)
                                                        
                                                else:
                                                        self.clearbtn=tk.Button(f3,text="Clear LOG",width=15,command=code_generator.clear)
                                                        self.clearbtn.place(x=850,y=500)
                                                code_generator.log()

                                else:
                                        pass
                                        

                class candidate:
                        
                                        

                        def update(event):
                                color=tkvarq2.get()
                                File=open("user.docx","r")
                                b=[]
                                a=File.readlines()
                                for x in a:
                                        b=x.split()
                                #(b)
                                
                                if len(b)!=0:
                                        if color!=b[1]:
                                                
                                                if color in ["red","green","blue"]:
                                                        self.heading_add.config(text="You are Entering Details for {} House".format(tkvarq.get()),
                                                                bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                        self.label1_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                        self.label2_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                else:
                                                        self.heading_add.config(text="You are Entering Details for {} House".format(tkvarq2.get()),
                                                                bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                        self.label1_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                        self.label2_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                t="Access Denied!"
                                                Login.warning(t)
                                        
                                        else:
                                                if color in ["red","green","blue"]:
                                                        self.heading_add.config(text="You are Entering Details for {} House".format(tkvarq.get()),
                                                                bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                        self.label1_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                        self.label2_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                else:
                                                        self.heading_add.config(text="You are Entering Details for {} House".format(tkvarq2.get()),
                                                                bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                        self.label1_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                        self.label2_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                candidate.show_data()
                                else:
                                        if color in ["red","green","blue"]:
                                                self.heading_add.config(text="You are Entering Details for {} House".format(tkvarq.get()),
                                                                bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                self.label1_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                                self.label2_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="white")
                                        else:
                                                self.heading_add.config(text="You are Entering Details for {} House".format(tkvarq2.get()),
                                                                bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                self.label1_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                                self.label2_add.config(bg="{}".format(tkvarq2.get()),
                                                                        fg="black")
                                        candidate.show_data()
                                        
                                        
                        

                        def check_avail():
                                connect=sql.connect("candidate.db")
                                querry=connect.cursor()
                                name_maker="candidates_for_{}".format(tkvarq2.get())
                                post_checker=var.get()
                                name_get=self.name.get()
                                passquerry=("SELECT {} FROM {} WHERE {} NOT IN('NULL')".format(post_checker,name_maker,post_checker))
                                querry.execute(passquerry)
                                list1=querry.fetchall()
                                list_of_candidates=[]
                                for x in list1:
                                        for y in x:
                                                list_of_candidates.append(y)
                                if name_get in list_of_candidates:
                                        return True
                                connect.commit()
                                
                        def add():
                                color=tkvarq2.get()
                                File=open("user.docx","r")
                                b=[]
                                a=File.readlines()
                                for x in a:
                                        b=x.split()
                                if len(b)!=0:
                                        if b[1]!=tkvarq2.get():
                                                t="Access Denied!"
                                                Login.warning(t)
                                        else:
                                                connect=sql.connect("candidate.db")
                                                querry=connect.cursor()
                                                r=candidate.check_avail()
                                                name_get=self.name.get()
                                                if name_get in [""," "]:
                                                        t="Please enter Candidate Name"
                                                        Login.warning(t)
                                                elif r==True:
                                                        t="Candidate Already There!"
                                                        Login.warning(t)
                                                else:
                                                        name_maker="candidates_for_{}".format(tkvarq2.get())
                                                        post_checker=var.get()
                                                        name_get=self.name.get()
                                                        passquerry=("INSERT INTO {}({}) VALUES('{}')".format(name_maker,post_checker,name_get))
                                                        querry.execute(passquerry)
                                                        connect.commit()
                                                candidate.show_data()
                                else:
                                        connect=sql.connect("candidate.db")
                                        querry=connect.cursor()
                                        r=candidate.check_avail()
                                        name_get=self.name.get()
                                        if name_get in [""," "]:
                                                t="Please enter Candidate Name"
                                                Login.warning(t)
                                        elif r==True:
                                                t="Candidate Already There!"
                                                Login.warning(t)
                                        else:
                                                name_maker="candidates_for_{}".format(tkvarq2.get())
                                                post_checker=var.get()
                                                name_get=self.name.get()
                                                passquerry=("INSERT INTO {}({}) VALUES('{}')".format(name_maker,post_checker,name_get))
                                                querry.execute(passquerry)
                                                connect.commit()
                                        candidate.show_data()
                                


                        def show_data():
                                connect=sql.connect("candidate.db")
                                querry=connect.cursor()
                                table_name="candidates_for_"+tkvarq2.get()
                                querry.execute("select * from {} ".format(table_name))
                                rows=querry.fetchall()
                                if len(rows)!=0:
                                        n=0
                                        m=len(rows)
                                        self.table.delete(*self.table.get_children())
                                        for row in rows:
                                                self.table.insert('',n, values=row)
                                                n=n+1
                                        connect.commit()
                                else:
                                        List=['No Captain Foud','No Vice Captain Found']
                                        self.table.delete(*self.table.get_children())
                                        self.table.insert('',0, values=List)

                                connect.close()
                                self.name.delete(0,'end')
                        
                

                        def delete_data():
                                delete=self.table.focus()
                                content=self.table.item(delete)
                                row=content['values']
                                
                                connect=sql.connect("candidate.db")
                                querry=connect.cursor()
                                table_name="candidates_for_"+tkvarq2.get()
                                if len(row)==0:
                                        t="Please Select the Candidate"
                                        Login.warning(t)
                                elif row[0]=='None':
                                        querry.execute("DELETE FROM {} WHERE House_Vice_Captain LIKE ('{}')".format(table_name,row[1]))
                                else:
                                        querry.execute("DELETE FROM {} WHERE House_Captain LIKE ('{}')".format(table_name,row[0]))
                                        
                                connect.commit()
                                candidate.show_data()        



                def launch():
                        File=open("attempt.docx",'r')
                        at=File.readlines()
                        #(at)
                        if len(at)==0:
                                p=os.getcwd()
                                a="{}".format(p)
                                #os.system('''cmd cd /d {}'''.format(a))
                                #os.system('cmd /c "python voting.py"')
                                os.system('cmd /c "voting.exe"')
                                File2=open('attempt.docx','w')
                                File2.write('1')
                                File2.close()
                                
                        elif int(at[0])==1:
                                t="Sorry you have Did Voting for this Year"
                                Login.warning(t)
                        else:
                                pass
                        File.close()
                        
                def show_result():
                        global result_frame_captain
                        global result_frame_vice_captain
                        result_frame_captain.destroy()
                        result_frame_vice_captain.destroy()
                        name2="voted_for_{}".format(tkvarq3.get())
                        
                        global heading1
                        global heading2
                        result_frame_captain=tk.Frame(f5,width=400,height=400)
                        result_frame_captain.place(x=100,y=200)
                        result_frame_vice_captain=tk.Frame(f5,width=400,height=400)
                        result_frame_vice_captain.place(x=600,y=200)
                        
                        heading1=tk.Label(result_frame_captain,text="Results for House Captain",font=('Arial Black',15),bg="{}".format(tkvarq3.get()))
                        heading1.place(x=0,y=0,relwidth=1)
                        heading2=tk.Label(result_frame_vice_captain,text="Results for House Vice Captain",font=('Arial Black',15),bg="{}".format(tkvarq3.get()))
                        heading2.place(x=0,y=0,relwidth=1)
                        color=tkvarq3.get()
                        if color in ["red","green","blue"]:
                                heading1.config(bg="{}".format(tkvarq3.get()),fg="white")
                                heading2.config(bg="{}".format(tkvarq3.get()),fg="white")
                        else:
                                heading1.config(bg="{}".format(tkvarq3.get()),fg="black")
                                heading2.config(bg="{}".format(tkvarq3.get()),fg="black")
                        connect=sql.connect("vote.db")
                        querry=connect.cursor()
                        connect2=sql.connect("candidate.db")
                        querry2=connect2.cursor()
                        connect3=sql.connect('code.db')
                        querry3=connect3.cursor()
                        
                        List_of_captain=[]
                        z="SELECT House_Captain FROM candidates_for_{} WHERE House_Captain NOT LIKE 'None'".format(tkvarq3.get())
                        querry2.execute(z)
                        connect2.commit()
                        l=querry2.fetchall()
                        
                        for x in l:
                                for y in x:
                                        List_of_captain.append(y)
                        #(List_of_captain)

                        d={}

                        for x in List_of_captain:
                                z="select {} from vote_for_captain_{}".format(x,tkvarq3.get())
                                querry.execute(z)
                                connect.commit()
                                v=querry.fetchall()
                                vf=[]
                                for y in v:
                                        for z in y:
                                                vf.append(z)
                                                d['{}'.format(x)]='{}'.format(z)
                                

                                        #("{} has got {} votes".format(x,vf[0]))


                        sorted_dict = {}
                        sorted_keys = sorted(d, key=d.get,reverse=True)  # [1, 3, 2]
                        for w in sorted_keys:
                                sorted_dict[w] = d[w]
                        key=sorted_dict.keys()
                        n=40
                        z="SELECT * FROM {}".format(name2)
                        querry3.execute(z)
                        List=querry3.fetchall()
                        List_voted_Final=[]
                        for x in List:
                                for y in x:
                                        List_voted_Final.append(y)
                        total=len(List_voted_Final)
                        
                        
                        label1=tk.Label(result_frame_captain,text="Total Votes Count {}".format(total),font=('Arial Black',12))
                        label1.place(x=0,y=350)
                        label2=tk.Label(result_frame_vice_captain,text="Total Votes Count {}".format(total),font=('Arial Black',12))
                        label2.place(x=0,y=350)

                        for x in key:
                                label=tk.Label(result_frame_captain,text="{} has got {} Votes".format(x,sorted_dict[x]),font=('Arial Black',12))
                                label.place(x=0,y='{}'.format(n))
                                n=n+30
                        
                        #(d)
                        #(sorted_dict)
                        


                        List_of_Vice_captain=[]
                        z="SELECT House_Vice_Captain FROM candidates_for_{} WHERE House_Vice_Captain NOT LIKE 'None'".format(tkvarq3.get())
                        querry2.execute(z)
                        connect2.commit()
                        l=querry2.fetchall()
                        for x in l:
                                for y in x:
                                        List_of_Vice_captain.append(y)
                        #(List_of_Vice_captain)

                        d2={}

                        for x in List_of_Vice_captain:
                                z="select {} from vote_for_vice_captain_{}".format(x,tkvarq3.get())
                                querry.execute(z)
                                connect.commit()
                                v=querry.fetchall()
                                vf=[]
                                for y in v:
                                        for z in y:
                                                vf.append(z)
                                                d2['{}'.format(x)]='{}'.format(z)
                                

                                #("{} has got {} votes".format(x,vf[0]))


                        sorted_dict2 = {}
                        sorted_keys2 = sorted(d2, key=d2.get,reverse=True)  # [1, 3, 2]
                        for w in sorted_keys2:
                                sorted_dict2[w] = d2[w]

                        key=sorted_dict2.keys()
                        n=40
                        for x in key:
                                label=tk.Label(result_frame_vice_captain,text="{} has got {} Votes".format(x,sorted_dict2[x]),font=('Arial Black',12))
                                label.place(x=0,y='{}'.format(n))
                                n=n+30
                        #(d2)
                        #(sorted_dict2)


                def update2(event):
                        show_result()


                def reset():
                        t="This will reset all voting data for this year"
                        a=Login.ask(t)
                        if a==True:
                                t="Do you want to delete All Voting DATA"
                                a=Login.ask(t)
                                if a==True:
                                        file=open("attempt.docx","w")
                                        file.write("")
                                        file.close()
                                else:
                                        pass
                        else:
                                pass


                def changepassword():
                        def change():
                                file1=open("user.docx",'r')
                                c=file1.readline()
                                b=['admin yellow','admin red','admin blue','admin green']
                                connect=sql.connect("User.db")
                                querry=connect.cursor()
                                querry.execute("select * from user")
                                a=querry.fetchall()
                                length=len(a)
                                users={}
                                n=0
                                for x in range(0,length):
                                        b=a[n]
                                        u=b[0]
                                        p=b[1]
                                        users[u]=p
                                        n=n+1

                                #(users)
                                #(c)
                                if c in ['admin yellow','admin red','admin blue','admin green']:
                                        if enter.get()!=users['{}'.format(c)]:
                                                t="Old Password is Wrong"
                                                Login.warning(t)
                                                enter.delete(0,'end')
                                        else:
                                                if enter2.get() in [""," "]:
                                                        t="Please Enter the new password"
                                                        Login.warning(t)
                                                else:
                                                        z="update user SET password={} WHERE username LIKE('{}')".format(enter2.get(),c)
                                                        querry.execute(z)
                                                        connect.commit()
                                                        frame.destroy()
                                                        Login.swap(self.f1)
                                else:
                                        if enter.get()!=users['admin']:
                                                t="Old Password is Wrong"
                                                Login.warning(t)
                                                enter.delete(0,'end')
                                        else:
                                                if enter2.get() in [""," "]:
                                                        t="Please Enter the new password"
                                                        Login.warning(t)
                                                else:
                                                        z="update user SET password={} WHERE username LIKE('admin')".format(enter2.get())
                                                        querry.execute(z)
                                                        connect.commit()
                                                        frame.destroy()
                                                        Login.swap(self.f1)

                        def cancel():
                                frame.destroy()
                        frame=tk.Frame(f6,width=500,height=200,bg="grey")
                        frame.place(x=400,y=100)
                        Label=tk.Label(frame,text="Enter Old Password",width=20,height=2)
                        Label.place(x=10,y=30)
                        enter=tk.Entry(frame,width=20,font=20)
                        enter.place(x=250,y=30)
                        Label2=tk.Label(frame,text="Enter New Password",width=20,height=2)
                        Label2.place(x=10,y=80)
                        enter2=tk.Entry(frame,width=20,font=20)
                        enter2.place(x=250,y=80)
                        btn2=tk.Button(frame,text="Change Password",width=20,height=2,command=change)
                        btn2.place(x=150,y=150)
                        btn1=tk.Button(frame,text="Cancel",width=10,height=2,command=cancel)
                        btn1.place(x=10,y=150)
                        
                        
                def openhelp():
                        os.system('''cmd /c "help.pdf"''')
                def openhelp2():
                        os.system('''cmd /c "help2.pdf"''')
                        
                
                def tog(frame):          
                        global table
                        global data
                        if frame.winfo_exists()==False:
                                frame=tk.Frame(f8,width=500,height=500,bg="grey")
                                table=ttk.Treeview(frame)
                                frame.place(x=120,y=150)
                        else:
                                frame.place(x=120,y=150)
                        postname=tk.Label(frame,text="Edit Post",font=20)
                        postname.place(x=200,y=0)
                        
                        delbtn=tk.Button(frame,text="delete",width=20,command=lambda:pop(table))
                        delbtn.place(x=250,y=450)
                        addbtn=tk.Button(frame,text="ADD",width=10,command=lambda:insert(table))
                        addbtn.place(x=400,y=50)
                        enter=tk.Label(frame,text="Enter New Post",font=20,bg="pink")
                        enter.place(x=30,y=50)
                        data=tk.Entry(frame,width=40)
                        data.place(x=150,y=50)
                        closebtn=tk.Button(frame,text="exit",width=20,command=lambda:close(frame))
                        closebtn.place(x=50,y=450)
                        post=tuple(show())
                        table['columns']=('Post Available',)
                        table.column('#0',width=0, stretch=tk.NO)
                        table.column('Post Available',anchor=tk.CENTER,width=300, stretch=tk.NO)   
                        table.heading('#0',text='',anchor=tk.CENTER)
                        table.heading('Post Available',text='Post Available',anchor=tk.CENTER)
                        tab(table)
                        table.place(x=50,y=100)      
                def writepost(c):
                        connect=sql.connect("data.db")
                        querry=connect.cursor()
                        a=""
                        for x in c:
                                if x != " ":
                                        a=a+x
                                else:
                                        pass
                        q="create table {} (candidate_name text,Votes int DEFAULT 0)".format(a)
                        querry.execute(q)
                        connect.commit()
                        connect.close()      
                
                def insert(table):
                        c=data.get()   
                        
                        if c in ['',' ']:
                                t="Please Enter Any Post"
                                Login.warning(t)
                        else:
                                File=open("file.File","a",newline='')
                                file2=open("data.csv","a",newline='')
                                File.write(c)
                                File.write('\n')
                                File.close()
                                data.delete(0,'end')
                                tab(table)
                        post_list=show()  
                        select_post_list=post_list
                        if len(post_list)==0:
                                var2.set("No Post Found!")
                                select_post=tk.OptionMenu(add,var2,value="No Post Found!")
                                select_post.config(width=20,height=2)
                                select_post.place(x=200,y=140)
                        else:
                                var2.set(select_post_list[0])
                                select_post=tk.OptionMenu(add,var2,*select_post_list)
                                select_post.config(width=20,height=2)
                                select_post.place(x=200,y=140)
                        writepost(c)

                def show():
                        File=open("file.File","r",newline='')
                        List1=[]
                        for x in File:
                                List1.append(x.strip('\n'))
                        File.close()
                        List1.pop(0)
                        return(List1)
                def pop2(c):
                        connect=sql.connect("data.db")
                        querry=connect.cursor()
                        a=""
                        for x in c:
                                if x != " ":
                                        a=a+x
                                else:
                                        pass
                        
                        q="DROP table {}".format(a)
                        querry.execute(q)
                        connect.commit()
                        connect.close() 
                        view_data()   
                        
                                   
                def pop(table):
                        
                        File=open("file.File","r",newline='')
                        LIST=[]
                        delete=table.focus()
                        content=table.item(delete)
                        row=content['values']
                        l=len(row)
                        
                        
                        if l==0:
                                t="Please Select the Any Post"
                                Login.warning(t)
                        else:
                                t="This Will delete entire data related to this particular post"
                                f=Login.ask(t)
                                if f==True:
                                        for x in File:
                                                LIST.append(x.strip('\n'))
                                        d=row[0]
                                        if d in LIST:
                                                i=LIST.index(d)
                                                LIST.pop(i)
                                                File2=open("file.File","w",newline='')
                                                for x in LIST:
                                                        File2.write(x)
                                                        File2.write('\n')
                                                File2.close()
                                                File.close()
                                                tab(table)
                                                post_list=show()  
                                                select_post_list=post_list
                                                if len(post_list)==0:
                                                        var2.set("No Post Found!")
                                                        select_post=tk.OptionMenu(add,var2,value="No Post Found!")
                                                        select_post.config(width=20,height=2)
                                                        select_post.place(x=200,y=140)
                                                else:
                                                        var2.set(select_post_list[0])
                                                        select_post=tk.OptionMenu(add,var2,*select_post_list)
                                                        select_post.config(width=20,height=2)
                                                        select_post.place(x=200,y=140)
                                                pop2(d)              
                                        else:
                                                pass
                                else:
                                        pass
                                
                     
                
                def tab(table):
                        post=show()
                        Len=len(post)
                        if Len!=0:
                                n=0
                                table.delete(*table.get_children())
                                for x in post:
                                        table.insert(parent='',index=n,iid=n,text='', values=(x,))
                                        n=n+1
                        else:
                                table.delete(*table.get_children())
                                table.insert(parent='',index=0,iid=0,text='', values="No_Post_Found!")
                
                def close(frame):
                        frame.destroy()
        
                def writedata(table2):
                        connect=sql.connect("data.db")
                        querry=connect.cursor()
                        a=""
                        c=var2.get()
                        d=name.get()
                        for x in c:
                                if x != " ":
                                        a=a+x
                                else:
                                        pass
                        if d=="" or d==" ":
                                t="Please enter Candidate name!"
                                Login.warning(t)
                        else:
                                q="select candidate_name from {}".format(a)
                                querry.execute(q)
                                w=querry.fetchall()
                                if len(w)!=0:
                                        List=[]
                                        for x in w:
                                                List.append(x[0])
                                        if d in List:
                                                t="Candidate already there!"
                                                Login.warning(t)
                                                
                                        else:
                                                q="insert into {}(candidate_name) values('{}')".format(a,d)
                                                querry.execute(q)
                                                connect.commit()
                                else:
                                        q="insert into {}(candidate_name) values('{}')".format(a,d)
                                        querry.execute(q)
                                        connect.commit()
                        name.delete(0,'end')
                        view_data()
                        connect.close()

                        
                def view_data():
                        connect=sql.connect("data.db")
                        querry=connect.cursor()
                        q="SELECT name FROM sqlite_master WHERE type='table';"
                        querry.execute(q)
                        data=querry.fetchall()
                        n=0
                        List=[]
                      
                        if len(data)!=0:
                                table2.delete(*table2.get_children())
                                for x in data:
                                        List.append(x[0])
                                for y in List:
                                        q="select candidate_name from {}".format(y)
                                        querry.execute(q)
                                        data2=querry.fetchall()
                                        if len(data2)!=0:
                                                List2=[]
                                                for z in data2:
                                                        List2.append(z[0])
                                                for d in List2:
                                                        table2.insert(parent='',index=n,iid=n,text='',values=(d,y))
                                                        n=n+1
                                                List2=[]
                                if n==0:
                                        table2.delete(*table2.get_children())
                                        table2.insert(parent='',index=0,iid=0,text='',values=("No data Found!","error"))
                                
                                        

                        else:
                                table2.delete(*table2.get_children())
                                table2.insert(parent='',index=0,iid=0,text='',values=("No data Found!","error"))

                def delete():
                        connect=sql.connect("data.db")
                        querry=connect.cursor()
                        delete=table2.focus()
                        content=table2.item(delete)
                        row=content['values']
                        
                        if len(row)!=0 and row[1]!="error":
                                q="delete from {} where candidate_name LIKE ('{}')".format(row[1],row[0])
                                querry.execute(q)
                                connect.commit()
                                connect.close()
                                view_data()
                        else:
                                t="Please select a candidate"
                                Login.warning(t)

                def change3(self):
                        x=var4.get()
                        heading56.config(text="Results for post of {}".format(x))
                        connect=sql.connect("data.db")
                        querry=connect.cursor()
                        a=""
                        c=var4.get()
                        for x in c:
                                if x != " ":
                                        a=a+x
                                else:
                                        pass
                        q="select * from {}".format(a)
                        querry.execute(q)
                        dat=querry.fetchall()
                        q="select SUM(Votes) from {}".format(a)
                        querry.execute(q)
                        k=querry.fetchall()
                        j=k[0]
                        l=j[0]
                        
                        #table3.delete(*table2.get_children())
                        if len(dat)!=0:
                                table3.delete(*table3.get_children())
                                n=0
                                for y in dat:
                                        table3.insert(parent='',index=n,iid=n,text='',values=(y))
                                        n=n+1
                                lab.config(text="Total Votes Count {}".format(l))
                        else:
                                table3.delete(*table3.get_children())
                                table3.insert(parent='',index=0,iid=0,text='',values=("No Data found!","Error!"))
                                lab.config(text="Total Votes Count 0")



                        
                
                        
                        




                        

        
                                        
                #--------------------------------------window info-------------------------------------------------------------------
                
                global f3
                global f2
                global f4
                global f5
                global f6
                global f7
                global f8
                global f9
                global frame
                global tkvarq
                global table
                
                self.root=tk.Tk()
                self.l=self.root.winfo_screenheight()
                self.w=self.root.winfo_screenwidth()
                if self.w==1600 or self.w>1600:
                        self.root.geometry('{}x{}+0+0'.format(self.w-400,self.l-80))
                elif self.w==1280 or self.w>1280:
                        self.root.geometry('{}x{}+0+0'.format(self.w-200,self.l-80))
                else:
                        self.root.geometry('1080x720+0+0')
                        

                #self.root.geometry('{}x{}+0+0'.format(self.w-200,self.l-80))
                self.root.resizable(False,False)
                self.root.title("Vote_1.O")
                self.root.iconbitmap('icon.ico')
                f2=tk.Frame(self.root)
                f3=tk.Frame(self.root)
                f4=tk.Frame(self.root)
                f5=tk.Frame(self.root)
                f6=tk.Frame(self.root)
                f7=tk.Frame(self.root)
                f8=tk.Frame(self.root)
                f9=tk.Frame(self.root)
                







                #--------------------------------------Login window-------------------------------------------------------------------
                self.img=tk.PhotoImage(file="image.png")
                self.f1=tk.Frame(self.root)
                
                self.f1.place(x=0,y=0,relwidth=1,relheight=1)
                self.background1=tk.Label(master=self.f1,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
                self.Login_Frame=tk.Frame(master=self.f1,
                height=200,
                width=500)
                self.Login_Frame.place(x=290,y=210)
                self.username=tk.Label(master=self.Login_Frame,
                  text="Username",
                  font=("Arial Black",10))
                self.username.place(x=20,y=40)
                self.entry_username=tk.Entry(master=self.Login_Frame,
                        width=40)
                self.entry_username.place(x=25,y=60)

                self.password=tk.Label(master=self.Login_Frame,
                  text="Password",
                  font=("Arial Black",10))
                self.password.place(x=20,y=90)
                self.entry_password=tk.Entry(master=self.Login_Frame,
                        width=40,show="*")
                self.entry_password.place(x=25,y=110)

                self.login=tk.Button(master=self.f1,
                text="Login",
                width=20,
                height=2,
                relief=tk.RAISED,
                bg="pink",command=lambda : Login.Check_user(self.entry_username,self.entry_password,f2))
                self.login.place(x=350,y=390)

                self.desc=tk.Label(master=self.f1,
                text="VOTE_1.o",
                fg="purple",
                font=("Eras Bold ITC" ,20),
                underline=1)
                self.desc.place(x=565,y=290)
                self.credit1=tk.Label(self.f1,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit1.pack(side=tk.BOTTOM)

                #--------------------------------------Login_Window_end-------------------------------------------------------------------

                
                
                
                #---------------------------------------Option_Menu-----------------------------------------------------------------------------
                self.background2=tk.Label(master=f2,
                    image=self.img).place(x=0,y=0,relwidth=1,relheight=1)

                self.option1=tk.Button(master=f2,
                        text="Add Candidates",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f4))
                self.option1.place(x=40,y=360)
                
                self.option2=tk.Button(master=f2,
                        text="LogOut",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=Login.logout
                        )
                self.option2.place(x=400,y=360)
                self.option3=tk.Button(master=f2,
                        text="Generate OTVC",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f3))
                self.option3.place(x=760,y=360)

                self.option4=tk.Button(master=f2,
                        text="Launch Voting Program",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=launch)
                self.option4.place(x=40,y=150)
                self.option5=tk.Button(master=f2,
                        text="View Result",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f5))
                self.option5.place(x=400,y=150)
                self.option6=tk.Button(master=f2,
                        text="User",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f6))
                self.option6.place(x=760,y=150)
                self.option7=tk.Button(master=f2,
                        text="Other Post",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f8))
                self.option7.place(x=40,y=570)
                self.option8=tk.Button(master=f2,
                        text="Other Post Result",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f9))
                self.option8.place(x=400,y=570)

                self.heading=tk.Label(master=f2,
                        text="Vote_1.o",
                        fg="purple",
                    font=("Eras Bold ITC" ,40),
                    underline=1)
                self.heading.place(x=0,y=0)
                self.credit2=tk.Label(f2,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit2.pack(side=tk.BOTTOM)
                
                self.help=tk.Button(f2,text="Help",width=10,height=2,command=openhelp2)
                self.help.place(x=970,y=60)
                #---------------------------------------Option_Menu_end-----------------------------------------------------------------------------
                
                
                
                
#---------------------------------------------------------OTVC WINDOW--------------------------------------------------------------------------------------
                #---------------sturcture----------------------------------------------------


                self.background2=tk.Label(master=f3,
                                                image=self.img).place(x=0,y=0,
                                                relwidth=1,
                                                relheight=1)
                self.l1=tk.Label(f3,text="Please Select the House",
                        width=70,
                        height=2,
                        font=("Segoe UI Black",11),
                        fg="brown",
                        relief=tk.GROOVE)
                self.l1.place(x=150,y=150)
                self.l4=tk.Label(f3,text="OTVC (One time voting code) Generator",
                        width='{}'.format(self.w),
                        font=("Impact",20),
                        fg="brown",
                        relief=tk.FLAT,
                        underline=1)
                self.l4.pack(side=tk.TOP)

                

                #---------------------------option menu---------------------------------------------
                self.option_list=["yellow","green","red","blue"]
                tkvarq=tk.StringVar(f3)
                tkvarq.set(self.option_list[0])
                self.sel_house=tk.OptionMenu(f3,tkvarq,*self.option_list,command=code_generator.action1)
                self.sel_house.config(width=20,height=2)
                self.sel_house.place(x=800,y=150)
                #------------------------------------------------------------------------        
                
                self.log_frame=tk.Frame(f3,width=400,
                                height=200)
                self.label=tk.Label(self.log_frame,text="LOG")
                self.label.pack()
                self.clearbtn=tk.Button(f3,text="Clear LOG",width=15,command=code_generator.clear)
                self.openbtn=tk.Button(f3,text="Get Code files for Printing",width=30,command=code_generator.openfile)
                self.openbtn.place(x=750,y=60)
                self.back=tk.Button(f3,text="Back",width=10,command=Login.back)
                self.back.place(x=150,y=60)

                self.credit3=tk.Label(f3,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit3.pack(side=tk.BOTTOM)
#-----------------------------------------------------------------OTVC end--------------------------------------------------------------
                
                
                
#--------------------------------------------------------------Add Candidates----------------------------------------------------------
                #---------------------------option menu---------------------------------------------

                global tkvarq2
                global var
                
                self.background3=tk.Label(master=f4,
                    image=self.img).place(x=0,y=0,relwidth=1,relheight=1)

                self.credit4=tk.Label(f4,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit4.pack(side=tk.BOTTOM)

                self.option_list2=["yellow","green","red","blue"]
                tkvarq2=tk.StringVar(f4)
                tkvarq2.set(self.option_list2[0])
                self.sel_house=tk.OptionMenu(f4,tkvarq2,*self.option_list2,command=candidate.update)
                self.sel_house.config(width=20,height=2)
                self.sel_house.place(x=780,y=150)

                #------------------------------------------------------------------------ 
                self.label1=tk.Label(f4,text="Please select house for which you want to add Candidates:",
                                width=50,
                                height=2,
                                font=30)
                self.label1.place(x=100,y=150)
                self.frame_add=tk.Frame(f4,width=400,
                                height=400)
                self.frame_add.place(x=100,y=250)

                self.frame_view=tk.Frame(f4,width=400,
                                height=400)
                self.frame_view.place(x=550,y=250)
                
                self.table=ttk.Treeview(self.frame_view,columns=("House_Captain","House_Vice_Captain"))
                self.table.heading("House_Captain",text="House Captain")
                self.table.heading("House_Vice_Captain",text="House Vice Captain")
                self.table['show']='headings'
                self.table.column("House_Captain",width=200)
                self.table.column("House_Vice_Captain",width=200)
                self.table.pack()

                
                
                
                self.label1_add=tk.Label(self.frame_add,text="Enter name",
                                width=10,
                                height=1,bg="yellow")
                self.label1_add.place(x=20,y=80)
                self.name=tk.Entry(self.frame_add,width=40)
                self.name.place(x=120,y=80)
                
                

                #---------------------------option menu---------------------------------------------
                self.select_post_list=["House_Captain","House_Vice_Captain"]
                var=tk.StringVar(f4)
                var.set(self.select_post_list[0])
                self.select_post=tk.OptionMenu(self.frame_add,var,*self.select_post_list)
                self.select_post.config(width=20,height=2)
                self.select_post.place(x=200,y=140)

                #------------------------------------------------------------------------
                self.label2_add=tk.Label(self.frame_add,text="Select Post",
                                width=10,
                                height=1,bg="yellow")
                self.label2_add.place(x=20,y=140)

                self.addbutton=tk.Button(self.frame_add,text="Add",width=20,command=candidate.add)
                self.addbutton.place(x=120,y=260)
                self.show=tk.Button(f4,text="delete",width=20,command=candidate.delete_data)
                self.show.place(x=550,y=550)
                self.hint=tk.Label(f4,text="Just selct the candidate name and press the delete button!! ",bg="White",fg="Black",font=10)
                self.hint.place(x=550,y=500)
                self.back=tk.Button(f4,text="Back",width=10,command=Login.back)
                self.back.place(x=100,y=60)

                self.heading_add=tk.Label(self.frame_add,text="You are Entering Details for {} House".format(tkvarq.get()),
                                width=45,
                                font=10,bg="yellow")
                self.heading_add.place(x=0,y=20)
                
#--------------------------------------------RESULTS WINDOW----------------------------------------------------------------------------------
                self.background4=tk.Label(master=f5,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
                self.credit5=tk.Label(f5,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit5.pack(side=tk.BOTTOM)
                self.result_heading=tk.Label(f5,text="Results",width=50,font=("Impact",15))
                self.result_heading.place(x=0,y=0,relwidth=1)
                self.result_heading2=tk.Label(f5,text="Select House for Viewing Results",width=50,height=2)
                self.result_heading2.place(x=300,y=100)
                self.option_list3=["yellow","green","red","blue"]
                tkvarq3=tk.StringVar(f5)
                tkvarq3.set(self.option_list3[0])
                self.select_house=tk.OptionMenu(f5,tkvarq3,*self.option_list3,command=update2)
                self.select_house.config(width=20,height=2)
                self.select_house.place(x=700,y=100)
                global result_frame_captain
                global result_frame_vice_captain
                global heading1
                global heading2
                result_frame_captain=tk.Frame(f5,width=400,height=400)
                result_frame_captain.place(x=100,y=200)
                result_frame_vice_captain=tk.Frame(f5,width=400,height=400)
                result_frame_vice_captain.place(x=600,y=200)

                heading1=tk.Label(result_frame_captain,text="Results for House Captain",font=('Arial Black',15),bg="{}".format(tkvarq3.get()))
                heading1.place(x=0,y=0,relwidth=1)
                heading2=tk.Label(result_frame_vice_captain,text="Results for House Vice Captain",font=('Arial Black',15),bg="{}".format(tkvarq3.get()))
                heading2.place(x=0,y=0,relwidth=1)
                btn=tk.Button(f5,text="Back",width=10,height=2,command=Login.back)
                btn.place(x=10,y=50)
#-------------------------------------------RESULT END------------------------------------------------------------------------------------------

#-------------------------------------------USER WINDOW----------------------------------------------------------------------------------------
                self.background4=tk.Label(master=f6,
                        image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
                self.credit6=tk.Label(f6,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit6.pack(side=tk.BOTTOM)
                self.reset=tk.Button(f6,text="Reset",width=10,height=2,command=reset)
                self.reset.place(x=530,y=200)
                self.back2=tk.Button(f6,text="Back",width=10,height=2,command=Login.back)
                self.back2.place(x=100,y=50)
                
                self.change_pass=tk.Button(f6,text="Change Password",width=20,height=2,command=changepassword)
                self.change_pass.place(x=500,y=150)
 #----------------------------------------USER WINDOW END--------------------------------------------------------------------------------------               
                
 #----------------------------------------HOUSE ADMIN USER WINDOW------------------------------------------------------------------------------               
                background5=tk.Label(master=f7,
                image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
                self.credit7=tk.Label(f7,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit7.pack(side=tk.BOTTOM)

                option1=tk.Button(master=f7,
                text="Luanch Voting Program",
                width=40,
                height=10,
                relief=tk.RAISED,
                bg="pink",command=launch)
                option1.place(x=40,y=150)
                
                option2=tk.Button(master=f7,
                        text="Add Candidate",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f4)
                        )
                option2.place(x=400,y=150)
                        
                option3=tk.Button(master=f7,
                        text="LogOut",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=Login.logout
                        )
                option3.place(x=40,y=360)
                        
                option4=tk.Button(master=f7,
                        text="Generate OTVC",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f3))
                option4.place(x=400,y=360)

                option5=tk.Button(master=f7,
                        text="User",
                        width=40,
                        height=10,
                        relief=tk.RAISED,
                        bg="pink",command=lambda:Login.swap(f6))
                option5.place(x=760,y=150)


                heading=tk.Label(master=f7,
                        text="Vote_1.o",
                        fg="purple",
                        font=("Eras Bold ITC" ,40),
                        underline=1)
                heading.place(x=0,y=0)

                help=tk.Button(f7,text="Help",width=10,height=2,command=openhelp)
                help.place(x=970,y=60)
#---------------------------------other post-----------------------------------------------------------------------------------------
                background6=tk.Label(master=f8,
                image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
                self.credit8=tk.Label(f8,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit8.pack(side=tk.BOTTOM)
                
                
                
                back=tk.Button(f8,text="back",width=10,command=lambda:Login.swap(f2))
                back.place(x=120,y=50)
                
                add=tk.Frame(f8,width=400,height=400)
                add.place(x=100,y=250)
                view=tk.Frame(f8,width=400,height=400)
                view.place(x=550,y=250)
                scrollbar=tk.Scrollbar(view)
                scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
                table2=ttk.Treeview(view,yscrollcommand = scrollbar.set)
                table2['columns']=("Candidate_Name","Post")
                table2.column('#0',width=0, stretch=tk.NO)
                table2.column('Candidate_Name',anchor=tk.CENTER,width=300, stretch=tk.NO)
                table2.column('Post',anchor=tk.CENTER,width=300, stretch=tk.NO)
                        
                table2.heading('#0',text='',anchor=tk.CENTER)
                table2.heading('Candidate_Name',text='Candidate Name',anchor=tk.CENTER)
                table2.heading('Post',text='Post',anchor=tk.CENTER)
                table2.pack()
                scrollbar.config( command = table2.yview )
                label1_add=tk.Label(add,text="Enter name",
                                width=10,
                                height=1,bg="yellow")
                label1_add.place(x=20,y=80)
                name=tk.Entry(add,width=40)
                name.place(x=120,y=80)
                post_list=show()
                select_post_list=post_list
                var2=tk.StringVar(f8)
                if len(post_list)==0:
                        var2.set("No Post Found!")
                        select_post=tk.OptionMenu(add,var2,value="No Post Found!")
                        select_post.config(width=20,height=2)
                        select_post.place(x=200,y=140)
                else:
                        var2.set(select_post_list[0])
                        select_post=tk.OptionMenu(add,var2,*select_post_list)
                        select_post.config(width=20,height=2)
                        select_post.place(x=200,y=140)

                label2_add=tk.Label(add,text="Select Post",
                                width=10,
                                height=1,bg="yellow")
                label2_add.place(x=20,y=140)

                addbutton=tk.Button(add,text="Add",width=20,command=lambda:writedata(table2))
                addbutton.place(x=120,y=260)
                delete_button=tk.Button(f8,text="Delete",width=20,command=delete)
                delete_button.place(x=750,y=600)
                post=tk.Button(add,text="edit post",width=20,command=lambda:tog(frame))
                post.place(x=120,y=300)
                
                head=tk.Label(add,text="Entering Data For Special Post",width=45,font=10,bg="yellow")
                head.place(x=0,y=0)

                


                frame=tk.Frame(f8,width=500,height=500,bg="grey")
                table=ttk.Treeview(frame)
                
                view_data()
 #---------------------------other post end------------------------------------------------------
 # 
 # -----------------other post result window-----------------------------------------------------

                background7=tk.Label(master=f9,
                image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
                self.credit9=tk.Label(f9,text="This software is developed by-Abhinav Vishwakarma class:-XII Science batch (2020-2021)",
                font=("Impact",15),height=1,width='{}'.format(self.w))
                self.credit9.pack(side=tk.BOTTOM)
                
                
                  
                
                back=tk.Button(f9,text="back",width=10,command=lambda:Login.swap(f2))
                back.place(x=120,y=50)

                result_heading=tk.Label(f9,text="Results for Other Post",width=50,font=("Impact",15))
                result_heading.place(x=0,y=0,relwidth=1)
                result_heading2=tk.Label(f9,text="Select Post for Viewing Results",width=50,height=2)
                result_heading2.place(x=300,y=100)
                post_list2=show()
                select_post=post_list2
                var4=tk.StringVar(f9)
                if len(post_list2)==0:
                        var4.set("No Post Found!")
                        select_post1=tk.OptionMenu(f9,var4,value="No Post Found!")
                        select_post1.config(width=20,height=2)
                        select_post1.place(x=700,y=100)
                else:
                        var4.set(select_post[0])
                        select_post1=tk.OptionMenu(f9,var4,*select_post,command=change3)
                        select_post1.config(width=20,height=2)
                        select_post1.place(x=700,y=100)
                
                result_frame=tk.Frame(f9,width=400,height=400)
                result_frame.place(x=300,y=200)
                fra=tk.Frame(result_frame,height=2)
                fra.pack(side=tk.BOTTOM,fill=tk.X)      

                heading56=tk.Label(result_frame,text="Results for post of {}".format(select_post[0]),font=('Arial Black',13),bg="Purple",fg="White")
                heading56.place(x=0,y=0,relwidth=1)
                scrollbar2=tk.Scrollbar(result_frame)
                scrollbar2.pack(side=tk.RIGHT,fill=tk.Y)
                table3=ttk.Treeview(result_frame,yscrollcommand = scrollbar2.set)
                table3['columns']=("Candidate_Name","Vote")
                table3.column('#0',width=0, stretch=tk.NO)
                table3.column('Candidate_Name',anchor=tk.CENTER,width=300, stretch=tk.NO)
                table3.column('Vote',anchor=tk.CENTER,width=300, stretch=tk.NO)
                        
                table3.heading('#0',text='',anchor=tk.CENTER)
                table3.heading('Candidate_Name',text='Candidate Name',anchor=tk.CENTER)
                table3.heading('Vote',text='Votes Count',anchor=tk.CENTER)
                table3.pack()
                scrollbar.config( command = table3.yview )
                lab=tk.Label(result_frame,text="Total Votes Count 0",font=13)
                lab.pack(side=tk.BOTTOM,fill=tk.X)
                
                change3(self)
                
                



#------------------------------------------------------END----------------------------------------------------------------------------

                
                self.f1.tkraise()
                self.root.mainloop()


   


  




Window()



