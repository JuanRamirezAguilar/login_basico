import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import hashlib
from dbUsuario import DBUsuario

from usuario import Usuario

def captcha() -> str:
    import random as rd
    import string

    LENGHT_CODE = 6 # Tamaño del codigo captcha generado
    codigo = ""

    # Cadena de numeros alfanumericos
    caracteres = string.ascii_uppercase + string.digits + string.ascii_lowercase

    for _ in range (LENGHT_CODE):
        char = rd.choice(caracteres)
        codigo += char

    return codigo
# Fin captcha()

def login(root) -> None:
    global str_captcha
    
    # Frame que cubre todo el login
    frame_login = ttk.Frame(root, padding=20)
    frame_login.pack(fill="both", expand=True)

    # Imagen de usuario
    img_path = "src/user.png"
    img = Image.open(img_path)

    # Redimensionar la imagen
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
    img =img.convert("RGBA")

    user_img = ImageTk.PhotoImage(img)
    img_label = ttk.Label(frame_login, image=user_img)
    img_label.image = user_img
    img_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    # Widgets del correo y de la contraseña
    label_info = ttk.Label(frame_login, text="Ingresa tu correo y contraseña.")
    label_info.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    label_correo = ttk.Label(frame_login, text="Correo: ")
    label_correo.grid(row=2, column=0, padx=5, pady=5)

    entry_correo = ttk.Entry(frame_login, width=25)
    entry_correo.grid(row=2, column=1, padx=5, pady=5)

    label_password = ttk.Label(frame_login, text="Contraseña: ")
    label_password.grid(row=3, column=0, padx=5, pady=5)

    entry_password = ttk.Entry(frame_login, show='*', width=25)
    entry_password.grid(row=3, column=1, padx=5, pady=5)

    # Captcha del login
    style_captcha = ttk.Style()
    style_captcha.configure("Custom.TFrame", background="white")

    frame_captcha = ttk.Frame(frame_login, style="Custom.TFrame")
    frame_captcha.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

    label_captcha1 = ttk.Label(frame_captcha, text="Ingresa el captcha", font=("Helvetica", 12, "bold"), foreground="red", background="white")
    label_captcha1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    
    str_captcha = captcha() # Se le asigna un captcha aleatorio

    label_captcha2 = ttk.Label(frame_captcha, text=str_captcha, font=("Helvetica", 15, "bold"), borderwidth=20)
    label_captcha2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    entry_captcha = ttk.Entry(frame_captcha)
    entry_captcha.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


    # Boton del login
    button_login = ttk.Button(frame_login, text="Ingresar", padding=5, command=lambda:comprobar_login())
    button_login.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

    def cambiar_captcha() -> None:
        global str_captcha
        
        new_captcha = captcha()
        str_captcha = new_captcha
        label_captcha2.configure(text=new_captcha)
        entry_captcha.delete(0, len(entry_captcha.get()))
    # Fin cambiar_captcha()

    # Cuando se use el boton del login, esto se va a usar para logearse
    def comprobar_login() -> None:        
        var_correo = entry_correo.get()
        var_password = entry_password.get()
        var_captcha = entry_captcha.get()
    # Fin comprobar_login()

        if not var_correo or not var_password or not var_captcha:
            messagebox.showwarning(title="Aviso", message="No se ha ingresado ningun dato.")
            cambiar_captcha()
            return
            
        if var_captcha != str_captcha:
            message_captcha = ttk.Label(frame_captcha, text="Captcha invalido.", foreground="red")
            message_captcha.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
            cambiar_captcha()
            return

        
        encript_pass = hashlib.md5(var_password.encode()).hexdigest()
        user_login = Usuario(0, var_correo, encript_pass, "")
        
        autentificacion = DBUsuario()
        
        if not autentificacion.authenticate_user(user_login):
            messagebox.showerror(title="Error en el login.", message="Correo o contraseña incorrectos.")
            cambiar_captcha()
            return
        
        # Logica para el inicio de sesion
        messagebox.showinfo(title="Login", message="Login correcto.")

    root.mainloop()
# Fin login



def main() -> None:
    # Configuraciones del login
    raiz_de_vetana = ttk.Window(themename="superhero")
    raiz_de_vetana.title("Login - Contraseña")
    raiz_de_vetana.resizable(False, False)
    
    login(raiz_de_vetana)
# Fin main

if __name__ == "__main__":
    main()