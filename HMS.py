from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1400x800+0+0")  # Increased window size for better fit

        # Define variables
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        self.Booldp = StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System", fg="red", bg="white", font=("times new roman", 35, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        ########### for DATA Frame ##################

        Dataframe = Frame(self.root, bd=15, relief=RIDGE)
        Dataframe.place(x=0, y=100, width=1350, height=400)  # Increased width and height

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=900, height=370)  # Increased size for better visibility

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Prescription")
        DataframeRight.place(x=910, y=5, width=430, height=370)  # Adjusted size to fit within the window

        ############### Button Frame ##############
        Buttonframe = Frame(self.root, bd=15, relief=RIDGE)
        Buttonframe.place(x=0, y=510, width=1400, height=70)  # Increased button frame size

        ############### Details Frame ##############
        Detailsframe = Frame(self.root, bd=15, relief=RIDGE)
        Detailsframe.place(x=0, y=580, width=1400, height=220)  # Increased details frame

        # ============================DataframeLeft=========================
        # ===============Label for tablet==================
        lblNameTablet = Label(DataframeLeft, text="Names of Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNameTablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("arial", 12, "bold"), width=32)
        comNameTablet["values"] = (
            "Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan", "Fluticasone", "Insulin glargine",
            "Lisdexamfetamine", "Pregabalin", "Tiotropium", "Sitagliptin", "Levothyroxine", "Rosuvastatin", "Albuterol", "Nexium", "Naproxen", "Clonazepam", "Pantoprazole", "Prednisone")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        # ============Label for reference no.=================
        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        # ================Label for Dose=================
        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        # ==============Label for No of tablets===============
        lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, textvariable=self.NumberofTablets, font=("arial", 12, "bold"), width=35)
        txtNoOftablets.grid(row=3, column=1)

        # =============Label for Lot==================
        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, textvariable=self.Lot, font=("arial", 12, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        # ============Label for Issue Date=================
        lblissueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, textvariable=self.Issuedate, font=("arial", 12, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        # =============Label for Exp Date=================
        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, textvariable=self.ExpDate, font=("arial", 12, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        # ====================Daily Dose==================
        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, textvariable=self.DailyDose, font=("arial", 12, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        # ===================Side Effect==================
        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, textvariable=self.sideEfect, font=("arial", 12, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        # ===================Further Information=================
        lblFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Information", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, textvariable=self.FurtherInformation, font=("arial", 12, "bold"), width=35)
        txtFurtherinfo.grid(row=0, column=3)

        # ===================Blood Pressure=================
        lblBloodPressure = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPress = Entry(DataframeLeft, textvariable=self.Booldp, font=("arial", 12, "bold"), width=35)
        txtBloodPress.grid(row=1, column=3)

        # ===============Storage Advice==================
        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, textvariable=self.StorageAdvice, font=("arial", 12, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3)

        # ===================Driving Using Machine=================
        lblDriving = Label(DataframeLeft, font=("arial", 12, "bold"), text="Driving Using Machine", padx=2, pady=6)
        lblDriving.grid(row=4, column=2, sticky=W)
        txtDriving = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtDriving.grid(row=4, column=3)

        # ====================Patient ID==================
        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient ID", padx=2, pady=6)
        lblPatientId.grid(row=5, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=5, column=3)

        # ====================NHS Number==================
        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhsNumber.grid(row=6, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=6, column=3)

        # ====================Patient Name==================
        lblPatientName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientName.grid(row=7, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=7, column=3)

        # ====================Date of Birth==================
        lblDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=8, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=8, column=3)

        # ====================Patient Address==================
        lblPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=9, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=9, column=3)

        # ================== DataframeRight - Prescription Details ====================
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=15, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #===================Buttons====================================
        btnPrescription = Button(bd=5, relief=RIDGE, command=self.iPrectioption, text="Prescription", fg="black", bg="green", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnPrescription.place(x=11, y=540)

        btnPrescriptionData = Button(bd=5, command=self.iPrescriptionData, relief=RIDGE, text="Prescription Data", bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnPrescriptionData.place(x=227, y=540)

        btnUpdate = Button(bd=5, command=self.update_data, relief=RIDGE, text="Update", bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnUpdate.place(x=443, y=540)

        btnDelete = Button(bd=5, relief=RIDGE, command=self.idelete, text="Delete", bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnDelete.place(x=659, y=540)

        btnClear = Button(bd=5, relief=RIDGE, command=self.clear, text="Clear", bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnClear.place(x=875, y=540)

        btnExit = Button(bd=5, relief=RIDGE, command=self.iExit, text="Exit", bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnExit.place(x=1091, y=540)

        btnSearch = Button(bd=5, relief=RIDGE, text="Search", bg="green", fg="black", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=6)
        btnSearch.place(x=1307, y=540)

#===================Table with Scrollbars======================

        # Creating Scrollbars
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        
        # Creating Treeview (Table)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("Nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        # Adding Scrollbars to the Treeview
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # Defining Table Headings
        self.hospital_table.heading("Nameoftablets", text="Name of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        # Defining Column Widths
        self.hospital_table.column("Nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        # Displaying Table
        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        # Binding Event for Row Selection
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetching Data from the Database
        self.fetch_data()

        ############################function Declration#####################################


    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
              messagebox.showerror("Error","All field are reuired")
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="ilovesuga",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                     self.Nameoftablets.get(),
                                                                                                     self.ref.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.NumberofTablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.Issuedate.get(),
                                                                                                     self.ExpDate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get()
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")

                
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="ilovesuga",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update into hospital set Nameoftablets=%s,ref=%s,Dose=%s,NumberofTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,StorageAdvice=%s,nhsNumber=%s,PatientName=%s,DateOfBirth=%s,PatientAddress=%s",(
                                                                                                     self.Nameoftablets.get(),
                                                                                                     self.ref.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.NumberofTablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.Issuedate.get(),
                                                                                                     self.ExpDate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get()
                                                                                        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated")                                                                      


    def  fetch_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="ilovesuga",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select 8 from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                        self.hospital_table.insert("",END,values=i)
                conn.commit()
        conn.close()                

    def get_cursor(self,event=""):
            cursor_row=self.hospital_table.focus()
            content=self.hospital_table.item(cursor_row)
            row=content["values"]
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6]) 
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])

    def  iPrectioption(self):
          self.txtPrescription.insert(END,"Name of Tablets:-\t\t\t"+self.Nameoftablets.get()+"\n")
          self.txtPrescription.insert(END,"Reference number :-\t\t\t"+self.ref.get()+"\n") 
          self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")   
          self.txtPrescription.insert(END,"Number of tablets:-\t\t\t"+self.NumberofTablets.get()+"\n")  
          self.txtPrescription.insert(END,"LOT:-\t\t\t"+self.Lot.get()+"\n")
          self.txtPrescription.insert(END,"Issuedate:-\t\t\t"+self.Issuedate.get()+"\n")
          self.txtPrescription.insert(END,"ExpDate :\t\t\t"+self.ExpDate.get()+"\n") 
          self.txtPrescription.insert(END,"DailyDose:-\t\t\t"+self.DailyDose.get()+"\n")
          self.txtPrescription.insert(END,"Side effetcs:\t\t\t"+self.sideEfect.get()+"\n") 
          self.txtPrescription.insert(END,"Futher Information:\t\t\t"+self.FurtherInformation.get()+"\n")    
          self.txtPrescription.insert(END,"Storage Advice:-\t\t\t"+self.StorageAdvice.get()+"\n") 
          self.txtPrescription.insert(END,"DrivingUsingMachine :-\t\t\t"+self.DrivingUsingMachine.get()+"\n") 
          self.txtPrescription.insert(END," patient ID:-\t\t\t"+self.PatientId.get()+"\n")  
          self.txtPrescription.insert(END,"Nhs Number :-\t\t\t"+self.nhsNumber.get()+"\n")
          self.txtPrescription.insert(END,"patient Name  :-\t\t\t"+self.PatientName.get()+"\n")  
          self.txtPrescription.insert(END,"Date of Birth :-\t\t\t"+self.DateOfBirth.get()+"\n") 
          self.txtPrescription.insert(END,"PAtient  Address :-\t\t\t"+self.PatientAddress.get()+"\n") 
          


    def idelete(self):

          conn=mysql.connector.connect(host="localhost",username="root",password="ilovesuga",database="mydata")
          my_cursor=conn.cursor()
          query="delete from hospital where Reference_No=%s"
          value=(self.ref.get(),)
          my_cursor.execute(query,value)

          conn.commit()
          conn.close()

          self.fetch_data()
          messagebox.showinfo("Delete","patient has been delete succesfully")

    def clear(self):
            self.Nameoftablets.set("")
            self.ref.set("")
            self.Dose.set("")
            self.NumberofTablets.set("")
            self.Lot.set("")
            self.Issuedate.set("")
            self.ExpDate.set("") 
            self.DailyDose.set("")
            self.sideEfect.set("")
            self.FurtherInformation.set("")
            self.PatientId.set("")
            self.StorageAdvice.set("")
            self.nhsNumber.set("")
            self.PatientName.set("")
            self.DateOfBirth.set("")
            self.PatientAddress.set("")
            self.Booldp.set("")
            self.HowToUseMedication.set("")
            self.txtPrescription.delete("1.0",END)


    def iExit(self):
           iExit=messagebox.askyesno("Hospital management System","confire you want to exit")
           if iExit>0:
                   root.destroy()
                   return









if __name__ == "__main__":
    root = Tk()
    application = Hospital(root)
    root.mainloop()
