#Trabajo de diccionario - tarea 15
informacion_personal = {"Nombre":"Edgar","Edad":"43","Ciudad":"Mera","Profesión":"Empleado privado"}
informacion_personal["ciudad"]="Puyo"
informacion_personal["Profesión2"]="Administrador"
if "telefono" not in informacion_personal:
  informacion_personal["telefono"] = "987654321"
del(informacion_personal["Edad"])
print (informacion_personal)