import requests
import argparse

# 
# Configure this two variables with you app info from Wunderlist API service
#
CLIENT_ID = "PON_AQUI_TU_CLIENT_ID"
ACCESS_TOKEN = "PON_AQUI_TU_ACCESS_TOKEN"
#

LISTS_ENDPOINT = "https://a.wunderlist.com/api/v1/lists"
TASKS_ENDPOINT = "https://a.wunderlist.com/api/v1/tasks"

headers = {
	'content-type': 'application/json',
        'X-Client-ID': CLIENT_ID,
        'X-Access-Token': ACCESS_TOKEN
}

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--tarea", help="Nombre de la tarea", type=str)
	parser.add_argument("-f", "--fichero", help="Fichero con tareas", type=str)

	args = parser.parse_args()

	# Comprombar si no hay argumentos
	if not (args.tarea or args.fichero):
		parser.error('Utiliza -t para crear tareas individuales o -f para cargar masivamente tareas desde un fichero de texto')

 	# Obtenemos el inbox del usuario
	response = requests.get(LISTS_ENDPOINT, headers=headers)
	json = response.json()
	inbox_id = 0 
	for item in json:
        	if item["list_type"] == "inbox":
                	inbox_id = item["id"]

	# Crear una tarea por nombre
	if args.tarea:
			
		params = {
			'list_id': inbox_id,
			'title': args.tarea
		}
		response = requests.post(TASKS_ENDPOINT, json=params, headers=headers)

	# Crear tareas desde archivo de texto
	if args.fichero:

		with open(args.textfile) as file:
			content = file.readlines()
			for task in content:
				params = {
					'list_id': inbox_id,
					'title': task
				}
				response = requests.post(TASKS_ENDPOINT, json=params, headers=headers)


if __name__ == "__main__":
	main()
