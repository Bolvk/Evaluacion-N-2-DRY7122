import requests

def get_route_info(api_key, from_city, to_city):
    '&locale=es_ES'
    url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={from_city}&to={to_city}&outFormat=json&unit=k&locale=es_ES"
    response = requests.get(url)
    return response.json()

def display_route_info(route):
    distance = route['route']['distance']
    time_seconds = route['route']['time']
    fuel_used = route['route'].get('fuelUsed', None)  
    narrative = route['route']['legs'][0]['maneuvers']
   
    time_hours = int(time_seconds // 3600)
    time_minutes = int((time_seconds % 3600) // 60)
    time_seconds = int(time_seconds % 60)
   
    print(f"Distancia: {distance:.2f} km")
    print(f"Duración del viaje: {time_hours} horas, {time_minutes} minutos, {time_seconds} segundos")
    if fuel_used is not None:
        print(f"Combustible requerido: {fuel_used:.2f} litros")
    else:
        print("Información sobre el combustible no disponible.")
    print("Narrativa del viaje:")
    for maneuver in narrative:
        print(maneuver['narrative'])

def main():
    api_key = '3fOMJjuNkVJdAWuOpSiibOszd2634cjT'
    while True:
        from_city = input("Ciudad de Origen: ")
        to_city = input("Ciudad de Destino: ")
       
        if from_city.lower() == 'q' or to_city.lower() == 'q':
            break
       
        route = get_route_info(api_key, from_city, to_city)
        if route['info']['statuscode'] == 0:
            display_route_info(route)
        else:
            print("Error al obtener la información de la ruta.")
       
        print("Ingrese 'q' en cualquiera de las ciudades para salir.")

if __name__ == "__main__":
    main()
