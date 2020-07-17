import tkinter as tk
import mysql.connector as mysql
import os
import smtplib
import datetime

class Admin_Islemleri(object):
    def __init__(self):
        self.Admin_Screen=tk.Toplevel(root)
        self.Admin_Screen.title("YÖNETİCİ İŞLEMLERİ EKRANI")
        self.Admin_Screen.geometry("1050x250")
        self.Admin_Screen.transient(root)

        self.YeniKitap=tk.Button(self.Admin_Screen,text="Yeni Kitap Ekle",\
                       bg="pink",command=self.YeniKitapEkle,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.YeniKitap.grid(row=0,column=0)
        
        self.KitapSil=tk.Button(self.Admin_Screen,text="Kitap Sil",\
                       bg="pink",command=self.KitapSil,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.KitapSil.grid(row=0,column=1)
        
        self.YeniUye=tk.Button(self.Admin_Screen,text="Yeni Üye Ekle",\
                       bg="pink",command=self.YeniUyeEkle,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.YeniUye.grid(row=1,column=0)
        
        self.UyeSil=tk.Button(self.Admin_Screen,text="Üyelikten Düşür",\
                       bg="pink",command=self.UyeSil,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.UyeSil.grid(row=1,column=1)
        
        self.KitapAra=tk.Button(self.Admin_Screen,text="Kitap Arama",\
                       bg="pink",command=self.KitapArama,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.KitapAra.grid(row=2,column=0)
        
        self.UyeAra=tk.Button(self.Admin_Screen,text="Üye Arama",\
                       bg="pink",command=self.UyeArama,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.UyeAra.grid(row=2,column=1)
    
    def YKitapKayit(self):        
        BOOK_ID=self.YKBIDVar.get()
        ISBN=self.YKISBNVar.get()
        Author=self.YKAuthVar.get()
        Title=self.YKTitleVar.get()
        Subject=self.YKSubjVar.get()
        Pub_Year=self.YKPubYearVar.get()
        Publisher=self.YKPubCompVar.get()
        Edition=self.YKEditionVar.get()
        Lang=self.YKLangVar.get()
        Shelf_ID=self.YKShelfIDVar.get()
        Cov_IMG=self.YKCovIMGVar.get()
        Pub_Loc=self.YKPubLocVar.get()
        
        Values=(BOOK_ID,ISBN,Author,Title,Subject,Pub_Year,Publisher,Edition,Lang,Shelf_ID,Cov_IMG,Pub_Loc)
        sql="Insert into BOOKS_TBL(BOOK_ID,ISBN,Author,Title,Subject,Pub_Year,\
        Publisher,Edition,Lang,Shelf_ID,Cov_IMG,Pub_Loc) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(sql,Values)
        db.commit()                

    def YKitapGiris(self):
        self.YKBIDVar.set(0)
        self.YKISBNVar.set("")
        self.YKAuthVar.set("")
        self.YKTitleVar.set("")
        self.YKSubjVar.set("")
        self.YKPubYearVar.set(0)
        self.YKPubCompVar.set("")
        self.YKEditionVar.set("")
        self.YKLangVar.set("")
        self.YKShelfIDVar.set("")
        self.YKCovIMGVar.set("")
        self.YKPubLocVar.set("")
    
    def YKitapKapat(self):
        self.YeniKitapEkrani.destroy()
    def YeniKitapEkle(self):
        self.YeniKitapEkrani=tk.Toplevel(self.Admin_Screen)        
        self.YeniKitapEkrani.title("YENİ KİTAP EKLEME İŞLEMLERİ EKRANI")
        self.YeniKitapEkrani.geometry("500x450")
        self.YeniKitapEkrani.transient(self.Admin_Screen)
        
        self.YKInputFrame=tk.Frame(self.YeniKitapEkrani)
        self.YKInputFrame.grid(row=0,column=0)
        self.YKButtonFrame=tk.Frame(self.YeniKitapEkrani)
        self.YKButtonFrame.grid(row=1,column=0)
        
        self.YKBIDVar=tk.IntVar()
        self.YKBID=tk.Label(self.YKInputFrame,text="Yeni Kitap ID",\
                           width=20)
        self.YKBID.grid(row=0,column=0,sticky='nw')
        self.YKitapIDGiris=tk.Entry(self.YKInputFrame,width=50,\
                                    textvariable=self.YKBIDVar)
        self.YKitapIDGiris.grid(row=0,column=1)
        
        self.YKISBNVar=tk.StringVar()
        self.YKISBN=tk.Label(self.YKInputFrame,text="Yeni Kitap ISBN",\
                             width=20)
        self.YKISBN.grid(row=1,column=0,sticky='nw')
        self.YKitapISBNGiris=tk.Entry(self.YKInputFrame,width=50,\
                                      textvariable=self.YKISBNVar)
        self.YKitapISBNGiris.grid(row=1,column=1)
        
        self.YKAuthVar=tk.StringVar()
        self.YKAuth=tk.Label(self.YKInputFrame,text="Yeni Kitap Author",\
                             width=20)
        self.YKAuth.grid(row=2,column=0,sticky='nw')
        self.YKitapAuthGiris=tk.Entry(self.YKInputFrame,width=50,\
                                      textvariable=self.YKAuthVar)
        self.YKitapAuthGiris.grid(row=2,column=1)
        
        self.YKTitleVar=tk.StringVar()
        self.YKTitle=tk.Label(self.YKInputFrame,text="Yeni Kitap Title",\
                              width=20)
        self.YKTitle.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapTitleGiris=tk.Entry(self.YKInputFrame,width=50,\
                                       textvariable=self.YKTitleVar)
        self.YKitapTitleGiris.grid(row=3,column=1)
        
        self.YKSubjVar=tk.StringVar()
        self.YKSubj=tk.Label(self.YKInputFrame,text="Yeni Kitap Subject",\
                             width=20)
        self.YKSubj.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapSubjGiris=tk.Entry(self.YKInputFrame,width=50,\
                                      textvariable=self.YKSubjVar)
        self.YKitapSubjGiris.grid(row=4,column=1)
        
        self.YKPubYearVar=tk.IntVar()
        self.YKPubYear=tk.Label(self.YKInputFrame,text="Yeni Kitap Pub. Year",\
                                width=20)
        self.YKPubYear.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapPubYearGiris=tk.Entry(self.YKInputFrame,width=50,\
                                     textvariable=self.YKPubYearVar)
        self.YKitapPubYearGiris.grid(row=5,column=1)
        
        self.YKPubCompVar=tk.StringVar()
        self.YKPubComp=tk.Label(self.YKInputFrame,text="Yeni Kitap Publisher",\
                                width=20)
        self.YKPubComp.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapPubCompGiris=tk.Entry(self.YKInputFrame,width=50,\
                                         textvariable=self.YKPubCompVar)
        self.YKitapPubCompGiris.grid(row=6,column=1)
        
        self.YKEditionVar=tk.StringVar()
        self.YKEdition=tk.Label(self.YKInputFrame,text="Yeni Kitap Edition",\
                                width=20)
        self.YKEdition.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapEditionGiris=tk.Entry(self.YKInputFrame,width=50,\
                                         textvariable=self.YKEditionVar)
        self.YKitapEditionGiris.grid(row=7,column=1)
        
        self.YKLangVar=tk.StringVar()
        self.YKLang=tk.Label(self.YKInputFrame,text="Yeni Kitap Language",\
                             width=20)
        self.YKLang.grid(row=8,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapLangGiris=tk.Entry(self.YKInputFrame,width=50,\
                                      textvariable=self.YKLangVar)
        self.YKitapLangGiris.grid(row=8,column=1)
        
        self.YKShelfIDVar=tk.StringVar()
        self.YKShelfID=tk.Label(self.YKInputFrame,text="Yeni Kitap Shelf ID",\
                                width=20)
        self.YKShelfID.grid(row=9,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapShelfIDGiris=tk.Entry(self.YKInputFrame,width=50,\
                                      textvariable=self.YKShelfIDVar)
        self.YKitapShelfIDGiris.grid(row=9,column=1)
        
        self.YKCovIMGVar=tk.StringVar()
        self.YKCovIMG=tk.Label(self.YKInputFrame,text="Yeni Kitap Cov. IMG",\
                               width=20)
        self.YKCovIMG.grid(row=10,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapCovIMGGiris=tk.Entry(self.YKInputFrame,width=50,\
                                      textvariable=self.YKCovIMGVar)
        self.YKitapCovIMGGiris.grid(row=10,column=1)
        
        self.YKPubLocVar=tk.StringVar()
        self.YKPubLoc=tk.Label(self.YKInputFrame,text="Yeni Kitap Pub. Location",\
                               width=20)
        self.YKPubLoc.grid(row=11,column=0,padx=3,pady=3,sticky="nw")
        self.YKitapPubLocGiris=tk.Entry(self.YKInputFrame,width=50,\
                                       textvariable=self.YKPubLocVar)
        self.YKitapPubLocGiris.grid(row=11,column=1)
        
        self.YKKayit=tk.Button(self.YKButtonFrame,text="Yeni Kitap Kaydet",\
                       bg="lightgreen",command=self.YKitapKayit,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YKKayit.grid(row=0,column=0)
        
        self.YKYeniGiris=tk.Button(self.YKButtonFrame,text="Yeni Kitap Giriş",\
                       bg="lightgreen",command=self.YKitapGiris,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YKYeniGiris.grid(row=0,column=1)
        
        self.YKCikis=tk.Button(self.YKButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.YKitapKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YKCikis.grid(row=0,column=2)
        
    def KitabiListele(self):
        global KSBOOK_ID
        KSBOOK_ID=self.KSilIDVar.get()
        sql="SELECT * FROM BOOKS_TBL WHERE BOOK_ID= %s"
        mycursor.execute(sql,(KSBOOK_ID,))
        row=mycursor.fetchall()
        self.KSilISBNGiris.state="enabled"
        self.KSilISBNVar.set(row[0][1])
        self.KSilAuthGiris.state="enabled"
        self.KSilAuthVar.set(row[0][2])
        self.KSilTitleGiris.state="enabled"
        self.KSilTitleVar.set(row[0][3])
        self.KSilSubjGiris.state="enabled"
        self.KSilSubjVar.set(row[0][4])
        self.KSilPubYearGiris.state="enabled"
        self.KSilPubYearVar.set(row[0][5])
        
        self.KSilPubCompGiris.state="enabled"
        self.KSilPubCompVar.set(row[0][6])
        self.KSilEditionGiris.state="enabled"
        self.KSilEditionVar.set(row[0][7])
        self.KSilLangGiris.state="enabled"
        self.KSilLangVar.set(row[0][8])
        self.KSilShelfIDGiris.state="enabled"
        self.KSilShelfIDVar.set(row[0][9])
        
        self.KSilCovIMGGiris.state="enabled"
        self.KSilCovIMGVar.set(row[0][10])
        self.KSilPubLocGiris.state="enabled"
        self.KSilPubLocVar.set(row[0][11])
        
        self.KSilSor.config(state="normal")        
        
    def KitapSilTrue(self):
        sql="DELETE FROM BOOKS_TBL WHERE BOOK_ID= %s"
        mycursor.execute(sql,(KSBOOK_ID,))
        db.commit()
        
        self.Karar_Kontrol_Ekrani.destroy()
        
    def KitapSilFalse(self):
        self.Karar_Kontrol_Ekrani.destroy()   
        
    def KitapSilKontrol(self):                  
        self.Karar_Kontrol_Ekrani = tk.Toplevel(self.KitapSilEkrani)
        self.Karar_Kontrol_Ekrani.title("Kitap Silme İşlemi İçin")
        self.Karar_Kontrol_Ekrani.geometry("250x100")
        tk.Label(self.Karar_Kontrol_Ekrani, text="Eminmisiniz?").pack()
        tk.Button(self.Karar_Kontrol_Ekrani, text="EVET",command=self.KitapSilTrue).pack()
        tk.Button(self.Karar_Kontrol_Ekrani, text="HAYIR",command=self.KitapSilFalse).pack()        
        
    def KSilCikis(self):
        self.KitapSilEkrani.destroy()
        
    def KitapSil(self):
        self.KitapSilEkrani=tk.Toplevel(self.Admin_Screen)        
        self.KitapSilEkrani.title("KİTAP SİLME İŞLEMLERİ EKRANI")
        self.KitapSilEkrani.geometry("500x450")
        self.KitapSilEkrani.transient(self.Admin_Screen)
        
        self.KSilInputFrame=tk.Frame(self.KitapSilEkrani)
        self.KSilInputFrame.grid(row=0,column=0)
        self.KSilButtonFrame=tk.Frame(self.KitapSilEkrani)
        self.KSilButtonFrame.grid(row=1,column=0)
        
        self.KSilIDVar=tk.IntVar()
        self.KSilID=tk.Label(self.KSilInputFrame,text="Kitap ID",\
                           width=20)
        self.KSilID.grid(row=0,column=0,sticky='nw')
        self.KSilIDGiris=tk.Entry(self.KSilInputFrame,width=50,\
                                    textvariable=self.KSilIDVar)
        self.KSilIDGiris.grid(row=0,column=1)
        
        self.KSilISBNVar=tk.StringVar()
        self.KSilISBN=tk.Label(self.KSilInputFrame,text="Kitap ISBN",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilISBN.grid(row=1,column=0,sticky='nw')
        self.KSilISBNGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilISBNVar,state='disabled')
        self.KSilISBNGiris.grid(row=1,column=1)
        
        self.KSilAuthVar=tk.StringVar()
        self.KSilAuth=tk.Label(self.KSilInputFrame,text="Kitap Author",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilAuth.grid(row=2,column=0,sticky='nw')
        self.KSilAuthGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilAuthVar,state='disabled')
        self.KSilAuthGiris.grid(row=2,column=1)
        
        self.KSilTitleVar=tk.StringVar()
        self.KSilTitle=tk.Label(self.KSilInputFrame,text="Kitap Title",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilTitle.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.KSilTitleGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilTitleVar,state='disabled')
        self.KSilTitleGiris.grid(row=3,column=1)
        
        self.KSilSubjVar=tk.StringVar()
        self.KSilSubj=tk.Label(self.KSilInputFrame,text="Kitap Subject",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilSubj.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.KSilSubjGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilSubjVar,state='disabled')
        self.KSilSubjGiris.grid(row=4,column=1)
        
        self.KSilPubYearVar=tk.IntVar()
        self.KSilPubYear=tk.Label(self.KSilInputFrame,text="Kitap Pub. Year",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilPubYear.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.KSilPubYearGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilPubYearVar,state='disabled')
        self.KSilPubYearGiris.grid(row=5,column=1)
        
        self.KSilPubCompVar=tk.StringVar()
        self.KSilPubComp=tk.Label(self.KSilInputFrame,text="Kitap Publisher",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilPubComp.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.KSilPubCompGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilPubCompVar,state='disabled')
        self.KSilPubCompGiris.grid(row=6,column=1)
        
        self.KSilEditionVar=tk.StringVar()
        self.KSilEdition=tk.Label(self.KSilInputFrame,text="Kitap Edition",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilEdition.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.KSilEditionGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilEditionVar,state='disabled')
        self.KSilEditionGiris.grid(row=7,column=1)
        
        self.KSilLangVar=tk.StringVar()
        self.KSilLang=tk.Label(self.KSilInputFrame,text="Kitap Language",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilLang.grid(row=8,column=0,padx=3,pady=3,sticky="nw")
        self.KSilLangGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilLangVar,state='disabled')
        self.KSilLangGiris.grid(row=8,column=1)
        
        self.KSilShelfIDVar=tk.StringVar()
        self.KSilShelfID=tk.Label(self.KSilInputFrame,text="Kitap Shelf ID",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilShelfID.grid(row=9,column=0,padx=3,pady=3,sticky="nw")
        self.KSilShelfIDGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilShelfIDVar,state='disabled')
        self.KSilShelfIDGiris.grid(row=9,column=1)
        
        self.KSilCovIMGVar=tk.StringVar()
        self.KSilCovIMG=tk.Label(self.KSilInputFrame,text="Kitap Cov. IMG",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilCovIMG.grid(row=10,column=0,padx=3,pady=3,sticky="nw")
        self.KSilCovIMGGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilCovIMGVar,state='disabled')
        self.KSilCovIMGGiris.grid(row=10,column=1)
        
        self.KSilPubLocVar=tk.StringVar()
        self.KSilPubLoc=tk.Label(self.KSilInputFrame,text="Kitap Pub. Location",\
                    width=20,state='disabled',disabledforeground="gray")
        self.KSilPubLoc.grid(row=11,column=0,padx=3,pady=3,sticky="nw")
        self.KSilPubLocGiris=tk.Entry(self.KSilInputFrame,width=50,\
                    textvariable=self.KSilPubLocVar,state='disabled')
        self.KSilPubLocGiris.grid(row=11,column=1)
        
        self.KSilListele=tk.Button(self.KSilButtonFrame,text="Kitabı Listele",\
                       bg="lightgreen",command=self.KitabiListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KSilListele.grid(row=0,column=0)
        
        self.KSilSor=tk.Button(self.KSilButtonFrame,text="Kitabı Sil",\
                       bg="lightgreen",command=self.KitapSilKontrol,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'),state="disabled")        
        self.KSilSor.grid(row=0,column=1)
        
        self.KSilCikis=tk.Button(self.KSilButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.KSilCikis,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KSilCikis.grid(row=0,column=2)
    
    def YeniUyeKayit(self):        
        MEMBER_ID=self.UserIDVar.get()
        M_NAME=self.UserNameVar.get()
        M_SURNAME=self.UserSurnameVar.get()
        B_DATE=self.UserBirthDateVar.get()
        B_PLACE=self.UserBirthPlaceVar.get()
        ADRESS=self.UserAddressVar.get()
        E_MAIL=self.UserEMailVar.get()
        TEL_NO=self.UserTelNoVar.get()
                
        Values=(MEMBER_ID,M_NAME,M_SURNAME,B_DATE,B_PLACE,ADRESS,E_MAIL,TEL_NO)
        sql="Insert into MEMBERS_TBL(MEMBER_ID,M_NAME,M_SURNAME,B_DATE,B_PLACE,ADRESS,\
        E_MAIL,TEL_NO) \
        values(%s,%s,%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(sql,Values)
        db.commit()                
        
    def YUyeGiris(self):
        self.UserIDVar.set(0)
        self.UserNameVar.set("")
        self.UserSurnameVar.set("")
        self.UserBirthDateVar.set("")
        self.UserBirthPlaceVar.set("")
        self.UserAddressVar.set("")
        self.UserEMailVar.set("")
        self.UserTelNoVar.set("")        
    
    def YUyeKapat(self):
        self.YeniUyeEkrani.destroy()
    def YeniUyeEkle(self):        
        self.YeniUyeEkrani=tk.Toplevel(self.Admin_Screen)        
        self.YeniUyeEkrani.title("YENİ ÜYE EKLEME İŞLEMLERİ EKRANI")
        self.YeniUyeEkrani.geometry("500x450")
        self.YeniUyeEkrani.transient(self.Admin_Screen)
        
        self.YUInputFrame=tk.Frame(self.YeniUyeEkrani)
        self.YUInputFrame.grid(row=0,column=0)
        self.YUButtonFrame=tk.Frame(self.YeniUyeEkrani)
        self.YUButtonFrame.grid(row=1,column=0)
        
        self.UserIDVar=tk.IntVar()
        self.YUID=tk.Label(self.YUInputFrame,text="Yeni Üye ID",\
                           width=20)
        self.YUID.grid(row=0,column=0,sticky='nw')
        self.YUIDGiris=tk.Entry(self.YUInputFrame,width=50,\
                                    textvariable=self.UserIDVar)
        self.YUIDGiris.grid(row=0,column=1)
        
        self.UserNameVar=tk.StringVar()
        self.YUName=tk.Label(self.YUInputFrame,text="Yeni Üye İsim",\
                             width=20)
        self.YUName.grid(row=1,column=0,sticky='nw')
        self.YUNameGiris=tk.Entry(self.YUInputFrame,width=50,\
                                      textvariable=self.UserNameVar)
        self.YUNameGiris.grid(row=1,column=1)
        
        self.UserSurnameVar=tk.StringVar()
        self.YUSurname=tk.Label(self.YUInputFrame,text="Yeni Üye Soyadı",\
                             width=20)
        self.YUSurname.grid(row=2,column=0,sticky='nw')
        self.YUSurnameGiris=tk.Entry(self.YUInputFrame,width=50,\
                                      textvariable=self.UserSurnameVar)
        self.YUSurnameGiris.grid(row=2,column=1)
        
        self.UserBirthDateVar=tk.StringVar()
        self.YUBirthDate=tk.Label(self.YUInputFrame,text="Yeni Doğum Tarihi",\
                              width=20)
        self.YUBirthDate.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.YUBirthDateGiris=tk.Entry(self.YUInputFrame,width=50,\
                                       textvariable=self.UserBirthDateVar)
        self.YUBirthDateGiris.grid(row=3,column=1)
        
        self.UserBirthPlaceVar=tk.StringVar()
        self.YUBirthPlace=tk.Label(self.YUInputFrame,text="Yeni Üye Doğum Yeri",\
                             width=20)
        self.YUBirthPlace.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.YUBirthPlaceGiris=tk.Entry(self.YUInputFrame,width=50,\
                                      textvariable=self.UserBirthPlaceVar)
        self.YUBirthPlaceGiris.grid(row=4,column=1)
        
        self.UserAddressVar=tk.StringVar()
        self.YUAddress=tk.Label(self.YUInputFrame,text="Yeni Üye Adres",\
                                width=20)
        self.YUAddress.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.YUAddressGiris=tk.Entry(self.YUInputFrame,width=50,\
                                     textvariable=self.UserAddressVar)
        self.YUAddressGiris.grid(row=5,column=1)
        
        self.UserEMailVar=tk.StringVar()
        self.YUEMail=tk.Label(self.YUInputFrame,text="Yeni Üye E_Posta Adresi",\
                                width=20)
        self.YUEMail.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.YUEMailGiris=tk.Entry(self.YUInputFrame,width=50,\
                                         textvariable=self.UserEMailVar)
        self.YUEMailGiris.grid(row=6,column=1)
        
        self.UserTelNoVar=tk.StringVar()
        self.YUTelNo=tk.Label(self.YUInputFrame,text="Yeni Üye Tel. No.",\
                                width=20)
        self.YUTelNo.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.YUTelNoGiris=tk.Entry(self.YUInputFrame,width=50,\
                                         textvariable=self.UserTelNoVar)
        self.YUTelNoGiris.grid(row=7,column=1)
        
        
        self.YUKayit=tk.Button(self.YUButtonFrame,text="Yeni Üye Kaydet",\
                       bg="lightgreen",command=self.YeniUyeKayit,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YUKayit.grid(row=0,column=0)
        
        self.YUYeniGiris=tk.Button(self.YUButtonFrame,text="Yeni Üye Giriş",\
                       bg="lightgreen",command=self.YUyeGiris,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YUYeniGiris.grid(row=0,column=1)
        
        self.YUCikis=tk.Button(self.YUButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.YUyeKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YUCikis.grid(row=0,column=2)
        
    
    def UyeyiListele(self):
        global USMEMBER_ID
        USMEMBER_ID=self.USilIDVar.get()
        
        sql="SELECT * FROM MEMBERS_TBL WHERE MEMBER_ID= %s"
        mycursor.execute(sql,(USMEMBER_ID,))
        row=mycursor.fetchall()
        self.USilNameGiris.state="enabled"
        self.USilNameVar.set(row[0][1])
        self.USilSurnameGiris.state="enabled"
        self.USilSurnameVar.set(row[0][2])
        self.USilBirthDateGiris.state="enabled"
        self.USilBirthDateVar.set(row[0][3])
        self.USilBirthPlaceGiris.state="enabled"
        self.USilBirthPlaceVar.set(row[0][4])
        self.USilAddressGiris.state="enabled"
        self.USilAddressVar.set(row[0][5])
        
        self.USilEMailGiris.state="enabled"
        self.USilEMailVar.set(row[0][6])
        self.USilTelNoGiris.state="enabled"
        self.USilTelNoVar.set(row[0][7])
                              
        self.USilSor.config(state="normal")        
        
    def UyeyiSilTrue(self):
        sql="DELETE FROM MEMBERS_TBL WHERE MEMBER_ID= %s"
        mycursor.execute(sql,(USMEMBER_ID,))
        db.commit()
        
        self.UyeSilKararKontrol_Ekrani.destroy()
        
    def UyeyiSilFalse(self):
        self.UyeSilKararKontrol_Ekrani.destroy()   
        
    def UyeyiSilKontrol(self):                  
        self.UyeSilKararKontrol_Ekrani = tk.Toplevel(self.UyeSilEkrani)
        self.UyeSilKararKontrol_Ekrani.title("Üye Silme İşlemi İçin")
        self.UyeSilKararKontrol_Ekrani.geometry("250x100")
        tk.Label(self.UyeSilKararKontrol_Ekrani, text="Eminmisiniz?").pack()
        tk.Button(self.UyeSilKararKontrol_Ekrani, text="EVET",command=self.UyeyiSilTrue).pack()
        tk.Button(self.UyeSilKararKontrol_Ekrani, text="HAYIR",command=self.UyeyiSilFalse).pack()        
        
    def UyeyiSilCikis(self):
        self.UyeSilEkrani.destroy()
        
    def UyeSil(self):
        self.UyeSilEkrani=tk.Toplevel(self.Admin_Screen)        
        self.UyeSilEkrani.title("ÜYE SİLME İŞLEMLERİ EKRANI")
        self.UyeSilEkrani.geometry("500x450")
        self.UyeSilEkrani.transient(self.Admin_Screen)
        
        self.USilInputFrame=tk.Frame(self.UyeSilEkrani)
        self.USilInputFrame.grid(row=0,column=0)
        self.USilButtonFrame=tk.Frame(self.UyeSilEkrani)
        self.USilButtonFrame.grid(row=1,column=0)
        
        self.USilIDVar=tk.IntVar()
        self.USilID=tk.Label(self.USilInputFrame,text="Üye ID",\
                           width=20)
        self.USilID.grid(row=0,column=0,sticky='nw')
        self.USilIDGiris=tk.Entry(self.USilInputFrame,width=50,\
                                    textvariable=self.USilIDVar)
        self.USilIDGiris.grid(row=0,column=1)
        
        self.USilNameVar=tk.StringVar()
        self.USilName=tk.Label(self.USilInputFrame,text="Üye Adı",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilName.grid(row=1,column=0,sticky='nw')
        self.USilNameGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilNameVar,state='disabled')
        self.USilNameGiris.grid(row=1,column=1)
        
        self.USilSurnameVar=tk.StringVar()
        self.USilSurname=tk.Label(self.USilInputFrame,text="Üye Soyadı",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilSurname.grid(row=2,column=0,sticky='nw')
        self.USilSurnameGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilSurnameVar,state='disabled')
        self.USilSurnameGiris.grid(row=2,column=1)
        
        self.USilBirthDateVar=tk.StringVar()
        self.USilBirthDate=tk.Label(self.USilInputFrame,text="Üye Doğum Tarihi",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilBirthDate.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.USilBirthDateGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilBirthDateVar,state='disabled')
        self.USilBirthDateGiris.grid(row=3,column=1)
        
        self.USilBirthPlaceVar=tk.StringVar()
        self.USilBirthPlace=tk.Label(self.USilInputFrame,text="Üye Doğum Yeri",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilBirthPlace.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.USilBirthPlaceGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilBirthPlaceVar,state='disabled')
        self.USilBirthPlaceGiris.grid(row=4,column=1)
        
        self.USilAddressVar=tk.StringVar()
        self.USilAddress=tk.Label(self.USilInputFrame,text="Üye Adres",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilAddress.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.USilAddressGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilAddressVar,state='disabled')
        self.USilAddressGiris.grid(row=5,column=1)
        
        self.USilEMailVar=tk.StringVar()
        self.USilEMail=tk.Label(self.USilInputFrame,text="Üye E-Posta Adresi",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilEMail.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.USilEMailGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilEMailVar,state='disabled')
        self.USilEMailGiris.grid(row=6,column=1)
        
        self.USilTelNoVar=tk.StringVar()
        self.USilTelNo=tk.Label(self.USilInputFrame,text="Üye Tel. No.",\
                    width=20,state='disabled',disabledforeground="gray")
        self.USilTelNo.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.USilTelNoGiris=tk.Entry(self.USilInputFrame,width=50,\
                    textvariable=self.USilTelNoVar,state='disabled')
        self.USilTelNoGiris.grid(row=7,column=1)                                
        
        self.USilListele=tk.Button(self.USilButtonFrame,text="Üyeyi Listele",\
                       bg="lightgreen",command=self.UyeyiListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.USilListele.grid(row=0,column=0)
        
        self.USilSor=tk.Button(self.USilButtonFrame,text="Üyeyi Sil",\
                       bg="lightgreen",command=self.UyeyiSilKontrol,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'),state="disabled")        
        self.USilSor.grid(row=0,column=1)
        
        self.USilCikis=tk.Button(self.USilButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.UyeyiSilCikis,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.USilCikis.grid(row=0,column=2)
    
    def KitapAraListele(self):
        KAID=self.KAIDVar.get()
        KAISBN=self.KAISBNVar.get()
        KAAuth=self.KAAuthVar.get()
        KATitle=self.KATitleVar.get()
        KASubj=self.KASubjVar.get()
        KAPubYear=self.KAPubYearVar.get()
        KAPubComp=self.KAPubCompVar.get()
        KAEdition=self.KAEditionVar.get()
        KALang=self.KALangVar.get()
        KAShelfID=self.KAShelfIDVar.get()
        KAPubLoc=self.KAPubLocVar.get()
        
        Values=()
        Cond_Check=False # Check if a condition is aready added
        sql="SELECT * FROM BOOKS_TBL WHERE"
        if KAID!=0:
            sql=sql+" BOOK_ID=%s "
            Values=Values+(KAID,)
            Cond_Check=True
        if KAISBN!='':
            if Cond_Check==True:
                sql=sql+" AND ISBN=%s "
            else:
                sql=sql+" ISBN=%s "
                Cond_Check=True
            Values+=(KAISBN,)
        if KAAuth!='':
            if Cond_Check==True:
                sql=sql+" AND AUTHOR=%s "
            else:
                sql=sql+" AUTHOR=%s "
                Cond_Check=True
            Values+=(KAAuth,)
        if KATitle!='':
            if Cond_Check==True:
                sql=sql+" AND TITLE=%s "
            else:
                sql=sql+" TITLE=%s "
                Cond_Check=True
            Values+=(KATitle,)
        if KASubj!='':
            if Cond_Check==True:
                sql=sql+" AND SUBJECT=%s "
            else:
                sql=sql+" SUBJECT=%s "
                Cond_Check=True
            Values+=(KASubj,)
        if KAPubYear!=0:
            if Cond_Check==True:
                sql=sql+" AND PUB_YEAR=%s "
            else:
                sql=sql+" PUB_YEAR=%s "
                Cond_Check=True
            Values+=(KAPubYear,)
        if KAPubComp!='':
            if Cond_Check==True:
                sql=sql+" AND PUBLISHER=%s "
            else:
                sql=sql+" PUBLISHER=%s "
                Cond_Check=True
            Values+=(KAPubComp,)
        if KAEdition!='':
            if Cond_Check==True:
                sql=sql+" AND EDITION=%s "
            else:
                sql=sql+" EDITION=%s "
                Cond_Check=True
            Values+=(KAEdition,)
        if KALang!='':
            if Cond_Check==True:
                sql=sql+" AND LANG=%s "
            else:
                sql=sql+" LANG=%s "
                Cond_Check=True
            Values+=(KALang,)
        if KAShelfID!='':
            if Cond_Check==True:
                sql=sql+" AND SHELF_ID=%s "
            else:
                sql=sql+" SHELF_ID=%s "
                Cond_Check=True
            Values+=(KAShelfID,)
        if KAPubLoc!='':
            if Cond_Check==True:
                sql=sql+" AND PUB_LOC=%s "
            else:
                sql=sql+" PUB_LOC=%s "
                Cond_Check=True
            Values+=(KAPubLoc,)
                                
        print(Values)
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    
    def KAYeniAramaGiris(self):
        self.KAIDVar.set(0)
        self.KAISBNVar.set("")
        self.KAAuthVar.set("")
        self.KATitleVar.set("")
        self.KASubjVar.set("")
        self.KAPubYearVar.set(0)
        self.KAPubCompVar.set("")
        self.KAEditionVar.set("")
        self.KALangVar.set("")
        self.KAShelfIDVar.set("")
        self.KAPubLocVar.set("")
            
    def KAKapat(self):
        self.KitapAramaEkrani.destroy()
        
    def KitapArama(self):
        self.KitapAramaEkrani=tk.Toplevel(self.Admin_Screen)        
        self.KitapAramaEkrani.title("KİTAP ARAMA EKRANI")
        self.KitapAramaEkrani.geometry("500x450")
        self.KitapAramaEkrani.transient(self.Admin_Screen)
        
        self.KAInputFrame=tk.Frame(self.KitapAramaEkrani)
        self.KAInputFrame.grid(row=0,column=0)
        self.KAButtonFrame=tk.Frame(self.KitapAramaEkrani)
        self.KAButtonFrame.grid(row=1,column=0)
        
        self.KAIDVar=tk.IntVar()
        self.KAID=tk.Label(self.KAInputFrame,text="Kitap ID",\
                           width=20)
        self.KAID.grid(row=0,column=0,sticky='nw')
        self.KAIDGiris=tk.Entry(self.KAInputFrame,width=50,\
                                    textvariable=self.KAIDVar)
        self.KAIDGiris.grid(row=0,column=1)
        
        self.KAISBNVar=tk.StringVar()
        self.KAISBN=tk.Label(self.KAInputFrame,text="Kitap ISBN",\
                             width=20)
        self.KAISBN.grid(row=1,column=0,sticky='nw')
        self.KAISBNGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAISBNVar)
        self.KAISBNGiris.grid(row=1,column=1)
        
        self.KAAuthVar=tk.StringVar()
        self.KAAuth=tk.Label(self.KAInputFrame,text="Kitap Author",\
                             width=20)
        self.KAAuth.grid(row=2,column=0,sticky='nw')
        self.KAAuthGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAAuthVar)
        self.KAAuthGiris.grid(row=2,column=1)
        
        self.KATitleVar=tk.StringVar()
        self.KATitle=tk.Label(self.KAInputFrame,text="Kitap Title",\
                              width=20)
        self.KATitle.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.KATitleGiris=tk.Entry(self.KAInputFrame,width=50,\
                                       textvariable=self.KATitleVar)
        self.KATitleGiris.grid(row=3,column=1)
        
        self.KASubjVar=tk.StringVar()
        self.KASubj=tk.Label(self.KAInputFrame,text="Kitap Subject",\
                             width=20)
        self.KASubj.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.KASubjGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KASubjVar)
        self.KASubjGiris.grid(row=4,column=1)
        
        self.KAPubYearVar=tk.IntVar()
        self.KAPubYear=tk.Label(self.KAInputFrame,text="Kitap Pub. Year",\
                                width=20)
        self.KAPubYear.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubYearGiris=tk.Entry(self.KAInputFrame,width=50,\
                                     textvariable=self.KAPubYearVar)
        self.KAPubYearGiris.grid(row=5,column=1)
        
        self.KAPubCompVar=tk.StringVar()
        self.KAPubComp=tk.Label(self.KAInputFrame,text="Kitap Publisher",\
                                width=20)
        self.KAPubComp.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubCompGiris=tk.Entry(self.KAInputFrame,width=50,\
                                         textvariable=self.KAPubCompVar)
        self.KAPubCompGiris.grid(row=6,column=1)
        
        self.KAEditionVar=tk.StringVar()
        self.KAEdition=tk.Label(self.KAInputFrame,text="Kitap Edition",\
                                width=20)
        self.KAEdition.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.KAEditionGiris=tk.Entry(self.KAInputFrame,width=50,\
                                         textvariable=self.KAEditionVar)
        self.KAEditionGiris.grid(row=7,column=1)
        
        self.KALangVar=tk.StringVar()
        self.KALang=tk.Label(self.KAInputFrame,text="Kitap Language",\
                             width=20)
        self.KALang.grid(row=8,column=0,padx=3,pady=3,sticky="nw")
        self.KALangGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KALangVar)
        self.KALangGiris.grid(row=8,column=1)
        
        self.KAShelfIDVar=tk.StringVar()
        self.KAShelfID=tk.Label(self.KAInputFrame,text="Kitap Shelf ID",\
                                width=20)
        self.KAShelfID.grid(row=9,column=0,padx=3,pady=3,sticky="nw")
        self.KAShelfIDGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAShelfIDVar)
        self.KAShelfIDGiris.grid(row=9,column=1)
                      
        self.KAPubLocVar=tk.StringVar()
        self.KAPubLoc=tk.Label(self.KAInputFrame,text="Kitap Pub. Location",\
                               width=20)
        self.KAPubLoc.grid(row=11,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubLocGiris=tk.Entry(self.KAInputFrame,width=50,\
                                       textvariable=self.KAPubLocVar)
        self.KAPubLocGiris.grid(row=11,column=1)
        
        self.KAAra=tk.Button(self.KAButtonFrame,text="Kitap Ara",\
                       bg="lightgreen",command=self.KitapAraListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAra.grid(row=0,column=0)
        
        self.KAYeniGiris=tk.Button(self.KAButtonFrame,text="Yeni Arama",\
                       bg="lightgreen",command=self.KAYeniAramaGiris,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAYeniGiris.grid(row=0,column=1)
        
        self.KACikis=tk.Button(self.KAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.KAKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KACikis.grid(row=0,column=2)
    
    def UyeAraListele(self):    
        UAID=self.UAIDVar.get()
        UANAME=self.UANameVar.get()
        UASURNAME=self.UASurnameVar.get()
        UABDATE=self.UABDateVar.get()
        UABPLACE=self.UABPlaceVar.get()
        UAADDRESS=self.UAAddressVar.get()
        UAEMAIL=self.UAEMailVar.get()
        UATELNO=self.UATelNoVar.get()
        
        Values=()
        Cond_Check=False # Check if a condition is aready added
        sql="SELECT * FROM MEMBERS_TBL WHERE"
        if UAID!=0:
            sql=sql+" MEMBER_ID=%s "
            Values=Values+(UAID,)
            Cond_Check=True
        if UANAME!='':
            if Cond_Check==True:
                sql=sql+" AND M_NAME=%s "
            else:
                sql=sql+" M_NAME=%s "
                Cond_Check=True
            Values+=(UANAME,)
        if UASURNAME!='':
            if Cond_Check==True:
                sql=sql+" AND M_SURNAME=%s "
            else:
                sql=sql+" M_SURNAME=%s "
                Cond_Check=True
            Values+=(UASURNAME,)
        if UABDATE!='':
            if Cond_Check==True:
                sql=sql+" AND B_DATE=%s "
            else:
                sql=sql+" B_DATE=%s "
                Cond_Check=True
            Values+=(UABDATE,)
        if UABPLACE!='':
            if Cond_Check==True:
                sql=sql+" AND B_PLACE=%s "
            else:
                sql=sql+" B_PLACE=%s "
                Cond_Check=True
            Values+=(UABPLACE,)
        if UAADDRESS!='':
            if Cond_Check==True:
                sql=sql+" AND ADRESS=%s "
            else:
                sql=sql+" ADDRESS=%s "
                Cond_Check=True
            Values+=(UAADDRESS,)
        if UAEMAIL!='':
            if Cond_Check==True:
                sql=sql+" AND E_MAIL=%s "
            else:
                sql=sql+" E_MAIL=%s "
                Cond_Check=True
            Values+=(UAEMAIL,)
        if UATELNO!='':
            if Cond_Check==True:
                sql=sql+" AND TEL_NO=%s "
            else:
                sql=sql+" TEL_NO=%s "
                Cond_Check=True
            Values+=(UATELNO,)    
                                
        print(Values)
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    
    def UAYeniAramaGiris(self):
        self.UAIDVar.set(0)
        self.UANameVar.set("")
        self.UASurnameVar.set("")
        self.UABDateVar.set("")
        self.UABPlaceVar.set("")
        self.UAAddressVar.set("")
        self.UAEMailVar.set("")
        self.UATelNoVar.set("")    
        
    def UAUyeEMailGonder(self):
        adminmail = "blgm416deneme@gmail.com"
        receivermail=self.UAEMailVar.get()           
        server=smtplib.SMTP('smtp.gmail.com:587')
        pass_word="blgm416CORONA"
        subject="Odunc alip zamaninda iade etmediginiz kitaplar"
        # This allow you to include a subject by adding from, 
        # to and subject line
        main_message="Lutfen odunc aldiginiz ve iadesi zaman asimina \
        ugramis kitaplari en kisa surede iade ediniz"
        Body="""From: Name here <adminmail>
        To: <receivermail>
        Subject:%s 

        %s""" %(subject,main_message )


        try:
            server=smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(adminmail, pass_word)
            server.sendmail(adminmail,receivermail, Body )

            print('message sent')
         #error handling
        except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
            print('message not sent')
        finally:
            server.quit()

            
    def UAKapat(self):
        self.UyeAramaEkrani.destroy()
        
    def UyeArama(self):
        self.UyeAramaEkrani=tk.Toplevel(self.Admin_Screen)        
        self.UyeAramaEkrani.title("ÜYE ARAMA EKRANI")
        self.UyeAramaEkrani.geometry("500x450")
        self.UyeAramaEkrani.transient(self.Admin_Screen)
        
        self.UAInputFrame=tk.Frame(self.UyeAramaEkrani)
        self.UAInputFrame.grid(row=0,column=0)
        self.UAButtonFrame=tk.Frame(self.UyeAramaEkrani)
        self.UAButtonFrame.grid(row=1,column=0)
        
        self.UAIDVar=tk.IntVar()
        self.UAID=tk.Label(self.UAInputFrame,text="Üye ID",\
                           width=20)
        self.UAID.grid(row=0,column=0,sticky='nw')
        self.UAIDGiris=tk.Entry(self.UAInputFrame,width=50,\
                                    textvariable=self.UAIDVar)
        self.UAIDGiris.grid(row=0,column=1)
        
        self.UANameVar=tk.StringVar()
        self.UAName=tk.Label(self.UAInputFrame,text="Üye Adı",\
                             width=20)
        self.UAName.grid(row=1,column=0,sticky='nw')
        self.UANameGiris=tk.Entry(self.UAInputFrame,width=50,\
                                      textvariable=self.UANameVar)
        self.UANameGiris.grid(row=1,column=1)
        
        self.UASurnameVar=tk.StringVar()
        self.UASurname=tk.Label(self.UAInputFrame,text="Üye Soyadı",\
                             width=20)
        self.UASurname.grid(row=2,column=0,sticky='nw')
        self.UASurnameGiris=tk.Entry(self.UAInputFrame,width=50,\
                                      textvariable=self.UASurnameVar)
        self.UASurnameGiris.grid(row=2,column=1)
        
        self.UABDateVar=tk.StringVar()
        self.UABDate=tk.Label(self.UAInputFrame,text="Üye D. Tarihi",\
                              width=20)
        self.UABDate.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.UABDateGiris=tk.Entry(self.UAInputFrame,width=50,\
                                       textvariable=self.UABDateVar)
        self.UABDateGiris.grid(row=3,column=1)
        
        self.UABPlaceVar=tk.StringVar()
        self.UABPlace=tk.Label(self.UAInputFrame,text="Üye D. Yeri",\
                             width=20)
        self.UABPlace.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.UABPlaceGiris=tk.Entry(self.UAInputFrame,width=50,\
                                      textvariable=self.UABPlaceVar)
        self.UABPlaceGiris.grid(row=4,column=1)
        
        self.UAAddressVar=tk.StringVar()
        self.UAAdress=tk.Label(self.UAInputFrame,text="Üye Adresi",\
                                width=20)
        self.UAAdress.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.UAAddressGiris=tk.Entry(self.UAInputFrame,width=50,\
                                     textvariable=self.UAAddressVar)
        self.UAAddressGiris.grid(row=5,column=1)
        
        self.UAEMailVar=tk.StringVar()
        self.UAEMail=tk.Label(self.UAInputFrame,text="Üye E_Posta Adresi",\
                                width=20)
        self.UAEMail.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.UAEMailGiris=tk.Entry(self.UAInputFrame,width=50,\
                                         textvariable=self.UAEMailVar)
        self.UAEMailGiris.grid(row=6,column=1)
        
        self.UATelNoVar=tk.StringVar()
        self.UATelNo=tk.Label(self.UAInputFrame,text="Üye Tel. No.",\
                                width=20)
        self.UATelNo.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.UATelNoGiris=tk.Entry(self.UAInputFrame,width=50,\
                                         textvariable=self.UATelNoVar)
        self.UATelNoGiris.grid(row=7,column=1)                        
        
        self.UAAra=tk.Button(self.UAButtonFrame,text="Üye Ara",\
                       bg="lightgreen",command=self.UyeAraListele,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAAra.grid(row=0,column=0)
        
        self.UAYeniGiris=tk.Button(self.UAButtonFrame,text="Yeni Arama",\
                       bg="lightgreen",command=self.UAYeniAramaGiris,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAYeniGiris.grid(row=0,column=1)
        
        self.UAEMailGonder=tk.Button(self.UAButtonFrame,text="E-Mail Gönder",\
                       bg="lightgreen",command=self.UAUyeEMailGonder,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAEMailGonder.grid(row=0,column=2)
        
        self.UACikis=tk.Button(self.UAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.UAKapat,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UACikis.grid(row=0,column=3)            
    
class officerIslemleri(object):
    def __init__(self):
        self.Officer_Screen=tk.Toplevel(root)
        self.Officer_Screen.title("ÇALIŞAN İŞLEMLERİ EKRANI")
        self.Officer_Screen.geometry("1050x250")
        self.Officer_Screen.transient(root)

        self.OduncVerme=tk.Button(self.Officer_Screen,text="Ödünç Kitap Verme",\
                       bg="pink",command=self.OduncKitapVerme,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.OduncVerme.grid(row=0,column=0)
        
        self.KitapArama=tk.Button(self.Officer_Screen,text="Kitap Arama",\
                       bg="pink",command=self.KitapArama,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.KitapArama.grid(row=0,column=1)
        
        self.UyeArama=tk.Button(self.Officer_Screen,text="Üye Arama",\
                       bg="pink",command=self.UyeArama,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.UyeArama.grid(row=1,column=0)
        
        self.IadeEdilmeyen=tk.Button(self.Officer_Screen,text="İade Edilmeyen Kitaplar",\
                       bg="pink",command=self.IadeEdilmeyenKitaplar,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.IadeEdilmeyen.grid(row=1,column=1)
        
        self.IGKullanıcılar=tk.Button(self.Officer_Screen,text="İade Süresini İhlal Eden Kullanıcılar",\
                       bg="pink",command=self.IadeEtmeyenKullanicilar,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.IGKullanıcılar.grid(row=2,column=0)
        
        self.Raporlar=tk.Button(self.Officer_Screen,text="Raporlar",\
                       bg="pink",command=self.OfficerRaporlar,\
                       relief="raised",borderwidth=8,width=30,\
                       font=('Helvetica', '20'))        
        self.Raporlar.grid(row=2,column=1)
 
     
    def KitapAraListele(self):
        KAID=self.KAIDVar.get()
        KAISBN=self.KAISBNVar.get()
        KAAuth=self.KAAuthVar.get()
        KATitle=self.KATitleVar.get()
        KASubj=self.KASubjVar.get()
        KAPubYear=self.KAPubYearVar.get()
        KAPubComp=self.KAPubCompVar.get()
        KAEdition=self.KAEditionVar.get()
        KALang=self.KALangVar.get()
        KAShelfID=self.KAShelfIDVar.get()
        KAPubLoc=self.KAPubLocVar.get()
        
        Values=()
        Cond_Check=False # Check if a condition is aready added
        sql="SELECT * FROM BOOKS_TBL WHERE"
        if KAID!=0:
            sql=sql+" BOOK_ID=%s "
            Values=Values+(KAID,)
            Cond_Check=True
        if KAISBN!='':
            if Cond_Check==True:
                sql=sql+" AND ISBN=%s "
            else:
                sql=sql+" ISBN=%s "
                Cond_Check=True
            Values+=(KAISBN,)
        if KAAuth!='':
            if Cond_Check==True:
                sql=sql+" AND AUTHOR=%s "
            else:
                sql=sql+" AUTHOR=%s "
                Cond_Check=True
            Values+=(KAAuth,)
        if KATitle!='':
            if Cond_Check==True:
                sql=sql+" AND TITLE=%s "
            else:
                sql=sql+" TITLE=%s "
                Cond_Check=True
            Values+=(KATitle,)
        if KASubj!='':
            if Cond_Check==True:
                sql=sql+" AND SUBJECT=%s "
            else:
                sql=sql+" SUBJECT=%s "
                Cond_Check=True
            Values+=(KASubj,)
        if KAPubYear!=0:
            if Cond_Check==True:
                sql=sql+" AND PUB_YEAR=%s "
            else:
                sql=sql+" PUB_YEAR=%s "
                Cond_Check=True
            Values+=(KAPubYear,)
        if KAPubComp!='':
            if Cond_Check==True:
                sql=sql+" AND PUBLISHER=%s "
            else:
                sql=sql+" PUBLISHER=%s "
                Cond_Check=True
            Values+=(KAPubComp,)
        if KAEdition!='':
            if Cond_Check==True:
                sql=sql+" AND EDITION=%s "
            else:
                sql=sql+" EDITION=%s "
                Cond_Check=True
            Values+=(KAEdition,)
        if KALang!='':
            if Cond_Check==True:
                sql=sql+" AND LANG=%s "
            else:
                sql=sql+" LANG=%s "
                Cond_Check=True
            Values+=(KALang,)
        if KAShelfID!='':
            if Cond_Check==True:
                sql=sql+" AND SHELF_ID=%s "
            else:
                sql=sql+" SHELF_ID=%s "
                Cond_Check=True
            Values+=(KAShelfID,)
        if KAPubLoc!='':
            if Cond_Check==True:
                sql=sql+" AND PUB_LOC=%s "
            else:
                sql=sql+" PUB_LOC=%s "
                Cond_Check=True
            Values+=(KAPubLoc,)
                                
        print(Values)
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    
    def KAYeniAramaGiris(self):
        self.KAIDVar.set(0)
        self.KAISBNVar.set("")
        self.KAAuthVar.set("")
        self.KATitleVar.set("")
        self.KASubjVar.set("")
        self.KAPubYearVar.set(0)
        self.KAPubCompVar.set("")
        self.KAEditionVar.set("")
        self.KALangVar.set("")
        self.KAShelfIDVar.set("")
        self.KAPubLocVar.set("")
            
    def KAKapat(self):
        self.KitapAramaEkrani.destroy()
    
    def KitapArama(self):
        self.KitapAramaEkrani=tk.Toplevel(self.Officer_Screen)        
        self.KitapAramaEkrani.title("KİTAP ARAMA EKRANI")
        self.KitapAramaEkrani.geometry("500x450")
        self.KitapAramaEkrani.transient(self.Officer_Screen)
        
        self.KAInputFrame=tk.Frame(self.KitapAramaEkrani)
        self.KAInputFrame.grid(row=0,column=0)
        self.KAButtonFrame=tk.Frame(self.KitapAramaEkrani)
        self.KAButtonFrame.grid(row=1,column=0)
        
        self.KAIDVar=tk.IntVar()
        self.KAID=tk.Label(self.KAInputFrame,text="Kitap ID",\
                           width=20)
        self.KAID.grid(row=0,column=0,sticky='nw')
        self.KAIDGiris=tk.Entry(self.KAInputFrame,width=50,\
                                    textvariable=self.KAIDVar)
        self.KAIDGiris.grid(row=0,column=1)
        
        self.KAISBNVar=tk.StringVar()
        self.KAISBN=tk.Label(self.KAInputFrame,text="Kitap ISBN",\
                             width=20)
        self.KAISBN.grid(row=1,column=0,sticky='nw')
        self.KAISBNGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAISBNVar)
        self.KAISBNGiris.grid(row=1,column=1)
        
        self.KAAuthVar=tk.StringVar()
        self.KAAuth=tk.Label(self.KAInputFrame,text="Kitap Author",\
                             width=20)
        self.KAAuth.grid(row=2,column=0,sticky='nw')
        self.KAAuthGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAAuthVar)
        self.KAAuthGiris.grid(row=2,column=1)
        
        self.KATitleVar=tk.StringVar()
        self.KATitle=tk.Label(self.KAInputFrame,text="Kitap Title",\
                              width=20)
        self.KATitle.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.KATitleGiris=tk.Entry(self.KAInputFrame,width=50,\
                                       textvariable=self.KATitleVar)
        self.KATitleGiris.grid(row=3,column=1)
        
        self.KASubjVar=tk.StringVar()
        self.KASubj=tk.Label(self.KAInputFrame,text="Kitap Subject",\
                             width=20)
        self.KASubj.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.KASubjGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KASubjVar)
        self.KASubjGiris.grid(row=4,column=1)
        
        self.KAPubYearVar=tk.IntVar()
        self.KAPubYear=tk.Label(self.KAInputFrame,text="Kitap Pub. Year",\
                                width=20)
        self.KAPubYear.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubYearGiris=tk.Entry(self.KAInputFrame,width=50,\
                                     textvariable=self.KAPubYearVar)
        self.KAPubYearGiris.grid(row=5,column=1)
        
        self.KAPubCompVar=tk.StringVar()
        self.KAPubComp=tk.Label(self.KAInputFrame,text="Kitap Publisher",\
                                width=20)
        self.KAPubComp.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubCompGiris=tk.Entry(self.KAInputFrame,width=50,\
                                         textvariable=self.KAPubCompVar)
        self.KAPubCompGiris.grid(row=6,column=1)
        
        self.KAEditionVar=tk.StringVar()
        self.KAEdition=tk.Label(self.KAInputFrame,text="Kitap Edition",\
                                width=20)
        self.KAEdition.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.KAEditionGiris=tk.Entry(self.KAInputFrame,width=50,\
                                         textvariable=self.KAEditionVar)
        self.KAEditionGiris.grid(row=7,column=1)
        
        self.KALangVar=tk.StringVar()
        self.KALang=tk.Label(self.KAInputFrame,text="Kitap Language",\
                             width=20)
        self.KALang.grid(row=8,column=0,padx=3,pady=3,sticky="nw")
        self.KALangGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KALangVar)
        self.KALangGiris.grid(row=8,column=1)
        
        self.KAShelfIDVar=tk.StringVar()
        self.KAShelfID=tk.Label(self.KAInputFrame,text="Kitap Shelf ID",\
                                width=20)
        self.KAShelfID.grid(row=9,column=0,padx=3,pady=3,sticky="nw")
        self.KAShelfIDGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAShelfIDVar)
        self.KAShelfIDGiris.grid(row=9,column=1)
                      
        self.KAPubLocVar=tk.StringVar()
        self.KAPubLoc=tk.Label(self.KAInputFrame,text="Kitap Pub. Location",\
                               width=20)
        self.KAPubLoc.grid(row=11,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubLocGiris=tk.Entry(self.KAInputFrame,width=50,\
                                       textvariable=self.KAPubLocVar)
        self.KAPubLocGiris.grid(row=11,column=1)
        
        self.KAAra=tk.Button(self.KAButtonFrame,text="Kitap Ara",\
                       bg="lightgreen",command=self.KitapAraListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAra.grid(row=0,column=0)
        
        self.KAYeniGiris=tk.Button(self.KAButtonFrame,text="Yeni Arama",\
                       bg="lightgreen",command=self.KAYeniAramaGiris,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAYeniGiris.grid(row=0,column=1)
        
        self.KACikis=tk.Button(self.KAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.KAKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KACikis.grid(row=0,column=2)
  
        
    def UyeAraListele(self):    
        UAID=self.UAIDVar.get()
        UANAME=self.UANameVar.get()
        UASURNAME=self.UASurnameVar.get()
        UABDATE=self.UABDateVar.get()
        UABPLACE=self.UABPlaceVar.get()
        UAADDRESS=self.UAAddressVar.get()
        UAEMAIL=self.UAEMailVar.get()
        UATELNO=self.UATelNoVar.get()
        
        Values=()
        Cond_Check=False # Check if a condition is aready added
        sql="SELECT * FROM MEMBERS_TBL WHERE"
        if UAID!=0:
            sql=sql+" MEMBER_ID=%s "
            Values=Values+(UAID,)
            Cond_Check=True
        if UANAME!='':
            if Cond_Check==True:
                sql=sql+" AND M_NAME=%s "
            else:
                sql=sql+" M_NAME=%s "
                Cond_Check=True
            Values+=(UANAME,)
        if UASURNAME!='':
            if Cond_Check==True:
                sql=sql+" AND M_SURNAME=%s "
            else:
                sql=sql+" M_SURNAME=%s "
                Cond_Check=True
            Values+=(UASURNAME,)
        if UABDATE!='':
            if Cond_Check==True:
                sql=sql+" AND B_DATE=%s "
            else:
                sql=sql+" B_DATE=%s "
                Cond_Check=True
            Values+=(UABDATE,)
        if UABPLACE!='':
            if Cond_Check==True:
                sql=sql+" AND B_PLACE=%s "
            else:
                sql=sql+" B_PLACE=%s "
                Cond_Check=True
            Values+=(UABPLACE,)
        if UAADDRESS!=0:
            if Cond_Check==True:
                sql=sql+" AND ADRESS=%s "
            else:
                sql=sql+" ADDRESS=%s "
                Cond_Check=True
            Values+=(UAADDRESS,)
        if UAEMAIL!='':
            if Cond_Check==True:
                sql=sql+" AND E_MAIL=%s "
            else:
                sql=sql+" E_MAIL=%s "
                Cond_Check=True
            Values+=(UAEMAIL,)
        if UATELNO!='':
            if Cond_Check==True:
                sql=sql+" AND TEL_NO=%s "
            else:
                sql=sql+" TEL_NO=%s "
                Cond_Check=True
            Values+=(UATELNO,)    
                                
        print(Values)
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    
    def UAYeniAramaGiris(self):
        self.UAIDVar.set(0)
        self.UANameVar.set("")
        self.UASurnameVar.set("")
        self.UABDateVar.set("")
        self.UABPlaceVar.set("")
        self.UAAddressVar.set("")
        self.UAEMailVar.set("")
        self.UATelNoVar.set("")    
        
    def UAUyeEMailGonder(self):
        adminmail = "blgm416deneme@gmail.com"
        receivermail=self.UAEMailVar.get()           
        server=smtplib.SMTP('smtp.gmail.com:587')
        pass_word="blgm416CORONA"
        subject="Odunc alip zamaninda iade etmediginiz kitaplar"
        # This allow you to include a subject by adding from, 
        # to and subject line
        main_message="Lutfen odunc aldiginiz ve iadesi zaman asimina \
        ugramis kitaplari en kisa surede iade ediniz"
        Body="""From: Name here <adminmail>
        To: <receivermail>
        Subject:%s 

        %s""" %(subject,main_message )


        try:
            server=smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(adminmail, pass_word)
            server.sendmail(adminmail,receivermail, Body )

            print('message sent')
         #error handling
        except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
            print('message not sent')
        finally:
            server.quit()

            
    def UAKapat(self):
        self.UyeAramaEkrani.destroy()
        
    def UyeArama(self):
        self.UyeAramaEkrani=tk.Toplevel(self.Officer_Screen)        
        self.UyeAramaEkrani.title("ÜYE ARAMA EKRANI")
        self.UyeAramaEkrani.geometry("500x450")
        self.UyeAramaEkrani.transient(self.Officer_Screen)
        
        self.UAInputFrame=tk.Frame(self.UyeAramaEkrani)
        self.UAInputFrame.grid(row=0,column=0)
        self.UAButtonFrame=tk.Frame(self.UyeAramaEkrani)
        self.UAButtonFrame.grid(row=1,column=0)
        
        self.UAIDVar=tk.IntVar()
        self.UAID=tk.Label(self.UAInputFrame,text="Üye ID",\
                           width=20)
        self.UAID.grid(row=0,column=0,sticky='nw')
        self.UAIDGiris=tk.Entry(self.UAInputFrame,width=50,\
                                    textvariable=self.UAIDVar)
        self.UAIDGiris.grid(row=0,column=1)
        
        self.UANameVar=tk.StringVar()
        self.UAName=tk.Label(self.UAInputFrame,text="Üye Adı",\
                             width=20)
        self.UAName.grid(row=1,column=0,sticky='nw')
        self.UANameGiris=tk.Entry(self.UAInputFrame,width=50,\
                                      textvariable=self.UANameVar)
        self.UANameGiris.grid(row=1,column=1)
        
        self.UASurnameVar=tk.StringVar()
        self.UASurname=tk.Label(self.UAInputFrame,text="Üye Soyadı",\
                             width=20)
        self.UASurname.grid(row=2,column=0,sticky='nw')
        self.UASurnameGiris=tk.Entry(self.UAInputFrame,width=50,\
                                      textvariable=self.UASurnameVar)
        self.UASurnameGiris.grid(row=2,column=1)
        
        self.UABDateVar=tk.StringVar()
        self.UABDate=tk.Label(self.UAInputFrame,text="Üye D. Tarihi",\
                              width=20)
        self.UABDate.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.UABDateGiris=tk.Entry(self.UAInputFrame,width=50,\
                                       textvariable=self.UABDateVar)
        self.UABDateGiris.grid(row=3,column=1)
        
        self.UABPlaceVar=tk.StringVar()
        self.UABPlace=tk.Label(self.UAInputFrame,text="Üye D. Yeri",\
                             width=20)
        self.UABPlace.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.UABPlaceGiris=tk.Entry(self.UAInputFrame,width=50,\
                                      textvariable=self.UABPlaceVar)
        self.UABPlaceGiris.grid(row=4,column=1)
        
        self.UAAddressVar=tk.StringVar()
        self.UAAdress=tk.Label(self.UAInputFrame,text="Üye Adresi",\
                                width=20)
        self.UAAdress.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.UAAddressGiris=tk.Entry(self.UAInputFrame,width=50,\
                                     textvariable=self.UAAddressVar)
        self.UAAddressGiris.grid(row=5,column=1)
        
        self.UAEMailVar=tk.StringVar()
        self.UAEMail=tk.Label(self.UAInputFrame,text="Üye E_Posta Adresi",\
                                width=20)
        self.UAEMail.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.UAEMailGiris=tk.Entry(self.UAInputFrame,width=50,\
                                         textvariable=self.UAEMailVar)
        self.UAEMailGiris.grid(row=6,column=1)
        
        self.UATelNoVar=tk.StringVar()
        self.UATelNo=tk.Label(self.UAInputFrame,text="Üye Tel. No.",\
                                width=20)
        self.UATelNo.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.UATelNoGiris=tk.Entry(self.UAInputFrame,width=50,\
                                         textvariable=self.UATelNoVar)
        self.UATelNoGiris.grid(row=7,column=1)                        
        
        self.UAAra=tk.Button(self.UAButtonFrame,text="Üye Ara",\
                       bg="lightgreen",command=self.UyeAraListele,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAAra.grid(row=0,column=0)
        
        self.UAYeniGiris=tk.Button(self.UAButtonFrame,text="Yeni Arama",\
                       bg="lightgreen",command=self.UAYeniAramaGiris,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAYeniGiris.grid(row=0,column=1)
        
        self.UAEMailGonder=tk.Button(self.UAButtonFrame,text="E-Mail Gönder",\
                       bg="lightgreen",command=self.UAUyeEMailGonder,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAEMailGonder.grid(row=0,column=2)
        
        self.UACikis=tk.Button(self.UAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.UAKapat,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UACikis.grid(row=0,column=3)            

        
    
    def IadeEdilmeyenKitaplarListele(self):
        
        Values=()
        sql="SELECT * FROM BORROW_TBL"
       
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    
            
    def IadeEdilmeyenKapat(self):
        self.IadeEdilmeyenKitaplar.destroy()
        
    def IadeEtmeyenKullaniciListele(self):
        Values=()
        sql="SELECT * FROM MEMBERS_TBL, BOOKS_TBL WHERE MEMBER_ID= 1 AND M_NAME='Osman' "
       
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
        
        
    def IadeEtmeyenKullaniciTarihListele(self):
        sql="SELECT * FROM BORROW_TBL where D_DATE"
       
        print(sql)
        mycursor.execute("select * from BORROW_TBL where D_DATE <DATE_SUB(now(), INTERVAL 15 DAY)")
        data=mycursor.fetchall()
        print(data)
    
    def IadeEdilmeyenKitaplar(self):
        self.IadeEdilmeyenKitaplar=tk.Toplevel(self.Officer_Screen)        
        self.IadeEdilmeyenKitaplar.title("İADE EDİLMEYEN KİTAPLAR EKRANI")
        self.IadeEdilmeyenKitaplar.geometry("600x450")
        self.IadeEdilmeyenKitaplar.transient(self.Officer_Screen)
        
        self.KAInputFrame=tk.Frame(self.IadeEdilmeyenKitaplar)
        self.KAInputFrame.grid(row=0,column=0)
        self.KAButtonFrame=tk.Frame(self.IadeEdilmeyenKitaplar)
        self.KAButtonFrame.grid(row=1,column=0)
        
        
        self.KAAra=tk.Button(self.KAButtonFrame,text="Kitapları Listele",\
                       bg="lightgreen",command=self.IadeEdilmeyenKitaplarListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAra.grid(row=2,column=0)
        
        
        self.KACikis=tk.Button(self.KAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.IadeEdilmeyenKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KACikis.grid(row=2,column=1)

        self.KAListele=tk.Button(self.KAButtonFrame,text="İade Etmeyen Kullanıcı",\
                       bg="lightgreen",command=self.IadeEtmeyenKullaniciListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAListele.grid(row=3,column=0)        
        
        self.KAListelee=tk.Button(self.KAButtonFrame,text="Süresine Göre Listele",\
                       bg="lightgreen",command=self.IadeEtmeyenKullaniciTarihListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAListelee.grid(row=4,column=0) 

        
    
    def IadeEtmeyenKKListele(self):
        
        sql="SELECT * FROM BORROW_TBL,MEMBERS_TBL where D_DATE AND M_NAME=%s"
       
        print(sql)
        mycursor.execute("select * from BORROW_TBL where D_DATE <DATE_SUB(now(), INTERVAL 15 DAY)")
        data=mycursor.fetchall()
        print(data)
         
    def IadeEdilmeyenKKapat(self):
        self.IadeEtmeyenK.destroy()
        


    def YasakliUyeEkle(self):        
        MEMBER_ID=self.UserIDVar.get()
        M_NAME=self.UserNameVar.get()
        M_SURNAME=self.UserSurnameVar.get()
        B_DATE=self.UserBirthDateVar.get()
        B_PLACE=self.UserBirthPlaceVar.get()
        ADRESS=self.UserAddressVar.get()
        E_MAIL=self.UserEMailVar.get()
        TEL_NO=self.UserTelNoVar.get()
                
        Values=(MEMBER_ID,M_NAME,M_SURNAME,B_DATE,B_PLACE,ADRESS,E_MAIL,TEL_NO)
        sql="Insert into YasakliKullanici(MEMBER_ID,M_NAME,M_SURNAME,B_DATE,B_PLACE,ADRESS,\
        E_MAIL,TEL_NO) \
        values(%s,%s,%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(sql,Values)
        db.commit()                
        
    def YYasakliUyeGiris(self):
        self.UserIDVar.set(0)
        self.UserNameVar.set("")
        self.UserSurnameVar.set("")
        self.UserBirthDateVar.set("")
        self.UserBirthPlaceVar.set("")
        self.UserAddressVar.set("")
        self.UserEMailVar.set("")
        self.UserTelNoVar.set("")        
    
    def YasakliUyeKapat(self):
        self.YasakliUyeEkrani.destroy()
    def YeniUyeEkle(self):        
        self.YasakliUyeEkrani=tk.Toplevel(self.Officer_Screen)        
        self.YasakliUyeEkrani.title("Yasakli Üye Ekleme")
        self.YasakliUyeEkrani.geometry("500x450")
        self.YasakliUyeEkrani.transient(self.Officer_Screen)
        
        self.YUInputFrame=tk.Frame(self.YasakliUyeEkrani)
        self.YUInputFrame.grid(row=0,column=0)
        self.YUButtonFrame=tk.Frame(self.YasakliUyeEkrani)
        self.YUButtonFrame.grid(row=1,column=0)
        
        self.UserIDVar=tk.IntVar()
        self.YUID=tk.Label(self.YUInputFrame,text="Yasakli Üye ID",\
                           width=20)
        self.YUID.grid(row=0,column=0,sticky='nw')
        self.YUIDGiris=tk.Entry(self.YUInputFrame,width=50,\
                                    textvariable=self.UserIDVar)
        self.YUIDGiris.grid(row=0,column=1)
        
        self.UserNameVar=tk.StringVar()
        self.YUName=tk.Label(self.YUInputFrame,text="Yasakli İsim",\
                             width=20)
        self.YUName.grid(row=1,column=0,sticky='nw')
        self.YUNameGiris=tk.Entry(self.YUInputFrame,width=50,\
                                      textvariable=self.UserNameVar)
        self.YUNameGiris.grid(row=1,column=1)
        
        self.UserSurnameVar=tk.StringVar()
        self.YUSurname=tk.Label(self.YUInputFrame,text="Yasakli Soyadı",\
                             width=20)
        self.YUSurname.grid(row=2,column=0,sticky='nw')
        self.YUSurnameGiris=tk.Entry(self.YUInputFrame,width=50,\
                                      textvariable=self.UserSurnameVar)
        self.YUSurnameGiris.grid(row=2,column=1)
        
        self.UserBirthDateVar=tk.StringVar()
        self.YUBirthDate=tk.Label(self.YUInputFrame,text="Yasakli Doğum Tarihi",\
                              width=20)
        self.YUBirthDate.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.YUBirthDateGiris=tk.Entry(self.YUInputFrame,width=50,\
                                       textvariable=self.UserBirthDateVar)
        self.YUBirthDateGiris.grid(row=3,column=1)
        
        self.UserBirthPlaceVar=tk.StringVar()
        self.YUBirthPlace=tk.Label(self.YUInputFrame,text="Yasakli Doğum Yeri",\
                             width=20)
        self.YUBirthPlace.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.YUBirthPlaceGiris=tk.Entry(self.YUInputFrame,width=50,\
                                      textvariable=self.UserBirthPlaceVar)
        self.YUBirthPlaceGiris.grid(row=4,column=1)
        
        self.UserAddressVar=tk.StringVar()
        self.YUAddress=tk.Label(self.YUInputFrame,text="Yasakli Adres",\
                                width=20)
        self.YUAddress.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.YUAddressGiris=tk.Entry(self.YUInputFrame,width=50,\
                                     textvariable=self.UserAddressVar)
        self.YUAddressGiris.grid(row=5,column=1)
        
        self.UserEMailVar=tk.StringVar()
        self.YUEMail=tk.Label(self.YUInputFrame,text="Yasakli E_Posta Adresi",\
                                width=20)
        self.YUEMail.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.YUEMailGiris=tk.Entry(self.YUInputFrame,width=50,\
                                         textvariable=self.UserEMailVar)
        self.YUEMailGiris.grid(row=6,column=1)
        
        self.UserTelNoVar=tk.StringVar()
        self.YUTelNo=tk.Label(self.YUInputFrame,text="Yasakli Tel. No.",\
                                width=20)
        self.YUTelNo.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.YUTelNoGiris=tk.Entry(self.YUInputFrame,width=50,\
                                         textvariable=self.UserTelNoVar)
        self.YUTelNoGiris.grid(row=7,column=1)
        
        
        self.YUKayit=tk.Button(self.YUButtonFrame,text="Yasakli Üye Kaydet",\
                       bg="lightgreen",command=self.YasakliUyeEkle,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YUKayit.grid(row=0,column=0)
        
        self.YUYeniGiris=tk.Button(self.YUButtonFrame,text="Yeni Yasaklı Giriş",\
                       bg="lightgreen",command=self.YYasakliUyeGiris,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YUYeniGiris.grid(row=0,column=1)
        
        self.YUCikis=tk.Button(self.YUButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.YasakliUyeKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.YUCikis.grid(row=0,column=2)
    def IadeEtmeyenKullanicilar(self):
        self.IadeEtmeyenK=tk.Toplevel(self.Officer_Screen)        
        self.IadeEtmeyenK.title("KİTAP ARAMA EKRANI")
        self.IadeEtmeyenK.geometry("500x450")
        self.IadeEtmeyenK.transient(self.Officer_Screen)
        
        self.KAInputFrame=tk.Frame(self.IadeEtmeyenK)
        self.KAInputFrame.grid(row=0,column=0)
        self.KAButtonFrame=tk.Frame(self.IadeEtmeyenK)
        self.KAButtonFrame.grid(row=1,column=0)
        
        
        self.KAAra=tk.Button(self.KAButtonFrame,text="Süre İhlali Yapanlar",\
                       bg="lightgreen",command=self.IadeEtmeyenKKListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAra.grid(row=0,column=0)
        
        
        self.KACikis=tk.Button(self.KAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.IadeEdilmeyenKKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KACikis.grid(row=0,column=1)

        self.KEYasakli=tk.Button(self.KAButtonFrame,text="Yasaklı Kullanıcı Ekle",\
                       bg="lightgreen",command=self.YeniUyeEkle,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KEYasakli.grid(row=2,column=0)
    
    
    def OfficerRaporlarListele(self):
        
        Values=()
        sql="SELECT * FROM Raporlar"
       
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)

    def GOfficerRaporlarListele(self):
        
        Values=()
        sql="SELECT * FROM Raporlar WHERE B_DATE='Today.day'"
       
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
        
        
    
    
            
    def RaporlarKapat(self):
        self.OfficerRaporlar.destroy()
        
    def OfficerRaporlar(self):
        self.OfficerRaporlar=tk.Toplevel(self.Officer_Screen)        
        self.OfficerRaporlar.title("RAPORLAR EKRANI")
        self.OfficerRaporlar.geometry("600x450")
        self.OfficerRaporlar.transient(self.Officer_Screen)
        
        self.KAInputFrame=tk.Frame(self.OfficerRaporlar)
        self.KAInputFrame.grid(row=0,column=0)
        self.KAButtonFrame=tk.Frame(self.OfficerRaporlar)
        self.KAButtonFrame.grid(row=1,column=0)
        
        self.KAAra=tk.Button(self.KAButtonFrame,text="Raporları Listele",\
                       bg="lightgreen",command=self.OfficerRaporlarListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAra.grid(row=2,column=0)
        
        self.KAAraa=tk.Button(self.KAButtonFrame,text="Günlük Raporları Listele",\
                       bg="lightgreen",command=self.GOfficerRaporlarListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAraa.grid(row=3,column=0)        
        
        self.KACikis=tk.Button(self.KAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.RaporlarKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KACikis.grid(row=2,column=1)
        

    # -----ODUNC VERME FONKSİYONLARI---------------
    def OKVUyeAraListele(self):
        global OKVUserID
        OKVUserID=self.OKVUIDVar.get()
        sql="SELECT * FROM MEMBERS_TBL WHERE MEMBER_ID= %s"
        mycursor.execute(sql,(OKVUserID,))
        row=mycursor.fetchall()        
        self.OKVNameGiris.state="enabled"
        self.OKVNameVar.set(row[0][1])
        self.OKVSurnameGiris.state="enabled"
        self.OKVSurnameVar.set(row[0][2])
        self.OKVBDateGiris.state="enabled"
        self.OKVBDateVar.set(row[0][3])
        self.OKVBPlaceGiris.state="enabled"
        self.OKVBPlaceVar.set(row[0][4])
        self.OKVAddressGiris.state="enabled"
        self.OKVAddressVar.set(row[0][5])
        
        self.OKVEMailGiris.state="enabled"
        self.OKVEMailVar.set(row[0][6])
        self.OKVTelNoGiris.state="enabled"
        self.OKVTelNoVar.set(row[0][7])        
        
        self.OKVKitapAra.config(state="normal")   
        self.OKVKIDGiris.config(state= "normal")

    def OKVKitapAraListele(self):        
        global OKVBOOKID
        OKVBOOKID=self.OKVKIDVar.get()
        sql="SELECT * FROM BOOKS_TBL WHERE BOOK_ID= %s"
        mycursor.execute(sql,(OKVBOOKID,))
        row=mycursor.fetchall()
        print(row)
        self.OKVISBNGiris.state="enabled"
        self.OKVISBNVar.set(row[0][1])
        self.OKVAuthGiris.state="enabled"
        self.OKVAuthVar.set(row[0][2])
        self.OKVTitleGiris.state="enabled"
        self.OKVTitleVar.set(row[0][3])
        self.OKVSubjGiris.state="enabled"
        self.OKVSubjVar.set(row[0][4])
        self.OKVPubYearGiris.state="enabled"
        self.OKVPubYearVar.set(row[0][5])
        
        self.OKVPubCompGiris.state="enabled"
        self.OKVPubCompVar.set(row[0][6])
        self.OKVEditionGiris.state="enabled"
        self.OKVEditionVar.set(row[0][7])
        self.OKVLangGiris.state="enabled"
        self.OKVLangVar.set(row[0][8])
        self.OKVShelfIDGiris.state="enabled"
        self.OKVShelfIDVar.set(row[0][9])
                
        self.OKVPubLocGiris.state="enabled"
        self.OKVPubLocVar.set(row[0][11])
        
        self.OKVOduncVer.config(state="normal")        
        

    def OKVKitabiOduncVer(self):        
        sql="SELECT * FROM MEMBERS_TBL EXCEPT SELECT * FROM YasakliKullanici WHERE MEMBER_ID=%s"
        mycursor.execute(sql,(OKVUserID,))
        User=mycursor.fetchall()
        
        sql="SELECT * FROM BOOKS_TBL WHERE BOOK_ID= %s"
        mycursor.execute(sql,(OKVBOOKID,))
        Book=mycursor.fetchall()
        
        MEMBER_ID=OKVUserID
        B_NAME=User[0][1]
        B_SURNAME=User[0][2]
        Today=datetime.datetime.now()
    
        B_DATE=str(Today.year)+'-'+str(Today.month)+'-'+str(Today.day)
        if Today.month==2:
            if Today.day+15 <= 28:
                Month=2
                Day=Today.day+15
                Year=Today.year
            else:
                Month=3
                Day=(Today.day+15) % 28
                Year=Today.year                
        elif Today.month==12:
            if Today.day+15 <=30:
                Month=12
                Day=Today.day+15
                Year=Today.year
            else:
                Month=1
                Day=(Today.day+15) % 30
                Year=Today.year+1
        else:
            if Today.day+15 <=30:
                Month=Today.month
                Day=Today.day+15
                Year=Today.year
            else:
                Today.month+1
                Day=(Today.day+15) % 30
                Year=Today.year
                
        D_DATE=str(Year)+'-'+str(Month)+'-'+str(Day)
        BOOK_ID=OKVBOOKID
                
        Values=(MEMBER_ID,B_NAME,B_SURNAME,B_DATE,D_DATE,BOOK_ID)
        sql="Insert into BORROW_TBL(MEMBER_ID,B_NAME,B_SURNAME,B_DATE,D_DATE,\
        BOOK_ID) \
        values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,Values)
        db.commit()
        
        Values=(MEMBER_ID,BOOK_ID,B_DATE)
        sql="Insert into Raporlar(MEMBER_ID,BOOK_ID,B_DATE) \
        values(%s,%s,%s)"
        mycursor.execute(sql,Values)
        db.commit()
        
    def OKVKapat(self):
        self.OKVEkrani.destroy()
        
    def OduncKitapVerme(self):
        self.OKVEkrani=tk.Toplevel(self.Officer_Screen)        
        self.OKVEkrani.title("ÖDÜNÇ KİTAP VERME EKRANI")
        self.OKVEkrani.geometry("500x650")
        self.OKVEkrani.transient(self.Officer_Screen)
        
        self.OKVInputFrame=tk.Frame(self.OKVEkrani)
        self.OKVInputFrame.grid(row=0,column=0)
        self.OKVButtonFrame=tk.Frame(self.OKVEkrani)
        self.OKVButtonFrame.grid(row=1,column=0)
        
        self.OKVUIDVar=tk.IntVar()
        self.OKVUID=tk.Label(self.OKVInputFrame,text="Üye ID",\
                           width=20)
        self.OKVUID.grid(row=0,column=0,sticky='nw')
        self.OKVUIDGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                    textvariable=self.OKVUIDVar)
        self.OKVUIDGiris.grid(row=0,column=1)
        
        self.OKVNameVar=tk.StringVar()
        self.OKVName=tk.Label(self.OKVInputFrame,text="Üye Adı",\
                             width=20)
        self.OKVName.grid(row=1,column=0,sticky='nw')
        self.OKVNameGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVNameVar,\
                                      state='disabled')
        self.OKVNameGiris.grid(row=1,column=1)
        
        self.OKVSurnameVar=tk.StringVar()
        self.OKVSurname=tk.Label(self.OKVInputFrame,text="Üye Soyadı",\
                             width=20)
        self.OKVSurname.grid(row=2,column=0,sticky='nw')
        self.OKVSurnameGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVSurnameVar,\
                                      state='disabled')
        self.OKVSurnameGiris.grid(row=2,column=1)
        
        self.OKVBDateVar=tk.StringVar()
        self.OKVBDate=tk.Label(self.OKVInputFrame,text="Üye D. Tarihi",\
                              width=20)
        self.OKVBDate.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.OKVBDateGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                       textvariable=self.OKVBDateVar,\
                                       state='disabled')
        self.OKVBDateGiris.grid(row=3,column=1)
        
        self.OKVBPlaceVar=tk.StringVar()
        self.OKVBPlace=tk.Label(self.OKVInputFrame,text="Üye D. Yeri",\
                             width=20)
        self.OKVBPlace.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.OKVBPlaceGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVBPlaceVar,\
                                      state='disabled')
        self.OKVBPlaceGiris.grid(row=4,column=1)
        
        self.OKVAddressVar=tk.StringVar()
        self.OKVAdress=tk.Label(self.OKVInputFrame,text="Üye Adresi",\
                                width=20)
        self.OKVAdress.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.OKVAddressGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                     textvariable=self.OKVAddressVar,\
                                     state='disabled')
        self.OKVAddressGiris.grid(row=5,column=1)
        
        self.OKVEMailVar=tk.StringVar()
        self.OKVEMail=tk.Label(self.OKVInputFrame,text="Üye E_Posta Adresi",\
                                width=20)
        self.OKVEMail.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.OKVEMailGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                         textvariable=self.OKVEMailVar,\
                                         state='disabled')
        self.OKVEMailGiris.grid(row=6,column=1)
        
        self.OKVTelNoVar=tk.StringVar()
        self.OKVTelNo=tk.Label(self.OKVInputFrame,text="Üye Tel. No.",\
                                width=20)
        self.OKVTelNo.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.OKVTelNoGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                         textvariable=self.OKVTelNoVar,\
                                         state='disabled')
        self.OKVTelNoGiris.grid(row=7,column=1)                        
        
        self.OKVKIDVar=tk.IntVar()
        self.OKVKID=tk.Label(self.OKVInputFrame,text="Kitap ID",\
                           width=20,foreground="magenta")
        self.OKVKID.grid(row=8,column=0,sticky='nw')
        self.OKVKIDGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                    textvariable=self.OKVKIDVar,
                                    foreground="magenta",state='disabled')
        self.OKVKIDGiris.grid(row=8,column=1)
        
        self.OKVISBNVar=tk.StringVar()
        self.OKVISBN=tk.Label(self.OKVInputFrame,text="Kitap ISBN",\
                             width=20,foreground="magenta")
        self.OKVISBN.grid(row=9,column=0,sticky='nw')
        self.OKVISBNGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVISBNVar,
                                      foreground="magenta",state='disabled')
        self.OKVISBNGiris.grid(row=9,column=1)
        
        self.OKVAuthVar=tk.StringVar()
        self.OKVAuth=tk.Label(self.OKVInputFrame,text="Kitap Author",\
                             width=20,foreground="magenta")
        self.OKVAuth.grid(row=10,column=0,sticky='nw')
        self.OKVAuthGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVAuthVar,
                                      foreground="magenta",state='disabled')
        self.OKVAuthGiris.grid(row=10,column=1)
        
        self.OKVTitleVar=tk.StringVar()
        self.OKVTitle=tk.Label(self.OKVInputFrame,text="Kitap Title",\
                              width=20,foreground="magenta")
        self.OKVTitle.grid(row=11,column=0,padx=3,pady=3,sticky="nw")
        self.OKVTitleGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                       textvariable=self.OKVTitleVar,
                                       foreground="magenta",state='disabled')
        self.OKVTitleGiris.grid(row=11,column=1)
        
        self.OKVSubjVar=tk.StringVar()
        self.OKVSubj=tk.Label(self.OKVInputFrame,text="Kitap Subject",\
                             width=20,foreground="magenta")
        self.OKVSubj.grid(row=12,column=0,padx=3,pady=3,sticky="nw")
        self.OKVSubjGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVSubjVar,
                                      foreground="magenta",state='disabled')
        self.OKVSubjGiris.grid(row=12,column=1)
        
        self.OKVPubYearVar=tk.IntVar()
        self.OKVPubYear=tk.Label(self.OKVInputFrame,text="Kitap Pub. Year",\
                                width=20,foreground="magenta")
        self.OKVPubYear.grid(row=13,column=0,padx=3,pady=3,sticky="nw")
        self.OKVPubYearGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                     textvariable=self.OKVPubYearVar,
                                     foreground="magenta",state='disabled')
        self.OKVPubYearGiris.grid(row=13,column=1)
        
        self.OKVPubCompVar=tk.StringVar()
        self.OKVPubComp=tk.Label(self.OKVInputFrame,text="Kitap Publisher",\
                                width=20,foreground="magenta")
        self.OKVPubComp.grid(row=14,column=0,padx=3,pady=3,sticky="nw")
        self.OKVPubCompGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                         textvariable=self.OKVPubCompVar,
                                         foreground="magenta",state='disabled')
        self.OKVPubCompGiris.grid(row=14,column=1)
        
        self.OKVEditionVar=tk.StringVar()
        self.OKVEdition=tk.Label(self.OKVInputFrame,text="Kitap Edition",\
                                width=20,foreground="magenta")
        self.OKVEdition.grid(row=15,column=0,padx=3,pady=3,sticky="nw")
        self.OKVEditionGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                         textvariable=self.OKVEditionVar,
                                         foreground="magenta",state='disabled')
        self.OKVEditionGiris.grid(row=15,column=1)
        
        self.OKVLangVar=tk.StringVar()
        self.OKVLang=tk.Label(self.OKVInputFrame,text="Kitap Language",\
                             width=20,foreground="magenta")
        self.OKVLang.grid(row=16,column=0,padx=3,pady=3,sticky="nw")
        self.OKVLangGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVLangVar,
                                      foreground="magenta",state='disabled')
        self.OKVLangGiris.grid(row=16,column=1)
        
        self.OKVShelfIDVar=tk.StringVar()
        self.OKVShelfID=tk.Label(self.OKVInputFrame,text="Kitap Shelf ID",\
                                width=20,foreground="magenta")
        self.OKVShelfID.grid(row=17,column=0,padx=3,pady=3,sticky="nw")
        self.OKVShelfIDGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                      textvariable=self.OKVShelfIDVar,
                                      foreground="magenta",state='disabled')
        self.OKVShelfIDGiris.grid(row=17,column=1)
                      
        self.OKVPubLocVar=tk.StringVar()
        self.OKVPubLoc=tk.Label(self.OKVInputFrame,text="Kitap Pub. Location",\
                               width=20,foreground="magenta")
        self.OKVPubLoc.grid(row=18,column=0,padx=3,pady=3,sticky="nw")
        self.OKVPubLocGiris=tk.Entry(self.OKVInputFrame,width=50,\
                                       textvariable=self.OKVPubLocVar,
                                       foreground="magenta",state='disabled')
        self.OKVPubLocGiris.grid(row=18,column=1)
        
        self.OKVUAra=tk.Button(self.OKVButtonFrame,text="Üye Listele",\
                       bg="lightgreen",command=self.OKVUyeAraListele,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.OKVUAra.grid(row=0,column=0)
        
        self.OKVKitapAra=tk.Button(self.OKVButtonFrame,text="Kitap Listele",\
                       bg="lightgreen",command=self.OKVKitapAraListele,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'),state="disabled")        
        self.OKVKitapAra.grid(row=0,column=1)
        
        self.OKVOduncVer=tk.Button(self.OKVButtonFrame,text="Ödünç Ver",\
                       bg="lightgreen",command=self.OKVKitabiOduncVer,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'),state="disabled")        
        self.OKVOduncVer.grid(row=0,column=2)
        
        self.OKVCikis=tk.Button(self.OKVButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.OKVKapat,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.OKVCikis.grid(row=0,column=3)  
        
        
    
class UyeIslemleri(object):
    def __init__(self):
        self.Uye_Screen=tk.Toplevel(root)
        self.Uye_Screen.title("UYE İSLEM EKRANI")
        self.Uye_Screen.geometry("600x300")
        self.Uye_Screen.transient(root)
        
        self.KitapAra=tk.Button(self.Uye_Screen,text="Kitap İşlemleri", width=40, height=18,relief="ridge", command=self.KitapArama)
   
        self.KitapVar=tk.Button(self.Uye_Screen,text="Hangi Kitaplara Sahibim", width=40, height=18, bg="yellow",relief="ridge", command=self.Sahibim) 
 
        self.KitapAra.grid(row=0,column=0,padx=2,pady=3,sticky="w")

        self.KitapVar.grid(row=0,column=1,padx=2,pady=3,sticky="w")
   
    def OduncAraListele(self):    
        OKID=self.OKIDDVar.get()
        OKName=self.OKNameVar.get()
        OKSurname=self.OKSurnameVar.get()

        
        Values=()
        Cond_Check=False # Check if a condition is aready added
        sql="SELECT * FROM BORROW_TBL WHERE"
        if OKID!=0:
            if Cond_Check==True:
                sql=sql+" AND MEMBER_ID=%s "
            else:
                sql=sql+" MEMBER_ID=%s "
                Cond_Check=True
            Values+=(OKID,)
        if OKName!='':
            if Cond_Check==True:
                sql=sql+" AND B_NAME=%s "
            else:
                sql=sql+" B_NAME=%s "
                Cond_Check=True
            Values+=(OKName,)
        if OKSurname!='':
            if Cond_Check==True:
                sql=sql+" AND B_SURNAME=%s "
            else:
                sql=sql+" B_SURNAME=%s "
                Cond_Check=True
            Values+=(OKSurname,)
       
                                
        print(Values)
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    

                    
    def SOKapat(self):
        self.SahipOlduklarımEkrani.destroy()


    def YeniOduncAramaGiris(self):
        self.OKIDDVar.set(0)
        self.OKNameVar.set("")
        self.OKSurnameVar.set("")
   
      
    def Sahibim(self):
        self.SahipOlduklarımEkrani=tk.Toplevel(self.Uye_Screen)        
        self.SahipOlduklarımEkrani.title("ÖDÜNÇ ARAMA EKRANI")
        self.SahipOlduklarımEkrani.geometry("500x450")
        self.SahipOlduklarımEkrani.transient(self.Uye_Screen)
        
        self.SOInputFrame=tk.Frame(self.SahipOlduklarımEkrani)
        self.SOInputFrame.grid(row=0,column=0)
        self.UAButtonFrame=tk.Frame(self.SahipOlduklarımEkrani)
        self.UAButtonFrame.grid(row=1,column=0)
        
        self.OKIDDVar=tk.IntVar()
        self.OKID=tk.Label(self.SOInputFrame,text="Üye ID",\
                           width=20)
        self.OKID.grid(row=0,column=0,sticky='nw')
        self.OKIDGiris=tk.Entry(self.SOInputFrame,width=50,\
                                    textvariable=self.OKIDDVar)
        self.OKIDGiris.grid(row=0,column=1)
        
        self.OKNameVar=tk.StringVar()
        self.OKName=tk.Label(self.SOInputFrame,text="Üye Adı",\
                             width=20)
        self.OKName.grid(row=1,column=0,sticky='nw')
        self.OKNameGiris=tk.Entry(self.SOInputFrame,width=50,\
                                      textvariable=self.OKNameVar)
        self.OKNameGiris.grid(row=1,column=1)

        self.OKSurnameVar=tk.StringVar()
        self.OKSurname=tk.Label(self.SOInputFrame,text="Üye Soyadı",\
                             width=20)
        self.OKSurname.grid(row=2,column=0,sticky='nw')
        self.OKSurnameGiris=tk.Entry(self.SOInputFrame,width=50,\
                                      textvariable=self.OKSurnameVar)
        self.OKSurnameGiris.grid(row=2,column=1)       

        
        self.BAra=tk.Button(self.UAButtonFrame,text="Ara",\
                       bg="lightgreen",command=self.OduncAraListele,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.BAra.grid(row=4,column=0)
        
        self.UAYeniGiris=tk.Button(self.UAButtonFrame,text="Yeni Arama",\
                       bg="lightgreen",command=self.YeniOduncAramaGiris,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UAYeniGiris.grid(row=4,column=1)
        
        self.UACikis=tk.Button(self.UAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.SOKapat,\
                       relief="raised",borderwidth=8,width=12,\
                       font=('Helvetica', '10'))        
        self.UACikis.grid(row=4,column=2)            
     
    
    def KitapAraListele(self):
        KAID=self.KAIDVar.get()
        KAISBN=self.KAISBNVar.get()
        KAAuth=self.KAAuthVar.get()
        KATitle=self.KATitleVar.get()
        KASubj=self.KASubjVar.get()
        KAPubYear=self.KAPubYearVar.get()
        KAPubComp=self.KAPubCompVar.get()
        KAEdition=self.KAEditionVar.get()
        KALang=self.KALangVar.get()
        KAShelfID=self.KAShelfIDVar.get()
        KAPubLoc=self.KAPubLocVar.get()
        
        Values=()
        Cond_Check=False # Check if a condition is aready added
        sql="SELECT * FROM BOOKS_TBL WHERE"
        if KAID!=0:
            sql=sql+" BOOK_ID=%s "
            Values=Values+(KAID,)
            Cond_Check=True
        if KAISBN!='':
            if Cond_Check==True:
                sql=sql+" AND ISBN=%s "
            else:
                sql=sql+" ISBN=%s "
                Cond_Check=True
            Values+=(KAISBN,)
        if KAAuth!='':
            if Cond_Check==True:
                sql=sql+" AND AUTHOR=%s "
            else:
                sql=sql+" AUTHOR=%s "
                Cond_Check=True
            Values+=(KAAuth,)
        if KATitle!='':
            if Cond_Check==True:
                sql=sql+" AND TITLE=%s "
            else:
                sql=sql+" TITLE=%s "
                Cond_Check=True
            Values+=(KATitle,)
        if KASubj!='':
            if Cond_Check==True:
                sql=sql+" AND SUBJECT=%s "
            else:
                sql=sql+" SUBJECT=%s "
                Cond_Check=True
            Values+=(KASubj,)
        if KAPubYear!=0:
            if Cond_Check==True:
                sql=sql+" AND PUB_YEAR=%s "
            else:
                sql=sql+" PUB_YEAR=%s "
                Cond_Check=True
            Values+=(KAPubYear,)
        if KAPubComp!='':
            if Cond_Check==True:
                sql=sql+" AND PUBLISHER=%s "
            else:
                sql=sql+" PUBLISHER=%s "
                Cond_Check=True
            Values+=(KAPubComp,)
        if KAEdition!='':
            if Cond_Check==True:
                sql=sql+" AND EDITION=%s "
            else:
                sql=sql+" EDITION=%s "
                Cond_Check=True
            Values+=(KAEdition,)
        if KALang!='':
            if Cond_Check==True:
                sql=sql+" AND LANG=%s "
            else:
                sql=sql+" LANG=%s "
                Cond_Check=True
            Values+=(KALang,)
        if KAShelfID!='':
            if Cond_Check==True:
                sql=sql+" AND SHELF_ID=%s "
            else:
                sql=sql+" SHELF_ID=%s "
                Cond_Check=True
            Values+=(KAShelfID,)
        if KAPubLoc!='':
            if Cond_Check==True:
                sql=sql+" AND PUB_LOC=%s "
            else:
                sql=sql+" PUB_LOC=%s "
                Cond_Check=True
            Values+=(KAPubLoc,)
                                
        print(Values)
        print(sql)
        
        mycursor.execute(sql,Values)
        data=mycursor.fetchall()
        print(data)
    
    def KAYeniAramaGiris(self):
        self.KAIDVar.set(0)
        self.KAISBNVar.set("")
        self.KAAuthVar.set("")
        self.KATitleVar.set("")
        self.KASubjVar.set("")
        self.KAPubYearVar.set(0)
        self.KAPubCompVar.set("")
        self.KAEditionVar.set("")
        self.KALangVar.set("")
        self.KAShelfIDVar.set("")
        self.KAPubLocVar.set("")
            
    def KAKapat(self):
        self.KitapAramaEkrani.destroy()
        
    def KitapArama(self):
        self.KitapAramaEkrani=tk.Toplevel(self.Uye_Screen)        
        self.KitapAramaEkrani.title("KİTAP ARAMA EKRANI")
        self.KitapAramaEkrani.geometry("500x450")
        self.KitapAramaEkrani.transient(self.Uye_Screen)
        
        self.KAInputFrame=tk.Frame(self.KitapAramaEkrani)
        self.KAInputFrame.grid(row=0,column=0)
        self.KAButtonFrame=tk.Frame(self.KitapAramaEkrani)
        self.KAButtonFrame.grid(row=1,column=0)
        
        self.KAIDVar=tk.IntVar()
        self.KAID=tk.Label(self.KAInputFrame,text="Kitap ID",\
                           width=20)
        self.KAID.grid(row=0,column=0,sticky='nw')
        self.KAIDGiris=tk.Entry(self.KAInputFrame,width=50,\
                                    textvariable=self.KAIDVar)
        self.KAIDGiris.grid(row=0,column=1)
        
        self.KAISBNVar=tk.StringVar()
        self.KAISBN=tk.Label(self.KAInputFrame,text="Kitap ISBN",\
                             width=20)
        self.KAISBN.grid(row=1,column=0,sticky='nw')
        self.KAISBNGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAISBNVar)
        self.KAISBNGiris.grid(row=1,column=1)
        
        self.KAAuthVar=tk.StringVar()
        self.KAAuth=tk.Label(self.KAInputFrame,text="Kitap Author",\
                             width=20)
        self.KAAuth.grid(row=2,column=0,sticky='nw')
        self.KAAuthGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAAuthVar)
        self.KAAuthGiris.grid(row=2,column=1)
        
        self.KATitleVar=tk.StringVar()
        self.KATitle=tk.Label(self.KAInputFrame,text="Kitap Title",\
                              width=20)
        self.KATitle.grid(row=3,column=0,padx=3,pady=3,sticky="nw")
        self.KATitleGiris=tk.Entry(self.KAInputFrame,width=50,\
                                       textvariable=self.KATitleVar)
        self.KATitleGiris.grid(row=3,column=1)
        
        self.KASubjVar=tk.StringVar()
        self.KASubj=tk.Label(self.KAInputFrame,text="Kitap Subject",\
                             width=20)
        self.KASubj.grid(row=4,column=0,padx=3,pady=3,sticky="nw")
        self.KASubjGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KASubjVar)
        self.KASubjGiris.grid(row=4,column=1)
        
        self.KAPubYearVar=tk.IntVar()
        self.KAPubYear=tk.Label(self.KAInputFrame,text="Kitap Pub. Year",\
                                width=20)
        self.KAPubYear.grid(row=5,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubYearGiris=tk.Entry(self.KAInputFrame,width=50,\
                                     textvariable=self.KAPubYearVar)
        self.KAPubYearGiris.grid(row=5,column=1)
        
        self.KAPubCompVar=tk.StringVar()
        self.KAPubComp=tk.Label(self.KAInputFrame,text="Kitap Publisher",\
                                width=20)
        self.KAPubComp.grid(row=6,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubCompGiris=tk.Entry(self.KAInputFrame,width=50,\
                                         textvariable=self.KAPubCompVar)
        self.KAPubCompGiris.grid(row=6,column=1)
        
        self.KAEditionVar=tk.StringVar()
        self.KAEdition=tk.Label(self.KAInputFrame,text="Kitap Edition",\
                                width=20)
        self.KAEdition.grid(row=7,column=0,padx=3,pady=3,sticky="nw")
        self.KAEditionGiris=tk.Entry(self.KAInputFrame,width=50,\
                                         textvariable=self.KAEditionVar)
        self.KAEditionGiris.grid(row=7,column=1)
        
        self.KALangVar=tk.StringVar()
        self.KALang=tk.Label(self.KAInputFrame,text="Kitap Language",\
                             width=20)
        self.KALang.grid(row=8,column=0,padx=3,pady=3,sticky="nw")
        self.KALangGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KALangVar)
        self.KALangGiris.grid(row=8,column=1)
        
        self.KAShelfIDVar=tk.StringVar()
        self.KAShelfID=tk.Label(self.KAInputFrame,text="Kitap Shelf ID",\
                                width=20)
        self.KAShelfID.grid(row=9,column=0,padx=3,pady=3,sticky="nw")
        self.KAShelfIDGiris=tk.Entry(self.KAInputFrame,width=50,\
                                      textvariable=self.KAShelfIDVar)
        self.KAShelfIDGiris.grid(row=9,column=1)
                      
        self.KAPubLocVar=tk.StringVar()
        self.KAPubLoc=tk.Label(self.KAInputFrame,text="Kitap Pub. Location",\
                               width=20)
        self.KAPubLoc.grid(row=11,column=0,padx=3,pady=3,sticky="nw")
        self.KAPubLocGiris=tk.Entry(self.KAInputFrame,width=50,\
                                       textvariable=self.KAPubLocVar)
        self.KAPubLocGiris.grid(row=11,column=1)
        
        self.KAAra=tk.Button(self.KAButtonFrame,text="Kitap Ara",\
                       bg="lightgreen",command=self.KitapAraListele,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAAra.grid(row=0,column=0)
        
        self.KAYeniGiris=tk.Button(self.KAButtonFrame,text="Yeni Arama",\
                       bg="lightgreen",command=self.KAYeniAramaGiris,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KAYeniGiris.grid(row=0,column=1)
        
        self.KACikis=tk.Button(self.KAButtonFrame,text="Çıkış",\
                       bg="lightgreen",command=self.KAKapat,\
                       relief="raised",borderwidth=8,width=17,\
                       font=('Helvetica', '10'))        
        self.KACikis.grid(row=0,column=2)
    
    
        


db=mysql.connect(host="localhost",
                 user="root",
                 passwd="43361710")

mycursor=db.cursor(buffered=True)

# Create a database
mycursor.execute("CREATE DATABASE  IF NOT EXISTS LIBRARY_MNGMNT")
mycursor.execute("USE LIBRARY_MNGMNT")

mycursor.execute("SET GLOBAL sql_mode=''")

sql="""CREATE TABLE IF NOT EXISTS BOOKS_TBL (
BOOK_ID INT(10) NOT NULL PRIMARY KEY, 
ISBN VARCHAR(13), 
AUTHOR VARCHAR(20) NOT NULL, 
TITLE VARCHAR(40) NOT NULL, 
SUBJECT VARCHAR(20) NOT NULL, 
PUB_YEAR INT(4) NOT NULL, 
PUBLISHER VARCHAR(20) NOT NULL, 
EDITION VARCHAR(10), 
LANG VARCHAR(15), 
SHELF_ID VARCHAR(15),
COV_IMG VARCHAR(50),
PUB_LOC VARCHAR(20))"""

mycursor.execute(sql)
db.commit()

sql="""CREATE TABLE IF NOT EXISTS BORROW_TBL (
BOOK_ID INT(10) NOT NULL PRIMARY KEY,
B_NAME VARCHAR(20) NOT NULL, 
B_SURNAME VARCHAR(20) NOT NULL,
B_DATE VARCHAR(15) NOT NULL,
D_DATE VARCHAR(15) NOT NULL,
MEMBER_ID INT(10))"""

mycursor.execute(sql)
db.commit()

sql="""CREATE TABLE IF NOT EXISTS MEMBERS_TBL (
MEMBER_ID INT(10) NOT NULL PRIMARY KEY, 
M_NAME VARCHAR(20) NOT NULL,
M_SURNAME VARCHAR(20) NOT NULL,
B_DATE VARCHAR(15) NOT NULL,
B_PLACE VARCHAR(15) NOT NULL,
ADRESS VARCHAR(50) NOT NULL,
E_MAIL VARCHAR(30),
TEL_NO VARCHAR(20) NOT NULL)"""

mycursor.execute(sql)
db.commit()

sql="""CREATE TABLE IF NOT EXISTS YasakliKullanici (
MEMBER_ID INT(10) NOT NULL PRIMARY KEY, 
M_NAME VARCHAR(20) NOT NULL,
M_SURNAME VARCHAR(20) NOT NULL,
B_DATE VARCHAR(15) NOT NULL,
B_PLACE VARCHAR(15) NOT NULL,
ADRESS VARCHAR(50) NOT NULL,
E_MAIL VARCHAR(30),
TEL_NO VARCHAR(20) NOT NULL)"""

mycursor.execute(sql)
db.commit()

sql="""CREATE TABLE IF NOT EXISTS Raporlar (
OFFICER_ID INT(10) NOT NULL PRIMARY KEY, 
O_NAME VARCHAR(20) NOT NULL,
O_SURNAME VARCHAR(20) NOT NULL,
BOOK_ID INT(10) NOT NULL,
B_DATE VARCHAR(15) NOT NULL)"""

mycursor.execute(sql)
db.commit()




def Login_Successful_OpenWindow():
    Login_success_screen.destroy()
    Account_Screen.destroy()
    if "Admin" in Account_Type:
        Admin_Islemleri()
    elif "Officer" in Account_Type:
        officerIslemleri()
    elif "Uye" in Account_Type:
        UyeIslemleri()
    else:
        print("Tip tanımı yanlış!")
    

def Delete_password_not_recognised():
    Password_not_recog_screen.destroy()
    
def Delete_user_not_found_screen():
    User_not_found_screen.destroy()    


def Login_Successful():
    global Login_success_screen
    Login_success_screen = tk.Toplevel(Account_Screen)
    Login_success_screen.title("Success")
    Login_success_screen.geometry("150x100")
    tk.Label(Login_success_screen, text="Login Success").pack()
    tk.Button(Login_success_screen, text="OK",command=Login_Successful_OpenWindow).pack()

def Password_not_recognised():
    global Password_not_recog_screen
    Password_not_recog_screen = tk.Toplevel(Account_Screen)
    Password_not_recog_screen.title("Failure")
    Password_not_recog_screen.geometry("150x100")
    tk.Label(Password_not_recog_screen, text="Invalid Password ").pack()
    tk.Button(Password_not_recog_screen, text="OK", command=Delete_password_not_recognised).pack()

def User_not_found():
    global User_not_found_screen
    User_not_found_screen = tk.Toplevel(Account_Screen)
    User_not_found_screen.title("Failure")
    User_not_found_screen.geometry("150x100")
    tk.Label(User_not_found_screen, text="User Not Found").pack()
    tk.Button(User_not_found_screen, text="OK", command=Delete_user_not_found_screen).pack()


def Login_Verify():
    global Access_Right
    global Account_Type
    global Username
    
    Username = Username_Verify.get()
    Password = Password_Verify.get()
    Username_login_entry.delete(0, "end")
    Password_login_entry.delete(0, "end")

    List_of_files = os.listdir()
    if Username+".txt" in List_of_files:
        File = open(Username+".txt", "r")
        Verify = File.read().splitlines()
        Access_Right=Verify[2]
        Account_Type=Verify[3]
        if "False" in Access_Right:
            pass
        elif Password in Verify[1]:
            Login_Successful()
        else:
            Password_not_recognised()
    else:
        User_not_found()
        
def SystemLogin():    
    global Account_Screen
    Account_Screen=tk.Toplevel(root)
    Account_Screen.geometry("300x250")
    Account_Screen.title("Account Login")
    Account_Screen.transient(root)
    
    global Username_Verify
    global Password_Verify
    
    Username_Verify = tk.StringVar()
    Password_Verify = tk.StringVar()

    global Username_login_entry
    global Password_login_entry

    tk.Label(Account_Screen, text="Username * ").pack()
    Username_login_entry = tk.Entry(Account_Screen, textvariable=Username_Verify)
    Username_login_entry.pack()
    tk.Label(Account_Screen, text="").pack()
    tk.Label(Account_Screen, text="Password * ").pack()
    Password_login_entry = tk.Entry(Account_Screen, textvariable=Password_Verify, show= '*')
    Password_login_entry.pack()
    tk.Label(Account_Screen, text="").pack()
    tk.Button(Account_Screen, text="Login", width=10, height=1,command = Login_Verify).pack()

    
# Add introductory page
root = tk.Tk()
root.title('WELCOME TO BLGM416 LIBRARY')

root.geometry("375x475")
# Enter the path of image file.
Image_path="C:\Kütüphane Sistemi\Lib_Background_Image.gif"  
Photo = tk.PhotoImage(file=Image_path,master=root)
w = Photo.width()
h = Photo.height()
root.geometry("%dx%d+0+0" % (w, h))

Lbl = tk.Label(root, image=Photo)
Lbl.image = Photo
Lbl.pack(side='top', fill='both', expand='yes')

Login_Button=tk.Button(root,text="LOGIN",command=SystemLogin,\
                       relief="raised",borderwidth=8)
Login_Button.place(x = w-100, y =h-100 , width=100, height=100)
root.mainloop()
































