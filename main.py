import requests
import json

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

def get_information(url):
    response = requests.get(url)
    assert response.status_code == 200, f'Algo salio mal: {response.status_code}'
    content = json.loads(response.content)
    return content

def run():
    pesos_to_dolars = lambda pesos, dolar_value: pesos / dolar_value
    dolars_to_pesos = lambda dolars, dolar_value: dolars * dolar_value

    info = get_information(URL)

    dolar_value = float(info[0]['casa']['compra'].replace(',','.'))
    print(dolar_value)

    choice = input('¿Qué operacion quieres hacer \n 1: Dolar a pesos \n 2: Pesos a dolar \n ')
    if choice == '1':
        dolars = float(input('¿Cuántos dolares tienes?: '))
        pesos = round(dolars_to_pesos(dolars,dolar_value), 2)
        print(f'Equivalente a {pesos} pesos')
    elif choice == '2':
        pesos = float(input('¿Cuántos pesos tienes?: '))
        dolars = round(pesos_to_dolars(pesos, dolar_value), 2)
        print(f'Equivalen a {dolars} dolares')
    else:
        print('Escribe una opción correcta, gracias')

if __name__ == '__main__':
    run()
