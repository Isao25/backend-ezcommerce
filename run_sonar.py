from dotenv import load_dotenv
import os
import subprocess

load_dotenv()  # Carga las variables del .env

token = os.getenv('SONARQUBE_TOKEN')
if not token:
    raise ValueError("SONARQUBE_TOKEN no está definido en el archivo .env")

command = f'sonar-scanner -Dsonar.token={token}'
subprocess.run(command, shell=True, check=True)