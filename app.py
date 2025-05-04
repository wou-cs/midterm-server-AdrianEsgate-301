from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<int:x>", methods=["GET"])
def Decrement_by_one_and_show_hex_number(x):
    calculations = {"dec": x - 1, "hex": hex(x - 1)}
    return calculations, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Specify host and port here
    


    
