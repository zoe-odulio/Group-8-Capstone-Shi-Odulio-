from tkinter import *
from tkinter import ttk
import tkinter
root=Tk()
root.title('Debt Ledger')
frm = ttk.Frame(root, padding=20)
frm.grid()
#define submit commands

def adddebtincurred():
    adddebtincurred=adddebtincurred_entry.get()
#select person with existing debt
introlabel0=ttk.Label(frm, text="Check debt of person with existing debt")
introlabel0.grid(row=0,column=0,sticky=W)

def selectperson():
    selectedperson=ttk.Label(frm,text=selectedperson_var.get())
    selectedperson.grid(row=3,column=0,sticky=W,pady=2)

options1=['Niki','Jungwon','Sunoo']
selectedperson_var=StringVar()
selectedperson_var.set('Select Name')#default empty
#selectedperson_var.grid(column=0,row=2,sticky=W,pady=2)

drop1=OptionMenu(frm,selectedperson_var,*options1)
drop1.grid(column=0, row=1,sticky=W,pady=2)
submitselectperson=ttk.Button(frm,text='Submit',command=selectperson)
submitselectperson.grid(column=1,row=2,sticky=E,pady=2)

currentdebt=('current debt')

div0=ttk.Label(frm,text='----------------------------------------------------------------------------------------------------------')
div0.grid(column=0,row=4)
#add person with debt
def addpeople():
    addedperson=ttk.Label(frm,text=addedperson_entry.get())
    addedperson.grid(row=9,column=0,sticky=W,pady=2)
    debtfromnewppl=ttk.Label(frm,text=debtfromnewppl_entry.get())
    debtfromnewppl.grid(row=10,column=0,sticky=W,pady=2)


introlabel1=ttk.Label(frm, text="Adding New People")
introlabel1.grid(row=5,column=0,sticky=W,pady=2)
addingpeople_label = ttk.Label(frm, text="Name")
addingpeople_label.grid(row=6,column=0,sticky=W,pady=2)
addingpeople_var = StringVar()
addedperson_entry = ttk.Entry(frm, textvariable=addingpeople_var)
addedperson_entry.grid(column=1, row=6,sticky=E,pady=2)

debtfromnewppl_label = ttk.Label(frm, text="Amount")
debtfromnewppl_label.grid(row=7,column=0,sticky=W,pady=2)
debtfromnewppl_var = IntVar()
debtfromnewppl_entry= ttk.Entry(frm, textvariable=debtfromnewppl_var)
debtfromnewppl_entry.grid(column=1, row=7,sticky=E,pady=2)

addpplsubmit = ttk.Button(frm, text="Submit", command=addpeople)
addpplsubmit.grid(column=1, row=8,sticky=E,pady=2)

div1=ttk.Label(frm,text='----------------------------------------------------------------------------------------------------------')

div1.grid(column=0,row=11)
#receiving payment

introlabel2=ttk.Label(frm, text="Receiving Payment")
introlabel2.grid(row=12,column=0,sticky=W,pady=2)
def receivepayment():
   receivedpaymentppl=ttk.Label(frm,text=receivepaymentppl_var.get())
   receivedpaymentppl.grid(row=16,column=0,sticky=W,pady=2)
   receivedpayment=ttk.Label(frm,text=paymentreceived_entry.get())
   receivedpayment.grid(row=17,column=0,sticky=W,pady=2)

options2=['Niki','Jungwon','Sunoo']
receivepaymentppl_var=StringVar()
receivepaymentppl_var.set('Select Name')

drop2=OptionMenu(frm,receivepaymentppl_var,*options2)
drop2.grid(column=0, row=13,sticky=W,pady=2)


receivedpayment_label = ttk.Label(frm, text="Amount")
receivedpayment_label.grid(row=14,column=0,sticky=W,pady=2)
paymentreceived_var = IntVar()
paymentreceived_entry= ttk.Entry(frm, textvariable=paymentreceived_var)
paymentreceived_entry.grid(column=1, row=14,sticky=E,pady=2)

submitreceivepayment=ttk.Button(frm,text='Submit',command=receivepayment)
submitreceivepayment.grid(column=1,row=15,sticky=E,pady=2)
div1=ttk.Label(frm,text='----------------------------------------------------------------------------------------------------------')

div1.grid(column=0,row=18)
#incurring more debt
introlabel3=ttk.Label(frm, text="Receiving Payment")
introlabel3.grid(row=19,column=0,sticky=W,pady=2)
def adddebtincurred():
   adddebtname=ttk.Label(frm,text=adddebtname_var.get())
   adddebtname.grid(row=23,column=0,sticky=W,pady=2)
   addboramnt=ttk.Label(frm,text=addboramnt_entry.get())
   addboramnt.grid(row=24,column=0,sticky=W,pady=2)

options3=['Niki','Jungwon','Sunoo']
adddebtname_var=StringVar()
adddebtname_var.set('Select Name')

drop3=OptionMenu(frm,adddebtname_var,*options3)
drop3.grid(column=0, row=20,sticky=W,pady=2)


addboramnt_label = ttk.Label(frm, text="Amount")
addboramnt_label.grid(row=21,column=0,sticky=W,pady=2)
addboramnt_var = IntVar()
addboramnt_entry= ttk.Entry(frm, textvariable=addboramnt_var)
addboramnt_entry.grid(column=1, row=21,sticky=E,pady=2)

submitadddebt=ttk.Button(frm,text='Submit',command=adddebtincurred)
submitadddebt.grid(column=1,row=22,sticky=E,pady=2)

div1=ttk.Label(frm,text='----------------------------------------------------------------------------')
div1.grid(column=0,row=25)
introlabel4=ttk.Label(frm, text="Table of People with Debt")
introlabel4.grid(row=26,column=0,sticky=W,pady=2) #problem is that since table has an artbitary number of rows,  the line will not be accurate
class Table:
     
    def __init__(self,frm):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(frm)
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Lia',19),
       (2,'Yuna',18),
       (3,'Chaeryoung',20),
       (4,'Yeji',21),
       (5,'Ryujin',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window

currentdebt_table=Table(frm)

div1=ttk.Label(frm,text='----------------------------------------------------------------------------')
div1.grid(column=0,row=32)
introlabel4=ttk.Label(frm, text="Table of Payment Received")
introlabel4.grid(row=33,column=0,sticky=W,pady=2) #problem is that since table has an artbitary number of rows,  the line will not be accurate
class Table:
     
    def __init__(self,frm):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(frm)
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Lia',19),
       (2,'Yuna',18),
       (3,'Chaeryoung',20),
       (4,'Yeji',21),
       (5,'Ryujin',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
paymentreceived_table=Table(frm)
div1=ttk.Label(frm,text='----------------------------------------------------------------------------')
div1.grid(column=0,row=39)
introlabel4=ttk.Label(frm, text="Table of Additional Debt Incurred")
introlabel4.grid(row=40,column=0,sticky=W,pady=2) #problem is that since table has an artbitary number of rows,  the line will not be accurate
class Table:
     
    def __init__(self,frm):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(frm)
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Lia',19),
       (2,'Yuna',18),
       (3,'Chaeryoung',20),
       (4,'Yeji',21),
       (5,'Ryujin',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
adddebtincurred_table=Table(frm)
root.mainloop()