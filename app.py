import os

from flask import Flask
app= Flask(__name__)

@app.route("/")
def main():
  return "Bienvenido otra vez!!!!"

@app.route("/ComoEstas")
def hola():
  return "Estoy bien gracias. Muchas gracias"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
