import yaml
import logging
logging.basicConfig(
    filename='ymlll.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

config={"app":{
"name": "Student Portal",
"version": 1.0,},
"database":{
"host": "localhost",
"port": 3306,
"user": "root"}}

def read_config(file_path,config):
    with open(file_path,"w") as f:
        yaml.dump(config,f)
    try:
        with open(file_path,'r') as f:
            data = yaml.safe_load(f)
            localhost = data['database']['host']
            port = data['database']['port']
            root = data['database']['user']
            print(f"connecting to {localhost}:{port} as {root}")
            logging.info(f"connecting to {localhost}:{port} as {root}")

    except FileNotFoundError:
        print("Config file not found")
        logging.error("Config file not found")


read_config("config1.yaml", config)
