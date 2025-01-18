import tkinter 
from PIL import Image, ImageTk
import itertools
from tkinter import messagebox
def Hesapla():
    try:
        weight = float(enter1.get())
        height = float(enter2.get())
        if weight < 0 or height < 0:
            raise ValueError("Geçerli bir değer giriniz")
        bmi = weight / (height ** 2)
        kategori = ""
        if bmi < 18.5:
            kategori = "Zayıf Kategorisinde"
        elif 18.5 <= bmi < 24.9:
            kategori = "Normal Kategoride"
        elif 25 <= bmi < 29.9:
            kategori = "Fazla Kilolu Kategorisinde"
        else:
            kategori = "Obez Kategorisinde"
        result_label.config(text=f"BMI sonucu: {bmi:.2f} ({kategori})")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!") 
window = tkinter.Tk()
window.title("BMI Hesaplama")
window.minsize(width="500", height="500")
window.config(bg="#1a1a2e")
window.resizable(0,0) # kullancının tam ekan yapmasını engelledim.
label0 = tkinter.Label(text="")
label0.pack()
label00 = tkinter.Label(text="")
label0.config(bg="#1a1a2e")
label00.config(bg="#1a1a2e")
label00.pack()
Label1= tkinter.Label(text="Lütfen kilonuzu giriniz(kg)" ,borderwidth=2, relief="ridge",font=("Helvetica", 14, "bold"))
Label1.config(padx=20,pady=10)
Label1.config(bg="#16213e", fg="white")  
Label1.pack()
enter1= tkinter.Entry(window, font = ("ariel", 14))
enter1.pack(padx=10,pady=10)
Label2 =tkinter.Label(text="Lütfen boyunuzu giriniz(m)" ,borderwidth=2, relief="ridge",font=("Helvetica", 14, "bold"))
Label2.config(padx=20,pady=10)
Label2.config(bg="#16213e", fg="white")
Label2.pack()
enter2= tkinter.Entry(window, font = ("ariel", 14))
enter2.pack(padx=10,pady=10)
buton1=tkinter.Button(text="Hesaplama", bg="#4CAF50", activebackground="#45a049", activeforeground="white", command=Hesapla) 
buton1.config(padx=10, pady=10, bg="#f0f0f0")
buton1.pack()
labels=tkinter.Label(text=" ")
labels.config(bg="#1a1a2e")
labels.pack()
labelsx=tkinter.Label(text=" ")
labelsx.config(bg="#1a1a2e")
labelsx.pack()
result_label = tkinter.Label(window , font=("Helvetica", 14, "bold"))
result_label.config(bg="#1a1a2e")
result_label.pack(pady=10)
labelsxx=tkinter.Label(text="")
labelsxx.config(bg="#1a1a2e")
#görsel
image = Image.open("/Users/aliemirsertbas/Desktop/VSCO1prjct/personalPrjct/tkinter/ımage/new2.webp")
new_width = 500
new_height = 300
resized_image = image.resize((new_width, new_height))
gif = ImageTk.PhotoImage(resized_image)
label3 = tkinter.Label(window, image=gif)
label3.config(padx=30, pady=20)
label3.pack(side="top")
label3.config(bg="#1a1a2e")
window.mainloop()