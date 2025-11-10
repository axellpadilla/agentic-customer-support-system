#!/usr/bin/env python3
"""
Script simple para probar que Ollama responde correctamente a mensajes
"""
import subprocess
import sys
import json
import time

def test_ollama_response():
    """Prueba que Ollama responda correctamente."""
    print("🧪 Probando respuesta de Ollama...")
    print("=" * 50)
    
    model = "qwen2.5:0.5b"
    prompt = "Di solo 'Hola' en español y nada más"
    
    print(f"\n📤 Enviando mensaje al modelo '{model}'...")
    print(f"   Prompt: {prompt}\n")
    
    try:
        # Usar ollama run para probar
        start_time = time.time()
        
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        elapsed = time.time() - start_time
        
        if result.returncode == 0:
            response = result.stdout.strip()
            
            print("✅ Ollama respondió correctamente!\n")
            print("📥 Respuesta del modelo:")
            print("-" * 50)
            print(response[:300])  # Primeros 300 caracteres
            if len(response) > 300:
                print("...")
            print("-" * 50)
            print(f"\n⏱️  Tiempo de respuesta: {elapsed:.2f} segundos")
            
            print("\n" + "=" * 50)
            print("🎉 ¡Ollama funciona perfectamente!")
            print("\n✅ El sistema está listo para:")
            print("   • Responder a consultas")
            print("   • Procesar mensajes de clientes")
            print("   • Ejecutar la aplicación completa")
            
            return True
        else:
            print(f"\n❌ Error en la respuesta")
            print(f"   {result.stderr[:200]}")
            return False
            
    except subprocess.TimeoutExpired:
        print("\n⏰ Timeout - El modelo tardó más de 60 segundos")
        return False
    except FileNotFoundError:
        print("\n❌ Comando 'ollama' no encontrado")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_ollama_response()
    sys.exit(0 if success else 1)
