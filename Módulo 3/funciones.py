def mt_a_cm(metros): #metros = 2.33
    cm = metros*100 #cm = 2.33 * 100 = 233
    return cm # <- 233


def saludar():
    print("¡Hola!")

nombre = "Diego"

def saludar_nombre(nombre): #nombre = "Diego"
    otra_variable = ":)"
    print(f"¡Hola {nombre} {otra_variable}!")
    #print("¡Hola "+nombre+"!")


saludar()
saludar()
saludar()
saludar()
saludar()
saludar()

saludar_nombre("Elena")
saludar_nombre("Juana")
saludar_nombre(nombre) #nombre = "Diego"

centimetros = mt_a_cm(1.55) #centimetros = 155

def mt_a_cm_y_mm(metros): #metros = 2.33
    cm = mt_a_cm(metros) #cm = 233
    mm = metros * 1000 #mm = 2.33 * 1000 = 2330
    if mm > 2000: 
        print("wow son muchos mm")
    return (cm, mm) #regresa 233, 2330


centimetros, milimetros = mt_a_cm_y_mm(2.33) #centimetros = 233, milimetros = 2330
print(centimetros, milimetros)

def saludito(nombre="Elena", apellido="De Troya"): #nombre = "Elena", apellido = "De Arco"
    print(f"¡Buen día {nombre} {apellido}! ¿cómo va todo?")

saludito()
saludito("Juana") #¡Buen día Juana De Troya! ¿cómo va todo? 
saludito(apellido="De Arco") #¡Buen día Elena De Arco" ¿cómo va todo?
saludito(apellido="De Arco", nombre="Juana") #¡Buen día Juana de Arco! ¿cómo va todo?
