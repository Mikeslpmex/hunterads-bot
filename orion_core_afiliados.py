import requests
import time
import os

# 🔹 Generar enlace MEJORADO con afiliados REALES
def generar_enlace_mejorado(producto):
    producto_lower = producto.lower()
    
    # TUS AFILIADOS REALES
    if any(palabra in producto_lower for palabra in ['iphone', 'samsung', 'tv', 'smart']):
        return {
            "url": f"https://www.mercadolibre.com.mx/{producto.replace(' ', '-')}?afiliado=CHMI3457849",
            "plataforma": "Mercado Libre",
            "descripcion": "Electrónicos premium con garantía"
        }
    elif any(palabra in producto_lower for palabra in ['curso', 'digital', 'ebook', 'software']):
        return {
            "url": f"https://hotmart.com/product/{producto.replace(' ', '-')}?ref=148b2b84-a31f-41bc-a63d-43797781dafb",
            "plataforma": "Hotmart",
            "descripcion": "Productos digitales y cursos"
        }
    elif any(palabra in producto_lower for palabra in ['herramienta', 'ferreteria', 'construccion']):
        return {
            "url": f"https://www.amazon.com.mx/{producto.replace(' ', '-')}?tag=CHMI3457849",
            "plataforma": "Amazon",
            "descripcion": "Herramientas y materiales de calidad"
        }
    else:
        # Enlace por defecto
        return {
            "url": f"https://www.mercadolibre.com.mx/{producto.replace(' ', '-')}?afiliado=CHMI3457849",
            "plataforma": "Mercado Libre",
            "descripcion": "Producto recomendado"
        }

# 🔹 Publicar en Telegram
def publicar_en_telegram(mensaje):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("ADMIN_CHAT_ID")
    
    if not token or not chat_id:
        print("❌ Configuración de Telegram no encontrada")
        return {"ok": False}
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        print(f"❌ Error Telegram: {e}")
        return {"ok": False}

# 🔹 Activar publicación de producto
def activar_afiliado(producto):
    enlace_info = generar_enlace_mejorado(producto)
    mensaje = (
        f"🔥 **{producto.upper()}**\n\n"
        f"🔗 [COMPRAR AHORA]({enlace_info['url']})\n"
        f"🏪 {enlace_info['plataforma']}\n"
        f"📦 {enlace_info['descripcion']}"
    )
    
    resultado = publicar_en_telegram(mensaje)
    print(f"✅ Publicado: {producto}")
    return resultado

# 🔹 Modo automático mejorado
def modo_automatico(lista_productos, intervalo=3600):
    print("🌀 Modo automático Orion iniciado...")
    
    productos_optimizados = [
        "iPhone 15 Pro Max 256GB",
        "Samsung Galaxy S24 Ultra", 
        "Smart TV LG 55\" 4K",
        "PlayStation 5 Digital",
        "MacBook Air M3",
        "AirPods Pro 2da generación"
    ]
    
    productos = lista_productos or productos_optimizados
    
    while True:
        for producto in productos:
            activar_afiliado(producto)
            time.sleep(intervalo)

# 🔹 Activación directa
if __name__ == "__main__":
    productos_ejemplo = [
        "iPhone 15 Pro Max",
        "Samsung Galaxy S24",
        "Smart TV LG 4K"
    ]
    modo_automatico(productos_ejemplo, intervalo=3600)  # Cada hora
