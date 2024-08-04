""" 
----------------------------------------------
Ejemplos y campos de solicitudes en Postman
{
    "monto": 100,
    "tipo": "mxn"
}
 Y
 
{
    "monto": 5,
    "tipo": "usd"
}
---------------------------------------------------
""" 

from flask import Flask, jsonify, request

app = Flask(__name__)

EXCHANGE_RATE = 18.92 # Tipo de cambio

def mxn_a_usd(mxn):
    return mxn / EXCHANGE_RATE

def usd_a_mxn(usd):
    return usd * EXCHANGE_RATE

@app.route('/convert', methods=['POST'])
def convert_divisa():
    data = request.get_json()
    monto = data.get('monto')
    divisa_tipo = data.get('tipo')

    if divisa_tipo == 'mxn':
        resultado = mxn_a_usd(monto)
        output_divisa = 'usd'
    elif divisa_tipo == 'usd':
        resultado = usd_a_mxn(monto)
        output_divisa = 'mxn'
    else:
        return jsonify({"error": "Invalido el tipo de divisa. Utilice 'mxn' o 'usd'."}), 400

    return jsonify({"monto": resultado, "divisa": output_divisa})

if __name__ == '__main__':
    app.run(debug=False)
