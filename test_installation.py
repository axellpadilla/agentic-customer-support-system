#!/usr/bin/env python3
"""
Script de prueba rápida para verificar la instalación de Ollama
"""
import subprocess
import sys

def check_ollama():
    """Verifica si Ollama está instalado."""
    try:
        result = subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"✅ Ollama instalado: {result.stdout.strip()}")
            return True
        else:
            print("❌ Ollama no encontrado")
            return False
    except FileNotFoundError:
        print("❌ Comando ollama no disponible")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def check_server():
    """Verifica si el servidor está corriendo."""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Servidor Ollama activo con {len(models)} modelo(s)")
            return True
        else:
            print("⚠️  Servidor no responde correctamente")
            return False
    except:
        print("⚠️  Servidor Ollama no está activo")
        print("   Ejecuta: ollama serve")
        return False

if __name__ == "__main__":
    print("🧪 Verificando instalación de Ollama...")
    print("=" * 40)
    
    if check_ollama():
        check_server()
        print("\n✅ Sistema listo para usar")
    else:
        print("\n❌ Ollama no está instalado")
        print("Ejecuta: python install_ollama.py")
        sys.exit(1)
