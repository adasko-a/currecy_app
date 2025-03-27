import tkinter as tk

def center_and_scale(event):    
    """Centruje i skaluje obiekt w oknie."""    
    window_width = root.winfo_width()    
    window_height = root.winfo_height()    
    # Rozmiar obiektu (np. Label) - dostosuj do swoich potrzeb    
    object_width = window_width // 4  # Przykład: 1/4 szerokości okna    
    object_height = window_height // 5  # Przykład: 1/5 wysokości okna    
    # Pozycja obiektu (środek okna)    
    x = (window_width - object_width) // 2    
    y = (window_height - object_height) // 2

    # Aktualizacja położenia i rozmiaru obiektu    
    my_label.place(x=x, y=y, width=object_width, height=object_height)
    
root = tk.Tk()
root.title("Obiekt na środku")
# Obiekt do wyśrodkowania (np. Label z obrazkiem)
my_label = tk.Label(root, text="Obiekt na środku", bg="lightblue")  
# Możesz tu dodać obrazek
my_label.place(x=0,y=0) 
# Początkowe miejsce, zostanie zaktualizowane
# Zwiąż funkcję center_and_scale z zdarzeniem zmiany rozmiaru okna
root.bind("<Configure>", center_and_scale)
root.mainloop()