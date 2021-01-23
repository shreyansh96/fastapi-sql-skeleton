import os
from dotenv import load_dotenv

cwd = os.getcwd()
env_file_located_at = '/'.join(cwd.split('/')[:-1]) + '/.env'
load_dotenv(dotenv_path=env_file_located_at)

SERVER_IP = str(os.environ.get("SERVER_IP", "127.0.0.1"))
SERVER_PORT = int(os.environ.get("SERVER_PORT", 8000))
