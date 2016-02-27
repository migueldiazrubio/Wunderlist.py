import requests
import argparse

# 
# Configure this two variables with you app info from Wunderlist API service
#
CLIENT_ID = "PUT_YOUR_CLIENT_ID_HERE"
ACCESS_TOKEN = "PUT_YOUR_ACCESS_TOKEN_HERE"
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
	parser.add_argument("-t", "--task", help="Task name", type=str)
	parser.add_argument("-f", "--textfile", help="File with tasks", type=str)

	args = parser.parse_args()

	# Comprombar si no hay argumentos
	if not (args.task or args.textfile):
		parser.error('Use -t for creating single task or -f to use a textfile to generate tasks automatically')

 	# Obtenemos el inbox del usuario
	response = requests.get(LISTS_ENDPOINT, headers=headers)
	json = response.json()
	inbox_id = 0 
	for item in json:
        	if item["list_type"] == "inbox":
                	inbox_id = item["id"]

	# Crear una tarea por nombre
	if args.task:
			
		params = {
			'list_id': inbox_id,
			'title': args.task
		}
		response = requests.post(TASKS_ENDPOINT, json=params, headers=headers)

	# Crear tareas desde archivo de texto
	if args.textfile:

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
