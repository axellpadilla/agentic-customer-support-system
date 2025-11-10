import subprocess
import time
import requests
import os
import sys
from typing import Optional

class OllamaManager:
    """Gestor del ciclo de vida del servidor Ollama y disponibilidad de modelos."""

    def __init__(self, base_url: str = "http://localhost:11434", timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.process: Optional[subprocess.Popen] = None

    def _install_ollama_binary(self) -> bool:
        """Instala Ollama usando el script oficial (método comprobado para Codespaces).
        Basado en: https://github.com/BlackTechX011/Ollama-in-GitHub-Codespaces
        """
        try:
            print("📦 Instalando Ollama con el instalador oficial...")
            
            # Descargar e instalar usando el script oficial
            result = subprocess.run(
                "curl -fsSL https://ollama.com/install.sh | sh",
                shell=True,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutos
            )
            if result.returncode != 0:
                print("❌ Error instalando Ollama")
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}")
                return False
            
            # Verificar instalación
            result = subprocess.run(
                ["ollama", "--version"],
                capture_output=True,
                timeout=5
            )
            if result.returncode == 0:
                print("✅ Ollama instalado correctamente")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Error en instalación: {e}")
            return False

    def _run_setup_if_needed(self) -> bool:
        """Ejecuta la instalación automática si Ollama no está disponible."""
        try:
            # Verificar si ollama está instalado
            subprocess.run(["ollama", "--version"], capture_output=True, check=True, timeout=5)
            return True  # Ollama disponible
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            pass  # Ollama no disponible, intentar instalación

        print("🔧 Ollama no encontrado. Iniciando instalación automática...")
        
        # Intentar instalación con el método binario oficial
        if self._install_ollama_binary():
            return True
        
        # Si falla, intentar script de instalación
        try:
            install_script = os.path.join(os.path.dirname(__file__), "install_ollama.py")
            if os.path.exists(install_script):
                print("📥 Intentando con script de instalación...")
                result = subprocess.run(
                    [sys.executable, install_script],
                    capture_output=True,
                    text=True,
                    timeout=600
                )
                if result.returncode == 0:
                    print("✅ Ollama instalado correctamente")
                    return True
        except Exception as e:
            print(f"❌ Error ejecutando script de instalación: {e}")
        
        print("❌ Instalación automática falló")
        print("📋 Instala manualmente: curl -fsSL https://ollama.com/install.sh | sh")
        return False

    def is_running(self) -> bool:
        """Check if Ollama server is running."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def start_server(self) -> bool:
        """Inicia el servidor Ollama si no está ejecutándose."""
        if self.is_running():
            print("✅ Servidor Ollama ya está ejecutándose")
            return True

        try:
            print("🖥️  Iniciando servidor Ollama...")
            self.process = subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )

            # Esperar a que el servidor inicie
            start_time = time.time()
            while time.time() - start_time < self.timeout:
                if self.is_running():
                    print("✅ Servidor Ollama iniciado correctamente")
                    return True
                time.sleep(1)

            print("❌ El servidor no inició en el tiempo esperado")
            self.stop_server()
            return False

        except FileNotFoundError:
            print("❌ Comando 'ollama' no encontrado. Intentando instalación automática...")
            if self._run_setup_if_needed():
                # Reintentar después de la instalación
                return self.start_server()
            else:
                print("❌ Instalación automática falló")
                print("📋 Instala manualmente: curl -fsSL https://ollama.com/install.sh | sh")
                return False
        except Exception as e:
            print(f"❌ Error iniciando servidor Ollama: {e}")
            return False

    def stop_server(self):
        """Stop the Ollama server if we started it."""
        if self.process:
            try:
                if os.name == 'nt':
                    self.process.terminate()
                else:
                    os.killpg(os.getpgid(self.process.pid), 15)  # SIGTERM
                self.process.wait(timeout=10)
                print("Ollama server stopped.")
            except subprocess.TimeoutExpired:
                self.process.kill()
                print("Ollama server force killed.")
            except Exception as e:
                print(f"Error stopping Ollama server: {e}")
            finally:
                self.process = None

    def model_available(self, model_name: str) -> bool:
        """Verifica si un modelo específico está disponible."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                return any(model['name'] == model_name for model in models)
            return False
        except requests.RequestException:
            return False

    def pull_model(self, model_name: str) -> bool:
        """Descarga un modelo si no está disponible."""
        if self.model_available(model_name):
            print(f"✅ Modelo '{model_name}' ya está disponible")
            return True

        try:
            print(f"📥 Descargando modelo '{model_name}'...")
            print("⏳ Esto puede tomar varios minutos...")
            result = subprocess.run(
                ["ollama", "pull", model_name],
                capture_output=True,
                text=True,
                timeout=600  # 10 minutos
            )

            if result.returncode == 0:
                print(f"✅ Modelo '{model_name}' descargado correctamente")
                return True
            else:
                print(f"❌ Error descargando modelo '{model_name}': {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            print(f"⏰ Tiempo agotado descargando modelo '{model_name}'")
            return False
        except FileNotFoundError:
            print("❌ Comando 'ollama' no encontrado. Intentando instalación automática...")
            if self._run_setup_if_needed():
                # Reintentar después de la instalación
                return self.pull_model(model_name)
            else:
                print("❌ Instalación automática falló")
                print("📋 Instala manualmente: curl -fsSL https://ollama.com/install.sh | sh")
                return False
        except Exception as e:
            print(f"❌ Error descargando modelo: {e}")
            return False

    def ensure_ready(self, model_name: str) -> bool:
        """Asegura que el servidor Ollama esté ejecutándose y el modelo disponible."""
        print(f"\n🤖 Preparando Ollama con modelo '{model_name}'...")
        
        if not self.start_server():
            return False

        if not self.pull_model(model_name):
            return False

        print("✅ Ollama listo para usar\n")
        return True

# Instancia global del gestor
_manager = None

def get_ollama_manager(base_url: str = "http://localhost:11434") -> OllamaManager:
    """Obtiene o crea la instancia global del gestor Ollama."""
    global _manager
    if _manager is None:
        _manager = OllamaManager(base_url)
    return _manager

def ensure_ollama_ready(model_name: str, base_url: str = "http://localhost:11434") -> bool:
    """Función de conveniencia para asegurar que Ollama esté listo con el modelo especificado."""
    manager = get_ollama_manager(base_url)
    return manager.ensure_ready(model_name)

if __name__ == "__main__":
    # Probar el gestor
    model_name = os.getenv('OLLAMA_MODEL', 'qwen2.5:0.5b')
    print("🧪 Probando gestor de Ollama...")
    if ensure_ollama_ready(model_name):
        print("🎉 ¡Ollama está listo!")
    else:
        print("❌ Falló la preparación de Ollama")
        sys.exit(1)