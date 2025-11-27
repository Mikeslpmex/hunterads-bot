from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Estado financiero
finances = {
    'ingresos': 0.0,
    'gastos': 0.0,
    'saldo': 0.0,
    'ventas_count': 0,
    'nodos': {
        'afiliados_telegram': {'ingresos': 0.0, 'gastos': 0.0, 'ventas': 0},
        'hotmart': {'ingresos': 0.0, 'gastos': 0.0, 'ventas': 0},
        'mercadolibre': {'ingresos': 0.0, 'gastos': 0.0, 'ventas': 0},
    },
    'historial': [],
}

@app.route('/')
def home():
    return jsonify({
        "status": "Tesorero Orion activo",
        "endpoints": {
            "/estado": "Estado financiero",
            "/reporte": "Registrar venta (POST)",
            "/recomendacion": "Recomendación de inversión"
        }
    })

@app.route('/estado')
def estado():
    return jsonify({
        "ingresos": finances['ingresos'],
        "gastos": finances['gastos'],
        "saldo": finances['saldo'],
        "ventas_count": finances['ventas_count'],
        "nodos": finances['nodos'],
        "ultima_actualizacion": datetime.now().isoformat()
    })

@app.route('/reporte', methods=['POST'])
def reporte():
    try:
        data = request.json
        nodo = data.get('nodo', 'afiliados_telegram')
        ingresos = float(data.get('ingresos', 0))
        gastos = float(data.get('gastos', 0))
        producto = data.get('producto', 'Desconocido')
        
        # Actualizar finanzas
        finances['nodos'][nodo]['ingresos'] += ingresos
        finances['nodos'][nodo]['gastos'] += gastos
        finances['nodos'][nodo]['ventas'] += 1
        
        finances['ingresos'] += ingresos
        finances['gastos'] += gastos
        finances['saldo'] = finances['ingresos'] - finances['gastos']
        finances['ventas_count'] += 1
        
        # Registrar en historial
        finances['historial'].append({
            'fecha': datetime.now().isoformat(),
            'nodo': nodo,
            'producto': producto,
            'ingresos': ingresos,
            'gastos': gastos,
            'saldo_actual': finances['saldo']
        })
        
        # Mantener historial limitado
        if len(finances['historial']) > 100:
            finances['historial'] = finances['historial'][-100:]
        
        return jsonify({
            "status": "success",
            "mensaje": f"Venta de {producto} registrada",
            "saldo_actual": finances['saldo']
        })
        
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 400

@app.route('/recomendacion')
def recomendacion():
    saldo = finances['saldo']
    
    if saldo > 5000:
        recomendacion = f"✅ INVERSIÓN: Puedes invertir ${saldo * 0.7:.2f} en escalar"
    elif saldo > 1000:
        recomendacion = "💡 OPTIMIZACIÓN: Invierte en mejorar los enlaces más rentables"
    else:
        recomendacion = "⚠️ ENFOQUE: Genera más ingresos antes de invertir"
    
    return jsonify({
        "recomendacion": recomendacion,
        "saldo_actual": saldo,
        "nodo_mas_rentable": max(finances['nodos'].items(), key=lambda x: x[1]['ingresos'])[0]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
