def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio
    return temperaturas_promedio
ciudades_temperaturas = {
    "ciudad1_semana1": [78, 80, 82, 79, 85, 88, 92],
    "ciudad1_semana2": [76, 79, 83, 81, 87, 89, 93],
    "ciudad1_semana3": [77, 81, 85, 82, 88, 81, 95],
    "ciudad1_semana4": [75, 78, 80, 79, 84, 87, 91],
    "ciudad2_semana1": [62, 64, 68, 70, 73, 75, 79],
    "ciudad2_semana2": [63, 66, 70, 72, 75, 77, 81],
    "ciudad2_semana3": [61, 65, 68, 70, 72, 76, 80],
    "ciudad2_semana4": [64, 67, 69, 71, 74, 77, 80],
    "ciudad3_semana1": [90, 92, 94, 91, 88, 85, 82],
    "ciudad3_semana2": [89, 91, 93, 90, 87, 84, 81],
    "ciudad3_semana3": [91, 93, 95, 92, 89, 86, 83],
    "ciudad3_semana4": [88, 90, 92, 89, 86, 83, 88],
}
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")




