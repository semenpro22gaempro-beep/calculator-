
import customtkinter as CTk
import os
import sys


current_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_path, "calculator.ico")

root = CTk.CTk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Проверяем, существует ли файл, чтобы программа не вылетала с ошибкой
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print(f"Ошибка: Файл {icon_path} не найден!")

# Настройка темы
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")

root = CTk.CTk()
root.geometry("570x400")
root.title("Physics Calculator")
root.iconbitmap("C:/physic/calculator.ico")

tabview = CTk.CTkTabview(root, width=500, height=400)
tabview.grid(row = 0, column=0, padx=0, pady=(1, 0), sticky="nsew")

tab_doc = tabview.add("Калькулятор")
tab_grv = tabview.add("Сила тяжести")
tab_wpr = tabview.add("Давление воды")
tab_gyk = tabview.add("Закон Гука")
tab_slf = tabview.add("Давление тела")
tab_spd = tabview.add("Скорость")

# шрифты
font1 = ("Helvetica", 18 ,"bold")



# --- Настройка веса колонок для центрирования ---
for tab in [tab_doc, tab_grv, tab_wpr, tab_gyk, tab_slf, tab_spd]:
    tab.grid_columnconfigure(200, weight=220)

# --- ФУНКЦИИ С ЗАЩИТОЙ ОТ ОШИБОК ---

def grv():
    try:
        val = en_grv.get()
        num = float(val)
        res = num * 9.81
        lab_grv.configure(text=f"Результат: {res:.2f} H", text_color="white")
    except ValueError:
        lab_grv.configure(text="Введите число!", text_color="red")

def wpr():
    try:
        val1 = en_wpr.get()
        val2 = en2_wpr.get()
        num1 = float(val1)
        num2 = float(val2)
        res = num1 * num2 * 9.81
        lab_wpr.configure(text=f"Результат: {res:.2f} Па", text_color="white")
    except ValueError:
        lab_wpr.configure(text="Введите числа!", text_color="red")

def gyk():
    try:
        val1 = en_gyk.get()
        val2 = en2_gyk.get()
        num1 = float(val1)
        num2 = float(val2)
        res = num1 * num2
        lab_gyk.configure(text=f"Результат: {res:.2f} H", text_color="white")
    except ValueError:
        lab_gyk.configure(text="Введите числа!", text_color="red")

def slf():
    try:
        val1 = en_slf.get()
        val2 = en2_slf.get()
        num1 = float(val1)
        num2 = float(val2)
        res = num1 / num2
        lab_slf.configure(text=f"Результат: {res:.2f} ПА", text_color="white")
    except ValueError:
        lab_slf(text="Введите числа!", text_color="red")

def spd():
    try:
        val1 = en_spd.get()
        val2 = en2_spd.get()
        num1 = float(val1)
        num2 = float(val2)
        res = num1 / num2 
        lab_spd.configure(text=f"Результат: {res:.2f} м/с", text_color="white")
    except ValueError:
        lab_slf(text="Введите числа!", text_color="red")
    

# --- ИНТЕРФЕЙС ГРУ (Сила тяжести) ---
en_grv = CTk.CTkEntry(tab_grv, width=250, placeholder_text="Введите массу (кг)", height=50, font=font1)
en_grv.grid(row=0, column=0, padx=10, pady=20)

btn_grv = CTk.CTkButton(tab_grv, text="Рассчитать", command=grv, height=50, width=250, font=font1)
btn_grv.grid(row=1, column=0, padx=10, pady=10)

lab_grv = CTk.CTkLabel(tab_grv, text="", font=font1)
lab_grv.grid(row=0, column=1, padx=10, pady=10)

# --- ИНТЕРФЕЙС WPR (Давление воды) ---
en_wpr = CTk.CTkEntry(tab_wpr, width=250, placeholder_text="Высота (h, м)", height=50, font=font1)
en_wpr.grid(row=0, column=0, padx=10, pady=10)

en2_wpr = CTk.CTkEntry(tab_wpr, width=250, placeholder_text="Плотность (ρ, кг/м³)", height=50, font=font1)
en2_wpr.grid(row=1, column=0, padx=10, pady=10)

btn_wpr = CTk.CTkButton(tab_wpr, text="Рассчитать", command=wpr, height=50, width=250, font=font1)
btn_wpr.grid(row=2, column=0, padx=10, pady=10)

lab_wpr = CTk.CTkLabel(tab_wpr, text="", font=font1)
lab_wpr.grid(row=0, column=1, padx=10, pady=10)

# --- ИНТЕРФЕЙС DOC (Справка) ---
my_font = CTk.CTkFont(family="Arial", size=24, weight="bold")

Lab_doc = CTk.CTkLabel(tab_doc, text="Привет!", font=my_font)
Lab_doc.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

lab_doc2 = CTk.CTkLabel(tab_doc, text="Это мой калькулятор по физике", font=("Arial", 24))
lab_doc2.grid(row=1, column=0, padx=20, pady=2, sticky="w")

lab_doc3 = CTk.CTkLabel(tab_doc, text="Формулы: P = ρgh, F = mg, Fупр = kΔl", font=("Arial", 22, "italic"))
lab_doc3.grid(row=2, column=0, padx=20, pady=10, sticky="w")

# --- ИНТЕРФЕЙС GYK (Закон Гука) ---
en_gyk = CTk.CTkEntry(tab_gyk, width=250, placeholder_text="Коэффициент жесткости (k, Н/м)", height=50, font=font1)
en_gyk.grid(row=0, column=0, padx=10, pady=10)

en2_gyk = CTk.CTkEntry(tab_gyk, width=250, placeholder_text="Деформация (Δl, м)", height=50, font=font1)
en2_gyk.grid(row=1, column=0, padx=10, pady=10)

btn_gyk = CTk.CTkButton(tab_gyk, text="Рассчитать", command=gyk, height=50, width=250, font=font1)
btn_gyk.grid(row=2, column=0, padx=10, pady=10)

lab_gyk = CTk.CTkLabel(tab_gyk, text="", font=font1, height=50, width=250)
lab_gyk.grid(row=0, column=1, padx=10, pady=10)

# slf 

en_slf = CTk.CTkEntry(tab_slf, width=250, placeholder_text="Введите силу(H)", height=50, font=font1)
en_slf.grid(row = 0, column=0, padx=10, pady=10)

en2_slf = CTk.CTkEntry(tab_slf, width=250, placeholder_text="Введите площадь(M2)", height=50, font=font1)
en2_slf.grid(row = 1, column=0, padx=10, pady=10)

btn_slf = CTk.CTkButton(tab_slf, width=250, text="Рассчитать", command=slf, height=50, font=font1)
btn_slf.grid(row=2, column=0, padx=10, pady=10)

lab_slf = CTk.CTkLabel(tab_slf, text="", height=50, width=250, font=font1)
lab_slf.grid(row=0, column=1, padx=10, pady=10)

# spd 
en_spd = CTk.CTkEntry(tab_spd, placeholder_text="введите расстояние(М)", width=250, height=50, font=font1,)
en_spd.grid(row=0, column=0, padx=10, pady=10)

en2_spd = CTk.CTkEntry(tab_spd, placeholder_text="введите время(с)", width=250, height=50, font=font1)
en2_spd.grid(row=1, column=0, padx=10, pady=10)

btn_spd = CTk.CTkButton(tab_spd, text="Рассчитать", width=250, command=spd, height=50, font=font1)
btn_spd.grid(row=2, column=0, padx=10, pady=10)

lab_spd = CTk.CTkLabel(tab_spd, text="", width=250, height=50, font=font1)
lab_spd.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
