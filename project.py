from tkinter import *
from random import *
from PIL import ImageGrab



class Root(Tk):
    def save_rezult(self):
        if self.indikator[0] > 0 and self.indikator[1] > 0:
            ss_region = (300, 0, 1200, 600)
            ss_img = ImageGrab.grab(ss_region)
            ss_img.save(f"{self.word.get()} {randint(0,9999999)}.jpg")
            self.indikator = [0,0,0]
            self.clear()
            self.TXT.config(text = 'Файл збережено. Перевірте папку')
            self.insert.delete(0, END)
        else:
            self.TXT.config(text = 'Немає данних для збереження')
    def clearAll(self):
        self.indikator = [0,0,0]
        self.insert.delete(0, END)
        self.TXT.config(text = '')
        self.clear()
    def myIndicator(self):
        
        if len(self.word.get()) <= 5:
            self.indikator[0] = 50
            self.indikator[1] = 200
        elif len(self.word.get()) <= 10:
            self.indikator[0] = 40            
            self.indikator[1] = 100
        elif len(self.word.get()) <= 15:
            self.indikator[0] = 15
            self.indikator[1] = 50
        elif len(self.word.get()) <= 20:
            self.indikator[0] = 4
            self.indikator[1] = 30
        elif len(self.word.get()) <= 25:
            self.indikator[0] = 2
            self.indikator[1] = 10
        elif len(self.word.get()) > 25:
            self.indikator[0] = 0
            self.indikator[1] = 0
            self.TXT.config(text = 'Велика кількість символів > 26', fg = 'red')
            self.after(100, self.clear)
            
    
    def return_goodtxt456_fromSmall(self, word):
        hight = 20
        littleArr = []
        backArr = []
        if self.way == 1:
            for part in range (len(word)):            
                littleArr = [hight*(len(word) - part), word[part]]
                backArr.append(littleArr)
        else:
            for part in range (len(word)):            
                littleArr = [hight*(part+1), word[part]]
                backArr.append(littleArr)            
        return backArr
    
    def return_row (self, bigarr):
        rowLastPoint = self.lastPoint - 20
        hight_row = self.lastPoint - 50 - bigarr[0] - self.indikator[1]
        p = self.lastStep+30
        point = [self.lastStep,hight_row,self.lastStep,rowLastPoint,p,rowLastPoint,p,hight_row,bigarr[1]]
        self.lastStep = p + self.indikator[0]
        return point
    def clear(self):
        self.placew.delete("all")
        self.lastStep = 10
        self.firstPoint = 10        
    def create_row(self,d):       
        self.placew.create_polygon(d[0], d[1], d[2], d[3],d [4], d[5],d[6],d[7], fill=f'#{randint(100,999)}')
        self.placew.create_text(d[0]+15,d[1] - 20,fill="darkblue",font="Times 14",text=f"{d[8]}")
    def show(self,way):        
        self.way = way
        txt456 = self.word.get()
        self.TXT.config(text = f'{txt456} - {len(txt456)} с.', fg = 'black')                
        self.myIndicator()
        self.clear()
        goodtxt456 = self.return_goodtxt456_fromSmall(txt456)
        shuffle(goodtxt456)
        for z in range(len(goodtxt456)):
            start = self.return_row(goodtxt456[z])
            self.create_row(start)
    def __init__(self):
        super().__init__()
        self.lastStep = 10
        self.firstPoint = int(10)
        self.lastPoint = 600
        self.word = StringVar()
        self.indikator = [0,0,0]
        self.placew = Canvas(width = 890, height=self.lastPoint, bg='white')
        self.placew.place(x=300,y= 0)
        self.head = Label(font="Times 14", text = 'Введіть слово або словосполучення')
        self.head.place(x=5,y=20)
        self.insert = Entry(textvariable=self.word, font = "Times 14", width = 30)
        self.insert.place(x=10,y=50)
        self.btnInser = Button(text = 'Намалювати від великого до малого', command=lambda: self.show(1))
        self.btnInser.place(x=10, y=150)
        self.btnInser = Button(text = 'Намалювати від малого до великого', command=lambda: self.show(2))
        self.btnInser.place(x=10, y=200)
        self.btnClear = Button(text = 'Очистити',bg='#3a3afa',fg='white', command=self.clear)
        self.btnClear.place(x=10, y=250)
        self.btnClearAll = Button(text = 'Очистити все',bg='#3a3afa',fg='white', command=self.clearAll)
        self.btnClearAll.place(x=80, y=250)
        self.btnSave = Button(text = 'Зберегти',bg='#888',fg='white', command=self.save_rezult)
        self.btnSave.place(x=10, y=300)
        self.TXT = Label(font="Times 14")
        self.TXT.place(x=10,y=100) 
        txtError = 'Максимальна кількість символів у слові - 25'
        error_long_text = Label(text = txtError, font="Times 24", fg="darkblue")
        error_long_text.place(x=300, y=600)
        exitB = Button(text='Завершити роботу',bg='#588',fg='white', command = lambda: Root.destroy(self))
        exitB.place(x=10, y=600)
root = Root()
w = 1200 #w = root.winfo_screenwidth()
h = 700 #h = root.winfo_screenheight()
root.geometry(f'{w}x{h}+0+0')
root.overrideredirect(True)#Ховає верх
root.mainloop()



