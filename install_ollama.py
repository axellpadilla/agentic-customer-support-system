#!/usr/bin/env python3
"""
Instalador automático de Ollama usando el método binario oficial
Basado en: https://github.com/BlackTechX011/Ollama-in-GitHub-Codespaces
"""
import subprocess
import sys
import time
import os

def run_command(cmd, description="", timeout=120, shell=True):
    """Ejecuta un comando y muestra el resultado."""
    print(f"🔧 {description}")
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        if result.returncode == 0:
            print(f"✅ {description} - Exitoso")
            return True
        else:
            print(f"❌ {description} - Falló")
            if result.stderr:
                print(f"   Error: {result.stderr[:200]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} - Tiempo agotado")
        return False
    except Exception as e:
        print(f"❌ {description} - Error: {e}")
        return False

def check_ollama_installed():
    """Verifica si Ollama ya está instalado."""
    try:
        result = subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            print("✅ Ollama ya está instalado")
            return True
    except:
        pass
    return False

def install_ollama_binary():
    """Instala Ollama usando el script oficial (método comprobado)."""
    print("\n📦 Instalando Ollama con el instalador oficial...")
    
    # Descargar e instalar usando el script oficial
    if not run_command(
        "curl -fsSL https://ollama.com/install.sh | sh",
        "Descargando e instalando Ollama",
        timeout=300,  # 5 minutos
        shell=True
    ):
        return False
    
    # Verificar instalación
    if not run_command(
        "ollama --version",
        "Verificando instalación",
        timeout=10,
        shell=True
    ):
        return False
    
    print("✅ Ollama instalado correctamente")
    return True

def start_ollama_server():
    """Inicia el servidor de Ollama en segundo plano."""
    print("\n🖥️  Iniciando servidor Ollama...")
    
    try:
        # Iniciar servidor en segundo plano
        process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        
        # Esperar a que el servidor esté listo
        print("⏳ Esperando a que el servidor esté listo...")
        time.sleep(5)
        
        # Verificar que el servidor responde
        try:
            import requests
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            if response.status_code == 200:
                print("✅ Servidor Ollama iniciado correctamente")
                return True
        except:
            pass
        
        print("⚠️  El servidor puede no estar completamente listo")
        return True
        
    except Exception as e:
        print(f"❌ Error al iniciar servidor: {e}")
        return False

def pull_model(model_name):
    """Descarga el modelo especificado."""
    print(f"\n🤖 Descargando modelo: {model_name}")
    print("⏳ Esto puede tomar varios minutos...")
    
    if not run_command(
        ["ollama", "pull", model_name],
        f"Descargando {model_name}",
        timeout=600  # 10 minutos
    ):
        return False
    
    print(f"✅ Modelo {model_name} descargado correctamente")
    return True

def main():
    """Función principal de instalación."""
    print("🤖 Instalador Automático de Ollama para Codespaces")
    print("=" * 55)
    
    # Obtener nombre del modelo del entorno
    model_name = os.getenv('OLLAMA_MODEL', 'qwen2.5:0.5b')
    print(f"Modelo objetivo: {model_name} (ultra-rápido para Codespaces)\n")
    
    # Verificar si ya está instalado
    if check_ollama_installed():
        print("✅ Ollama ya está disponible")
    else:
        # Instalar Ollama usando el método binario oficial
        if not install_ollama_binary():
            print("\n❌ La instalación falló")
            print("\n📋 Instalación manual:")
            print("   curl -fsSL https://ollama.com/install.sh | sh")
            sys.exit(1)
    
    # Iniciar servidor
    if not start_ollama_server():
        print("\n⚠️  El servidor puede necesitar iniciarse manualmente")
        print("   Ejecuta: ollama serve")
    
    # Descargar modelo
    if not pull_model(model_name):
        print(f"\n⚠️  El modelo {model_name} puede descargarse manualmente")
        print(f"   Ejecuta: ollama pull {model_name}")
    
    print("\n🎉 ¡Instalación completa!")
    print("🚀 Puedes ejecutar: streamlit run app.py")

if __name__ == "__main__":
    main()
