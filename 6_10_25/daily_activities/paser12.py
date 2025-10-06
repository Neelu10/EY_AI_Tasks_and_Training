import configparser
config = configparser.ConfigParser()

config["database"]={
    "host": "localhost",
    "user": "root",
    "password": "admin123",
    "port": "3306",
}
with open("app.ini", "w") as configfile:
    config.write(configfile)

with open("app.ini", "r") as configfile:
    print(config["database"]["host"])