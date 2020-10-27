# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 07:11:25 2020

@author: utsav
"""


#JaiShriGanesh
#gui and database

def employee():
    emplogintop=Toplevel()
    emplogintop.title('EMPLOYEE LOGIN')
    emplogintop.geometry('250x80')
    Label(emplogintop,text='ID:').grid(row=0,column=0)
    Label(emplogintop,text="PASSWORD:").grid(row=1,column=0)
    ent_loginid=Entry(emplogintop)
    ent_loginid.grid(row=0,column=1)
    ent_loginpass=Entry(emplogintop)
    ent_loginpass.grid(row=1,column=1)
    
    
    
    
    
    
    
    #functioning of main employee portal after succesfull login
    def employeeportal():
        empportal=Toplevel()
        empportal.title("WELCOME EMPLOYEE")
        empportal.geometry('700x450')
        
        Label(empportal,text='WELCOME TO ACADA 2.0' ).grid(row=0,column=0,columnspan=5,padx=50)
        Label(empportal,text="MARK ATTENDANCE").grid(row=1,column=0,padx=10,pady=10)
        
        #making show pending jobs to employee treeviw
        
        emppendtv=ttk.Treeview(empportal,height=8,columns=('cus_id','No. of jobs','location','distance','time'))
        emppendtv.grid(row=3,column=0,columnspan=5,pady=10)
        emppendtv.heading('#1',text='cus_id')
        emppendtv.heading('#2',text='no. of jobs')
        emppendtv.heading('#3',text='location')
        emppendtv.heading('#4',text='distance(km)')
        emppendtv.heading('#5',text='time(minutes)')
        #emppendtv.heading('#6',text='status')
        
        emppendtv['show']='headings'
        emppendtv.column('cus_id',width=100,anchor='center')
        emppendtv.column('No. of jobs',width=100,anchor='center')
        emppendtv.column('location',width=100,anchor='center')
        emppendtv.column('distance',width=100,anchor='center')
        emppendtv.column('time',width=100,anchor='center')
        #emppendtv.column('status',width=100,anchor='center')
        
        
        #making showdone treeview for employeye
        
        empdonetv=ttk.Treeview(empportal,height=8,columns=('cus_id','No. of jobs','location','distance','time'))
        empdonetv.grid(row=5,column=0,columnspan=5,pady=5)
        empdonetv.heading('#1',text='cus_id')
        empdonetv.heading('#2',text='no. of jobs')
        empdonetv.heading('#3',text='location')
        empdonetv.heading('#4',text='distance(km)')
        empdonetv.heading('#5',text='time(minutes)')
        #empdonetv.heading('#6',text='status')
        
        empdonetv['show']='headings'
        empdonetv.column('cus_id',width=100,anchor='center')
        empdonetv.column('No. of jobs',width=100,anchor='center')
        empdonetv.column('location',width=100,anchor='center')
        empdonetv.column('distance',width=100,anchor='center')
        empdonetv.column('time',width=100,anchor='center')
        #empdonetv.column('status',width=100,anchor='center')
        
        
        
        
        def showdonejob():
            empdonetv.delete(*empdonetv.get_children())
            cur.execute('select cus_id,count(job_id),cus_location,distance,sum(problem_time) from cusjobs where ass_emp_id=%s and job_status=%s and emp_ass_date=curdate() group by cus_location',(tempidemp,'done'))
            itemid=1
            for i in cur:
                empdonetv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3],i[4]))
                itemid+=1
            itemid=1
            conn.commit()
            
            
            
            
            
            
            
        def showpendingjob():
            emppendtv.delete(*emppendtv.get_children())
            cur.execute('select cus_id,count(job_id),cus_location,distance,sum(problem_time) from cusjobs where ass_emp_id=%s and job_status=%s and emp_ass_date=curdate() group by cus_location',(tempidemp,'pending'))
            itemid=1
            for i in cur:
                emppendtv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3],i[4]))
                itemid+=1
            itemid=1
            conn.commit()
        
        
        
        showdonejobbt=Button(empportal,text='SHOW DONE JOBS TODAY',command=showdonejob)
        showpendingjobbt=Button(empportal,text='SHOW PENDING JOBS TODAY',command=showpendingjob)
        showdonejobbt.grid(row=4,column=0)
        showpendingjobbt.grid(row=2,column=0)
        
        
        
        
        
        
        
        
        
        def markarrival():
            returneda,returnedb=markattendance1()
            if returneda==1:
                cur.execute('select emp_name from empdata where emp_id=%s',(returnedb))
                tempname=cur.fetchone()
                
                cur.execute('insert into empattendance(workdate,day,emp_id,emp_name,arrival) values(curdate(),dayname(curdate()),%s,%s,curtime())',(returnedb,tempname[0]))
                conn.commit()
                
            else:
                cur.execute('select emp_name from empdata where emp_id=%s',(returnedb))
                tempname=cur.fetchone()
                
                cur.execute('insert into failedattempts(attempt_date,emp_id,emp_name,time) values(curdate(),%s,%s,curtime())',(returnedb,tempname[0]))
                conn.commit()
        markattendancebutton=Button(empportal,text='MARK ARRIVAL',command=markarrival)
        
        markattendancebutton.grid(row=1,column=1)
        
        
        def markdeparture():
            returneda,returnedb=markattendance1()
            if returneda==1:
                cur.execute('select emp_name from empdata where emp_id=%s',(returnedb))
                tempname=cur.fetchone()
                
                cur.execute('update empattendance set departure=curtime() where emp_id=%s',(returnedb))
                conn.commit()
                
            else:
                cur.execute('select emp_name from empdata where emp_id=%s',(returnedb))
                tempname=cur.fetchone()
                
                cur.execute('insert into failedattempts(attempt_date,emp_id,emp_name,time) values(curdate(),%s,%s,curtime())',(returnedb,tempname[0]))
                conn.commit()
        markattendancebutton=Button(empportal,text='MARK DEPARTURE',command=markdeparture)
        
        markattendancebutton.grid(row=1,column=2,padx=10,pady=10)
        
             
        
        
    
    
    
    
    
    def emplogin():
        global tempidemp
        tempidemp=ent_loginid.get()
        temppass=ent_loginpass.get()
        cur.execute('select count(*) from empdata where emp_id=%s and emp_pass=%s',(tempidemp,temppass))
        result=cur.fetchone()
        
        if result[0]!=1:
            messagebox.showinfo('ERROR','INVALID USERID AND PASSWORD')
            emplogintop.destroy()            
        else:
            emplogintop.destroy()
            employeeportal()
            
        
        
    emploginsubmit=Button(emplogintop,text="LOGIN",command=emplogin)
    emploginsubmit.grid(row=2,column=1)
    
        
    
    
    

#admin portal button functioning
def admin():
    
    
    admintop=Toplevel()
    admintop.title('ADMIN ACADA 2.0)')
    admintop.geometry("600x400")
    
    #defining add new employee button functioning
    def addemp():
        addemptop=Toplevel()
        addemptop.title('ADD EMPLOYEE')
        addemptop.geometry("700x300")
        
        Label(addemptop,text="Enter name:").grid(row=0,column=0,padx=10,pady=10)
        ent_name=Entry(addemptop)
        ent_name.grid(row=0,column=1,padx=10,pady=10)
        
        Label(addemptop,text="Enter email:").grid(row=0,column=2,padx=10,pady=10)
        ent_email=Entry(addemptop)
        ent_email.grid(row=0,column=3,padx=10,pady=10)
        
        Label(addemptop,text="Enter dob (DDMMYYYY):").grid(row=1,column=0,padx=10,pady=10)
        ent_dob=Entry(addemptop)
        ent_dob.grid(row=1,column=1,padx=10,pady=10)
        
        Label(addemptop,text="Enter mobile no.:").grid(row=1,column=2,padx=10,pady=10)
        ent_mno=Entry(addemptop)
        ent_mno.grid(row=1,column=3,padx=10,pady=10)
        
        Label(addemptop,text="PRESS ENTER TO GENERATE ID:").grid(row=2,column=0,padx=10,pady=10)
        ent_id=Entry(addemptop)
        ent_id.grid(row=2,column=1,padx=10,pady=10)
        ent_id.insert(0,"ENTER")
        
        #GENERATION OF TOKEN MEANS SUCCESSFULL ADDITION OF EMPLOYEE
        
        #defining functionality of gen_token() with database integration
        
        def gen_token():
            cur.execute('insert into empdata(emp_token_id,emp_id,emp_name,emp_email,emp_dob,emp_mno,emp_joindate) values(%s,%s,%s,%s,%s,%s,curdate())',('tmt'+ent_dob.get()[-2:]+ent_mno.get()[-2:],ent_id.get(),ent_name.get(),ent_email.get(),ent_dob.get(),ent_mno.get()))
            conn.commit()
            #cur.execute("insert into emplogindata(token_id,emp_id,emp_name) values(%s,%s,%s)",('tmt'+ent_dob.get()[-2:]+ent_mno.get()[-2:],ent_id.get(),ent_name.get()))
            #conn.commit()
            messagebox.showinfo("DONE","EMPLOYEE ADDED TO RECORDS")
            addemptop.destroy()
        
        
        tokenbt=Button(addemptop,text="GENERATE TOKEN",command=gen_token)
        tokenbt.grid(row=3,column=3,padx=10,pady=10)
        
        
        
        #defining add face command for new employee adition
        
        def addface():
            catchempfacefn(ent_id.get())
        
            
        
        
        addfacebt=Button(addemptop,text="ADD FACE",command=addface)
        addfacebt.grid(row=2,column=3,padx=10,pady=10)
        
        
        
        
        
        
        #defining id generation function on pressing enter to ent_id
        def gen_id():
            ent_id.delete(0,END)
            ent_id.insert(0,ent_name.get()[0:2]+ent_mno.get()[0:2]+ent_dob.get()[0:2])
            
        ent_id.bind("<Return>", (lambda event:gen_id()))
        
    
    
    
    def addjob():
        ent_jobnamead.config(state='normal')
        ent_jobtimead.config(state='normal')
        
    
    #adding a new employee to the company and generating a token_id
    addempbt=Button(admintop,text="ADD EMPLOYEE",command=addemp)
    addempbt.grid(row=0,column=0,padx=10,pady=10)
    Label(admintop,text=':TO ADD A NEW EMPLOYEE AND GENERATE A TOKEN ID').grid(row=0,column=1,columnspan=4)
    
    #adding new job types to the database
    addnewjobbt=Button(admintop,text='ADD A NEW JOB TYPE',command=addjob)
    addnewjobbt.grid(row=1,column=0,padx=10,pady=10)
    
    Label(admintop,text="ENTER JOB NAME:").grid(row=1,column=1)
    ent_jobnamead=Entry(admintop,state='disabled')
    ent_jobnamead.grid(row=1,column=2)
    
    Label(admintop,text="ENTER TIME:").grid(row=1,column=3)
    ent_jobtimead=Entry(admintop,state='disabled')
    ent_jobtimead.grid(row=1,column=4)
    
    def addjobtype():
        cur.execute('insert into jobtypes(job_name,expected_time) values(%s,%s)',(ent_jobnamead.get(),ent_jobtimead.get()))
        conn.commit()
        messagebox.showinfo('DONE','NEW JOB NAME ADDED')
        ent_jobnamead.delete(0,END)
        ent_jobtimead.delete(0,END)
        ent_jobnamead.config(state='disabled')
        ent_jobtimead.config(state='disabled')
        
        
    ent_jobtimead.bind("<Return>", (lambda event:addjobtype()))
    
    
    #assigning jobs to the  employeees
    
    def assignjob():
        jobportal=Toplevel()
        jobportal.title('admin assign job portal')
        jobportal.geometry('950x450')
        #Label(jobportal,text='HERE PENDING JOBS ARE PRESENETED WITH ESTIMATED TIME INCLUDING TRAVELLING AND SERVICE TIME\nFor Travelling we are assuming 3 minutes per km taking traffic in consideration as of now').grid(row=0,column=0,columnspan=6)
        Label(jobportal,text='PARAMETERS-1km=3 minutes to travel\n RE-FETCH IF CHANGES MADE').grid(row=0,column=0,sticky=N)
        
        #making a treeview with current pending jobs summary
        
        adjobtv=ttk.Treeview(jobportal,height=10,columns=('cus_id','No. of jobs','location','distance','time'))
        adjobtv.grid(row=2,column=0,columnspan=5)
        adjobtv.heading('#1',text='cus_id')
        adjobtv.heading('#2',text='no. of jobs')
        adjobtv.heading('#3',text='location')
        adjobtv.heading('#4',text='distance(km)')
        adjobtv.heading('#5',text='time(minutes)')
        
        adjobtv['show']='headings'
        adjobtv.column('cus_id',width=100,anchor='center')
        adjobtv.column('No. of jobs',width=100,anchor='center')
        adjobtv.column('location',width=100,anchor='center')
        adjobtv.column('distance',width=100,anchor='center')
        adjobtv.column('time',width=100,anchor='center')
        
       
        #we might add a verticle scroll bar to treeview later on if needed
        
        #treeview pending job summary making done
        
        #making a treeview for showing present day employee work status
        
        empworktv=ttk.Treeview(jobportal,height=10,columns=('emp_id','No. of jobs','Time','jobs_done'))
        empworktv.grid(row=2,column=6,columnspan=4,padx=15)
        empworktv.heading('#1',text='emp_id')
        empworktv.heading('#2',text='no. of jobs')
        empworktv.heading('#3',text='Time')
        empworktv.heading('#4',text='Jobs_done')
        empworktv['show']='headings'
        empworktv.column('emp_id',width=100,anchor='center')
        empworktv.column('No. of jobs',width=100,anchor='center')
        empworktv.column('Time',width=100,anchor='center')
        empworktv.column('Time',width=100,anchor='center')
        empworktv.column('jobs_done',width=100,anchor='center')
        
        
        #treeview employee present day work status making done
        
        #making actual job assigning system
        Label(jobportal,text='To assign jobs,select an employee and assign a cus_id').grid(row=3,column=0,columnspan=5)
        cur.execute('select emp_id from empdata')
        tempemplist=[]
        for i in cur:
            tempemplist.append(i[0]) 
        conn.commit() 
        
        
        Label(jobportal,text="SELECT EMP:").grid(row=4,column=0)
        ent_selectemp=ttk.Combobox(jobportal,values=tempemplist,width=10)
        ent_selectemp.grid(row=4,column=1)
        
        
        Label(jobportal,text="ASSIGN CUSTOMER").grid(row=4,column=2)
        ent_assigncus=Entry(jobportal)
        ent_assigncus.grid(row=4,column=3) 
        
        
        
        
        
        
        def assignworkemp():
            cur.execute('select time from empwork where emp_id=%s',(ent_selectemp.get()))
            temptotaltime=cur.fetchone()
            if int(temptotaltime[0])<400:
                
                cur.execute('select count(*) from (select * from cusjobs where ass_emp_id is NULL and cus_id=%s group by cus_location) as derivedtablealias',(ent_assigncus.get()))
                tempx=cur.fetchone()
                conn.commit()
                
                #if choosen customer has jobs at only one location
                if tempx[0]==1:
                    cur.execute('select count(job_id),distance,sum(problem_time),cus_location from cusjobs where ass_emp_id is NULL and cus_id=%s group by cus_location',(ent_assigncus.get()))
                    tempworkdata=cur.fetchone()
                    conn.commit()
                    cur.execute('update cusjobs set emp_ass_date=curdate() where cus_id=%s and job_status=%s',(ent_assigncus.get(),'pending'))
                    conn.commit()
                    
                    
                    cur.execute('select no_jobs,time from empwork where emp_id=%s',(ent_selectemp.get()))
                    tempadd=cur.fetchone()
                    conn.commit()
                    
                    cur.execute('select count(*) from cusjobs where ass_emp_id=%s and emp_ass_date=curdate() and cus_location=%s',(ent_selectemp.get(),tempworkdata[3]))
                    if cur.fetchone()[0]==0:
                        cur.execute('update empwork set no_jobs=%s,time=%s where emp_id=%s',(int(tempadd[0])+int(tempworkdata[0]),int(tempadd[1])+int(tempworkdata[2])+int(tempworkdata[1])*3,ent_selectemp.get()))
                        conn.commit()
                    else:
                        cur.execute('update empwork set no_jobs=%s,time=%s where emp_id=%s',(tempadd[0]+tempworkdata[0],tempadd[1]+tempworkdata[2],ent_selectemp.get()))
                        conn.commit()
                        
                    
                    
                    
                    cur.execute('update cusjobs set ass_emp_id=%s where cus_id=%s and job_status=%s',(ent_selectemp.get(),ent_assigncus.get(),'pending'))
                    conn.commit()
                    empworktv.delete(*empworktv.get_children())
                    itemid=1
                    cur.execute('select * from empwork')
                    for i in cur:
                        empworktv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3]))
                        itemid+=1
                    itemid=1
                    conn.commit()
                    
                
                    
                    
                    #print(tempworkdata)
                #if choosen customer has jobs at more than one locations    
                else:
                    
                    onelocation=simpledialog.askstring("INPUT","same cus has jobs at two locations\n enter one location name")
                    
                    cur.execute('select count(job_id),distance,sum(problem_time) from cusjobs where ass_emp_id is NULL and cus_id=%s and cus_location=%s group by cus_location',(ent_assigncus.get(),onelocation))
                    tempworkdata=cur.fetchone()
                    conn.commit()
                    
                    cur.execute('update empwork set no_jobs=%s,time=%s where emp_id=%s',(tempworkdata[0],tempworkdata[2]+int(tempworkdata[1])*3,ent_selectemp.get()))
                    conn.commit()
                    cur.execute('update cusjobs set ass_emp_id=%s where cus_id=%s and job_status=%s and cus_location=%s',(ent_selectemp.get(),ent_assigncus.get(),'pending',onelocation))
                    conn.commit()
                    empworktv.delete(*empworktv.get_children())
                    itemid=1
                    cur.execute('select * from empwork')
                    for i in cur:
                        empworktv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3]))
                        itemid+=1
                    itemid=1
                    conn.commit()
                    
                    #print(tempworkdata)
                    
                    
                    
                    
                    #cur.execute('update empwork set')
            else:
                messagebox.showinfo('sorry',"can't assign to this employee,work limit exceeded...try another")
        ent_assigncus.bind("<Return>", (lambda event:assignworkemp()))
        
           
            
        
        
        
        
        
              
        
        def fetchpendingsummary():
            adjobtv.delete(*adjobtv.get_children())
        
            cur.execute(' select cus_id,count(job_id),cus_location,distance,sum(problem_time) from cusjobs where ass_emp_id is NULL group by cus_location,cus_id order by cus_id')
            conn.commit()
            itemid=1
            for i in cur:
                adjobtv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3],(int(i[4])+(int(i[3])*3))))
                itemid+=1
            itemid=1  
            conn.commit()
                
        def fetchempwork():
            empworktv.delete(*empworktv.get_children()) 
            cur.execute('select * from empwork')
            itemid=1
            for i in cur:
                empworktv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3]))
                itemid+=1
            itemid=1
            conn.commit()
        
        
        def clearrecentwork():
            cur.execute('select emp_id from empdata')
            tempemplist=[]
            for i in cur:
                tempemplist.append(i[0])
            conn.commit()
            cur.execute('delete from empwork')
            conn.commit()
            itemid=1
            for i in range(len(tempemplist)):
                cur.execute('insert into empwork(emp_id,no_jobs,time,jobs_done) values(%s,%s,%s,%s)',(tempemplist[i],0,0,0))
                conn.commit()
            cur.execute('select * from empwork')
            empworktv.delete(*empworktv.get_children())    
            for i in cur:
                empworktv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3]))
                itemid+=1
            conn.commit()
            itemid=1
                
                
        
        
        
        fetchsummarypd=Button(jobportal,text='PENDING JOBS',command=fetchpendingsummary)
        fetchsummarypd.grid(row=1,column=0,pady=10)
        
        fetchempworkbt=Button(jobportal,text="EMP WORK ",command=fetchempwork)
        fetchempworkbt.grid(row=1,column=6,padx=15)
    
        #creating a button to clear recent assignments/refresh assignment
        clearassbt=Button(jobportal,text='CLEAR RECENT WORK',command=clearrecentwork)
        clearassbt.grid(row=1,column=7)       
        
    assignjobbt=Button(admintop,text='ASSIGN JOBS',command=assignjob)
    assignjobbt.grid(row=2,column=0,padx=10,pady=10)
    
    
    
    
    
    
    
    
    
    
        
def customer():
    cuslogintop=Toplevel()
    cuslogintop.title('CUSTOMER LOGIN')
    cuslogintop.geometry('250x80')
    Label(cuslogintop,text='ID:').grid(row=0,column=0)
    Label(cuslogintop,text="PASSWORD:").grid(row=1,column=0)
    ent_loginidcus=Entry(cuslogintop)
    ent_loginidcus.grid(row=0,column=1)
    ent_loginpasscus=Entry(cuslogintop)
    ent_loginpasscus.grid(row=1,column=1)
    
    
    def customerportal():
        cusportal=Toplevel()
        cusportal.title("WELCOME CUSTOME:  "+tempcusid)
        cusportal.geometry("1000x600")
        
        Label(cusportal,text='To add a service request').grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        Label(cusportal,text="enter problem :").grid(row=1,column=0)
        
        Label(cusportal,text='Enter product_id:').grid(row=1,column=2)
        Label(cusportal,text='Choose your location:').grid(row=2,column=0)
        Label(cusportal,text='Enter contact:').grid(row=2,column=2,pady=10)
        
        Label(cusportal,text='After submitting the request you will be alloted employee within 48 hours\nyou can check status in between').grid(row=3,column=0,columnspan=5)
        Label(cusportal,text='STATUS BAR').grid(row=5,column=0,pady=20)
        Label(cusportal,text='DOUBLE CLICK ON JOB NAME TO MARK IT DONE(available once you mark employee arrival)').grid(row=6,column=0,columnspan=9)
        
        
        
        cur.execute('select job_name from jobtypes')
        
    
        tempjoblist=[]
        for i in cur:
            tempjoblist.append(i[0])
        
        
        
        
        
        
        
        #ent_problem_name=Entry(cusportal,state="disabled")
        ent_problem_name=ttk.Combobox(cusportal,values=tempjoblist,width=20,state='disabled')
        ent_problem_name.grid(row=1,column=1,pady=10)
        ent_product_id=Entry(cusportal,state="disabled")
        ent_product_id.grid(row=1,column=3,pady=10)
        
        
        ent_cus_cno=Entry(cusportal,state='disabled')
        ent_cus_cno.grid(row=2,column=3)
        global locdist
        locdist={'malviya nagar':8,'jagatpura':2,'pratap nagar':4,'jhotwara':20}
        locations=[]
        for i in locdist:
            locations.append(i)
        
        ent_choose_location=ttk.Combobox(cusportal,values=locations,width=20)
        ent_choose_location.grid(row=2,column=1)
        ent_choose_location.current(0)
        ent_choose_location.config(state='disabled')
        
        #making a treeview to show job details and status to customer
        
        cusjobtv=ttk.Treeview(cusportal,height=5,columns=('job_id','cus_id','problem_name','problem_time','product_id','cus_location','distance','cus_cno','emp_id','job_status','req_date',"ass_date"))
        cusjobtv.grid(row=8,column=0,columnspan=9)
        cusjobtv.heading('#1',text='Job_id')
        cusjobtv.heading('#2',text='Cus_id')
        cusjobtv.heading('#3',text='Problem')
        cusjobtv.heading('#4',text='Time(minutes)')
        cusjobtv.heading('#5',text='Product_id')
        cusjobtv.heading('#6',text='Cus_location')
        cusjobtv.heading('#7',text='distance')
        cusjobtv.heading('#8',text='Cus_cno')
        cusjobtv.heading('#9',text='Emp_id')
        cusjobtv.heading('#10',text='STATUS')
        cusjobtv.heading('#11',text='reqDATE')
        cusjobtv.heading('#12',text='assDATE')
        cusjobtv['show']='headings'
        cusjobtv.column('job_id',width=100,anchor='center')
        cusjobtv.column('cus_id',width=100,anchor='center')
        cusjobtv.column('problem_name',width=100,anchor='center')
        cusjobtv.column('problem_time',width=100,anchor='center')
        cusjobtv.column('product_id',width=100,anchor='center')
        cusjobtv.column('cus_location',width=100,anchor='center')
        cusjobtv.column('distance',width=100,anchor='center')
        cusjobtv.column('cus_cno',width=100,anchor='center')
        cusjobtv.column('emp_id',width=100,anchor='center')
        cusjobtv.column('job_status',width=100,anchor='center')
        cusjobtv.column('req_date',width=100,anchor='center')
        cusjobtv.column('ass_date',width=100,anchor='center')
        
        #treeview ended till here only
        
        
        def fetchalljobscus():
            cusjobtv.delete(*cusjobtv.get_children())
            cur.execute('select * from cusjobs where cus_id=%s',(tempcusid))
            itemid=1
            for i in cur:
                cusjobtv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))
                itemid+=1
            itemid=1  
            conn.commit()
         
        def fetchpendingjobscus():
            cusjobtv.delete(*cusjobtv.get_children())
            cur.execute('select * from cusjobs where cus_id=%s and job_status=%s',(tempcusid,'pending'))
            itemid=1
            for i in cur:
                cusjobtv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))
                itemid+=1
            itemid=1  
            conn.commit()
            
                
        
        
        
        fetchalljobsbt=Button(cusportal,text='FETCH ALL JOBS',command=fetchalljobscus)
        fetchalljobsbt.grid(row=7,column=1)
        fetchpendingjobsbt=Button(cusportal,text="FETCH PENDING JOBS",command=fetchpendingjobscus)
        fetchpendingjobsbt.grid(row=7,column=3)
        
        #know your employee ->can be used to find emp name and contact after emp is assigned to customer
        
        Label(cusportal,text="KNOW YOUR SERVICE BOY->insert emp_id and press enter and mark employee arrival if assigned\n TO UPDATE ANY CHANGES MADE PLEASE RE-FETCH DATA" ).grid(row=9,column=0,padx=15,columnspan=4)
        Label(cusportal,text="ENTER EMP ID:").grid(row=10,column=0,pady=10)
        ent_knowempid=Entry(cusportal)
        ent_knowempid.grid(row=10,column=1)
        ent_knowempname=Entry(cusportal,state='disabled')
        ent_knowempname.grid(row=11,column=0,padx=10)
        ent_knowempcno=Entry(cusportal,state='disabled')
        ent_knowempcno.grid(row=11,column=1,padx=10)
        
        
        
        
        def markemparrival():
            returneda,returnedb=markattendance1()
            if returneda==1:
                cur.execute('insert into empcusvisit(cus_id,emp_id,date_service,arrival) values(%s,%s,curdate(),curtime())',(tempcusid,returnedb))
                conn.commit()
                ent_jobdone.config(state='normal')
            elif returneda==2:
                messagebox.showinfo('SORRY','FACE MISMATCH')
                
            
        
        def markempdeparture():
            returneda,returnedb=markattendance1()
            if returneda==1:
                cur.execute('update empcusvisit set departure=curtime() where cus_id=%s and date_service=curdate()',(tempcusid))
                conn.commit()
                ent_jobdone.config(state='disabled')
            elif returneda==2:
                messagebox.showinfo('SORRY','FACE MISMATCH')
            
        
        
        emparrivalbt=Button(cusportal,text="EMPLOYEE ARRIVAL",command=markemparrival)
        emparrivalbt.grid(row=10,column=3)
        empdeparturebt=Button(cusportal,text="EMPLOYEE departure",command=markempdeparture)
        empdeparturebt.grid(row=10,column=4)
        
        Label(cusportal,text="TO MARK A JOB DONE(enter id):").grid(row=11,column=3)
        ent_jobdone=Entry(cusportal,state='disabled')
        ent_jobdone.grid(row=11,column=4)
        
       
        def jobdone():
            cur.execute('update cusjobs set job_status=%s where job_id=%s',('done',ent_jobdone.get()))
            conn.commit()
            messagebox.showinfo('YES','status updated...RE-FETCH JOB DATA TO VIEW THE CHANGES')
            
            
        
        ent_jobdone.bind("<Return>", (lambda event:jobdone()))
        
        
        def fetchempdet():
            
            cur.execute('select emp_name,emp_mno from empdata where emp_id=%s',(ent_knowempid.get()))
            tempdata=cur.fetchone()
            ent_knowempname.config(state='normal')
            ent_knowempname.delete(0,END)
            
            ent_knowempname.insert(0,tempdata[0])
            ent_knowempname.config(state='disabled')
            ent_knowempcno.config(state='normal')
            ent_knowempcno.delete(0,END)
            ent_knowempcno.insert(0,tempdata[1])
            ent_knowempcno.config(state='disabled')
            conn.commit()
            
            
            
            
        
        ent_knowempid.bind("<Return>", (lambda event:fetchempdet()))
        
        

        
        
        def submit_request():
            dateslice=str(dt.date.today())
            tempjob_id=tempcusid[:2]+ent_product_id.get()[:2]+dateslice[-2:]
            #temp_job_status='pending'
            cur.execute('select expected_time from jobtypes where job_name=%s',(ent_problem_name.get()))
            temptime=cur.fetchone()[0]
            
            cur.execute('insert into cusjobs(job_id,cus_id,problem_name,problem_time,product_id,cus_location,distance,cus_cno,job_status,job_req_date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,curdate())',(tempjob_id,tempcusid,ent_problem_name.get(),temptime,ent_product_id.get(),ent_choose_location.get(),locdist[ent_choose_location.get()],ent_cus_cno.get(),'pending'))
            conn.commit()
            
            #cur.execute('select * from cusjobs where job_id=%s',(tempjob_id))
            #itemid=1
            #for i in cur:
            #   cusjobtv.insert('','end',"item"+str(itemid),values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
            #    itemid+=1
            #itemid=1  
            #conn.commit()
            submitreqbt.config(state='disabled')
            
            
            
        submitreqbt=Button(cusportal,text="SUBMIT REQUEST",command=submit_request,state='disabled')
        submitreqbt.grid(row=4,column=2)
        
        def add_request():
            ent_problem_name.delete(0,END)
            ent_product_id.delete(0,END)
            ent_cus_cno.delete(0,END)
            ent_choose_location.delete(0,END)
            
            ent_problem_name.config(state='normal')
            ent_product_id.config(state='normal')
            ent_cus_cno.config(state='normal')
            ent_choose_location.config(state='normal')
            submitreqbt.config(state='normal')
            
            
            
        addreqbt=Button(cusportal,text="ADD A REQUEST",command=add_request)
        addreqbt.grid(row=4,column=0)
        
                
        
        
        
        
        #refreshing the job list at customer end to see if a employee has been assigned or not
        def refresh_cusjobs():
            pass
        
        refreshbt=Button(cusportal,text="REFRESH",command=refresh_cusjobs,state='disabled')
        refreshbt.grid(row=5,column=2,pady=10)
        
        
        
        
        
       
        
        
        
        
        
        
        
    
    def cuslogin():
        global tempcusid
        tempcusid=ent_loginidcus.get()
        tempcuspass=ent_loginpasscus.get()
        cur.execute('select count(*) from cusdata where cus_id=%s and cus_pass=%s',(tempcusid,tempcuspass))
        result=cur.fetchone()
        
        if result[0]!=1:
            messagebox.showinfo('ERROR','INVALID USERID AND PASSWORD')
            cuslogintop.destroy()            
        else:
            cuslogintop.destroy()
            customerportal()
        
        
    cusloginsubmit=Button(cuslogintop,text="LOGIN",command=cuslogin)
    cusloginsubmit.grid(row=2,column=1)
    
    




#employee register function //we might add another funciton for customer register later on
def empregister():
    regtop=Toplevel()
    regtop.geometry('600x400')
    regtop.title('first time id password')
    
    Label(regtop,text='==>WELCOME TO THE COMPANY..HOPE YOU HAVE A WARMING EXPERIENCE HERE.',font=('Arial',9,'underline')).grid(row=0,pady=10,column=0,columnspan=6)
    Label(regtop,text='==>HERE IS YOUR COMPANY ID AND DETAILS ,CONFIRM THEM OR REPORT TO ADMIN FOR CHANGE',font=('Arial',9,'underline')).grid(row=1,pady=10,column=0,columnspan=6)
    Label(regtop,text='==>IF CONFIRMED CHOOSE A STRONG ID PASSWORD FOR LOGIN',font=('Arial',9,'underline')).grid(row=2,pady=10,column=0,columnspan=6)
    
    Label(regtop,text='ENTER TOKEN ID').grid(row=3,column=0,padx=10,pady=10)
    
    ent_token_id=Entry(regtop)
    ent_token_id.grid(row=3,column=1)
    
    
    Label(regtop,text='ID:').grid(row=4,column=0,pady=10)
    Label(regtop,text='NAME:').grid(row=4,column=2,padx=10,pady=10)
    Label(regtop,text='EMAIL:').grid(row=5,column=0,padx=10,pady=10)
    Label(regtop,text='DOB:').grid(row=5,column=2,padx=10,pady=10)
    Label(regtop,text='MOBILE NO:').grid(row=6,column=0,padx=10,pady=10)
    
    Label(regtop,text="PASSWORD:").grid(row=7,column=0,padx=10,pady=10)
    Label(regtop,text="RESET CODE:").grid(row=7,column=2,padx=10,pady=10)
    
    ent_check_id=Entry(regtop)
    ent_check_id.grid(row=4,column=1)
    ent_check_name=Entry(regtop)
    ent_check_name.grid(row=4,column=3)
    ent_check_email=Entry(regtop)
    ent_check_email.grid(row=5,column=1)
    ent_check_dob=Entry(regtop)
    ent_check_dob.grid(row=5,column=3)
    ent_check_mno=Entry(regtop)
    ent_check_mno.grid(row=6,column=1)
    
    ent_pass=Entry(regtop)
    ent_pass.grid(row=7,column=1)
    ent_pass.config(state='disabled')
    
    ent_resetcode=Entry(regtop)
    ent_resetcode.grid(row=7,column=3)
    ent_resetcode.config(state='disabled')
    
    
    
    def enable_pass_resetocde_entry():
        ent_pass.config(state='normal')
        ent_resetcode.config(state='normal')
        submitpassbutton.config(state='normal')
    
    confirmbutton=Button(regtop,text="CONFIRM",command=enable_pass_resetocde_entry)
    confirmbutton.grid(row=6,column=3,padx=10,pady=10)
    
    def submitpass():
        cur.execute('update empdata set emp_pass=%s,emp_reset=%s where emp_token_id=%s',(ent_pass.get(),ent_resetcode.get(),ent_token_id.get()))
        conn.commit()
        messagebox.showinfo('DONE','password and reset code updated')
        regtop.destroy()
        
    submitpassbutton=Button(regtop,text='SUBMIT',command=submitpass,state='disabled')
    submitpassbutton.grid(row=8,column=2,padx=10,pady=10)
    
    
    
    
    
    def fetch_token_details():
        token_id_temp=ent_token_id.get()
        tempc=[]
        cur.execute('select emp_token_id from empdata')
        conn.commit()
        
        for i in cur:
            tempc.append(i[0])
            
        
        if token_id_temp not in tempc:
            messagebox.showinfo('alas','invalid token id')
            regtop.destroy()
        else:
            cur.execute('select emp_id,emp_name,emp_email,emp_dob,emp_mno from empdata where emp_token_id=%s',(token_id_temp))
            for i in cur:
                ent_check_id.insert(0,i[0])
                ent_check_id.config(state='readonly')
                
                ent_check_name.insert(0,i[1])
                ent_check_name.config(state='readonly')
                
                ent_check_email.insert(0,i[2])
                ent_check_email.config(state='readonly')
                
                ent_check_dob.insert(0,i[3])
                ent_check_dob.config(state='readonly')
                
                ent_check_mno.insert(0,i[4])
                ent_check_mno.config(state='readonly')
    
    
    
    
    ent_token_id.bind("<Return>", (lambda event:fetch_token_details()))
    
    
def cusregister():
    cusregtop=Toplevel()
    cusregtop.title('CUSTOMER REGISTER')
    cusregtop.geometry('600x300')
    
    Label(cusregtop,text='ENTER ID:').grid(row=0,column=0)
    Label(cusregtop,text='ENTER NAME:').grid(row=0,column=2)
    Label(cusregtop,text='ENTER PASSWORD:').grid(row=1,column=0)
    Label(cusregtop,text='ENTER RESET CODE:').grid(row=1,column=2)
    
    ent_cusid=Entry(cusregtop)
    ent_cusid.grid(row=0,column=1,padx=10,pady=10)
    ent_cusname=Entry(cusregtop)
    ent_cusname.grid(row=0,column=3,padx=10,pady=10)
    ent_cuspass=Entry(cusregtop)
    ent_cuspass.grid(row=1,column=1,padx=10,pady=10)
    ent_cusreset=Entry(cusregtop)
    ent_cusreset.grid(row=1,column=3,padx=10,pady=10)
     
    
    def cusdatasubmit():
        
        cur.execute('insert into cusdata(cus_id,cus_name,cus_pass,cus_reset) values(%s,%s,%s,%s)',(ent_cusid.get(),ent_cusname.get(),ent_cuspass.get(),ent_cusreset.get()))
        conn.commit()
        messagebox.showinfo('DONE','CUSTOMER REGISTERED,ID PASSWORD SUBMITTED')
        cusregtop.destroy()
        
        
        
    cusdatasubmitbt=Button(cusregtop,text="SUBMIT & REGISTER",command=cusdatasubmit)
    cusdatasubmitbt.grid(row=2,column=3,padx=10)

import win32api
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import datetime as dt
import numpy as np
from catchempface import *
from atndmark import *

from tkinter.ttk import Combobox


#defining databases on if not exists basis
#creating database
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234')
cur = conn.cursor()
cur.execute("create database if not exists acada")
conn.commit()
cur.execute("use acada")
conn.commit()

#creating tables
#1.empdata
#2.attendance data table

cur.execute('create table if not exists empdata(emp_token_id char(10),emp_id char(10),emp_name char(20),emp_email char(20),emp_dob char(11),emp_mno char(10),emp_joindate date,emp_pass char(10),emp_reset char(10))')
conn.commit()
#cur.execute('create table if not exists emplogindata(token_id char(10),emp_id char(10),emp_name char(20),emp_pass char(10),emp_reset char(15))')
#conn.commit()

cur.execute('create table if not exists empattendance(workdate date,day char(15),emp_id char(10),emp_name char(20),arrival char(20),departure char(20))')
conn.commit()
cur.execute('create table if not exists failedattempts(attempt_date date,emp_id char(20),emp_name char(20),time char(20))')
conn.commit()
#creating customer data table
cur.execute('create table if not exists cusdata(cus_id char(10),cus_name char(20),cus_pass char(15),cus_reset char(15))')
conn.commit()
#creating jobrequest table
cur.execute('create table if not exists cusjobs(job_id char(10),cus_id char(10),problem_name char(15),problem_time char(20),product_id char(10),cus_location char(20),distance char(5),cus_cno char(10),ass_emp_id char(10),job_status char(10),job_req_date date,emp_ass_date date)')
conn.commit()
cur.execute('create table if not exists empcusvisit(cus_id char(10),emp_id char(10),date_service date,arrival char(20),departure char(20))')
conn.commit()
cur.execute('create table if not exists jobtypes(job_name char(20),expected_time char(20))')
conn.commit()
cur.execute('create table if not exists empwork(emp_id char(20),no_jobs char(5),time char(5),jobs_done char(10))')
conn.commit()


master=Tk()
master.title("ACADA 2.0")
master.geometry('600x350')


welcometext=Text(master,height=2,width=70)
welcometext.grid(row=0,column=0,rowspan=3,columnspan=5,padx=20,pady=30)
welcometext.insert(END,'welcome to ACADA,There are three login options available Choose yours')


masterempbutton=Button(master,text="EMPLOYEE",command=employee)
masterempbutton.grid(row=4,column=0,padx=10,pady=30)


adminempbutton=Button(master,text="ADMIN",command=admin)
adminempbutton.grid(row=4,column=1,padx=10,pady=30)

customerempbutton=Button(master,text='CUSTOMER',command=customer)
customerempbutton.grid(row=4,column=2,padx=10,pady=30)



endingtext=Text(master,height=5,width=70)
endingtext.grid(row=5,column=0,rowspan=3,columnspan=5,padx=20,pady=10)
endingtext.insert(END,'To acess any of the portal you need to have ID & password\nFor first time logins\nEmployee->Register with Token id provided by admin on email \nCUSTOMER-> REGISTER WITH TOKEN ID ON BILL/SERVICE LETTER ')
master.grid_rowconfigure(5,minsize=50)

empregisterbutton=Button(master,text="EMPLOYEE REGISTER",command=empregister)
empregisterbutton.grid(row=8,column=4,padx=10,pady=10)
cusregisterbutton=Button(master,text="CUSTOMER REGISTER",command=cusregister)
cusregisterbutton.grid(row=8,column=1,padx=10,pady=10)







master.mainloop()


