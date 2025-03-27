import requests
from tkinter import *
from tkinter import ttk


currency_dict = {'złoty':('PLN', 1.0)}

def get_request():
    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a?json/')
    if response.ok:
        data = response.json()[0]
        string = ' '.join([data['no'], data['effectiveDate']])
        temp_dict = {element['currency']:(element['code'], element['mid']) for element in data['rates']}
        main_header_var.set(string)
        currency_dict.update(temp_dict)
        center_and_place_widget(main_header,main_header.winfo_reqheight())
        combobox_from['values'] = list(currency_dict.keys())
        combobox_to['values'] = list(currency_dict.keys())
        combobox_from.place(x=200, y=120)
        ammount.place(x=200, y=200)
        combobox_to.place(x=600, y=120)
        center_and_place_widget(calculate_button, 250)
        result_var.set('')
        center_and_place_widget(result_label, result_label.winfo_reqheight())
        combobox_from.set('')
        combobox_to.set('')
        ammount.delete(0, END)

    else:
        if len(currency_dict) == 1:
            main_header_var.set('ConnectionError.')
            center_and_place_widget(main_header,main_header.winfo_reqheight())
        else:
            result_var.set('ConnectionError.')
            center_and_place_widget(result_label, result_label.winfo_reqheight())


def center_and_place_widget(widget, y_pos):    
    """Centruje i skaluje obiekt w oknie."""    
    root.update()
    window_width = root.winfo_width() 
    widget_width = widget.winfo_reqwidth()  
    x_center = (window_width - widget_width) // 2
    widget.place(x=x_center, y=y_pos)


def calculate():
    try:
        ammount_to_count = float(ammount.get())
    except Exception as e:
        result_var.set('Invalid value!')
        center_and_place_widget(result_label, 350)
    else:
        if combobox_from.get() is False or combobox_to.get() is False:
            result_var.set('Select currency!')
            center_and_place_widget(result_label, 350)
        elif combobox_from.get() == combobox_to.get() or combobox_from.get() not in currency_dict or combobox_to.get() not in currency_dict:
            result_var.set('Select diffrent currencies!')
            center_and_place_widget(result_label, 350)
        else:
            input_ammount = float(ammount.get()) * currency_dict[combobox_from.get()][1]
            output_ammount = input_ammount / currency_dict[combobox_to.get()][1]
            output_str = ammount.get() + ' ' + currency_dict[combobox_from.get()][0] + ' ------> ' + f'{output_ammount:.2f}' + ' ' + currency_dict[combobox_to.get()][0] 
            result_var.set(output_str)        
            center_and_place_widget(result_label, 350)

    

# Tworzenie okna
root = Tk(screenName = 'KursWalut') # Utworzenie głównego okna z nazwą w systemie
root.title('Kurs walut')  # nadanie tytułu okna
root.geometry('1000x400') # zdefiniowanie początkowego rozmiaru okna
root.resizable(False, False) # zablokowanie rozmiaru okna dla wysokości i szerokości
main_header_var = StringVar()
main_header_var.set('Download currency list.')
main_header = Label(root, textvariable= main_header_var, font = ('Arial', 16))
request_button = Button(root, text = 'Get request', font = ('Arial', 16), command = get_request, bg= 'blue', fg= 'blue', activebackground= 'green')
#tworzenie dwóch comboboxów z dostępnymi walutami
combobox_from = ttk.Combobox(root, values = list(currency_dict.keys()))
combobox_to = ttk.Combobox(root, values = list(currency_dict.keys()))
#tworzenie obiektu entry do wpisania ilości do przliczenia
ammount = Entry(root)
#tworzenie przysicku calculate
calculate_button = Button(root, text = 'Calculate', fg = 'lightblue', activebackground='blue', command=calculate, font = ('TimesNewRoman', 20))
#tworzenie wyniku
result_var = StringVar()
result_label = Label(root,textvariable=result_var, font = ('Arial', 25), fg = 'red')
#root.after(100, lambda: center_and_place_widget(main_header, 40))
#root.after(100, lambda: center_and_place_widget(request_button, 70))
center_and_place_widget(main_header, 40)
center_and_place_widget(request_button, 70)
root.mainloop()

