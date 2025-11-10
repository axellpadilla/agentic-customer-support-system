# Agentic Customer Support System

Sistema inteligente de atención al cliente que usa agentes de IA para proporcionar respuestas contextuales y empáticas. Construido con Python, Pydantic-AI, Streamlit, y modelos locales Ollama con compatibilidad OpenAI.

## 🌟 Características

- **Gestión Automática de Ollama**: Inicia automáticamente el servidor Ollama y descarga modelos según sea necesario
- **Contexto Inteligente**: Mantiene historial y preferencias del cliente
- **Servicio por Niveles**: Diferentes niveles de servicio para diferentes categorías de clientes
- **Seguimiento de Pedidos**: Información en tiempo real del estado de los pedidos
- **Análisis de Sentimiento**: Analiza el sentimiento del cliente para mejores respuestas
- **Base de Conocimiento**: Acceso rápido a políticas de envío, devoluciones y garantías
- **Manejo de Errores**: Degradación elegante cuando los servicios no están disponibles

## 🛠️ Stack Tecnológico

- Python 3.8+
- Streamlit
- Pydantic
- Pydantic-AI
- Ollama (modelos locales con compatibilidad OpenAI API)

## 📋 Requisitos

- Python 3.8 o superior
- Git

## 🚀 Instalación

### Método 1: GitHub Codespaces (Automático) ⭐

Si abres este repositorio en GitHub Codespaces, **todo se configura automáticamente**:
- Instala todas las dependencias
- Configura Ollama
- Descarga el modelo

Solo necesitas ejecutar:
```bash
python -m streamlit run app.py
```

### Método 2: Inicio Rápido (Recomendado para local)

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Croups/agentic-customer-support-system
cd agentic-customer-support-system
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Iniciar la aplicación:**
```bash
python -m streamlit run app.py
```

**¡Eso es todo!** El sistema instalará y configurará Ollama automáticamente la primera vez que lo ejecutes usando el [método comprobado de instalación binaria](https://github.com/BlackTechX011/Ollama-in-GitHub-Codespaces).

### Método 3: Script de Inicio Rápido

Un solo comando para configurar y ejecutar todo:

```bash
chmod +x start.sh && ./start.sh
```

Este script ejecuta automáticamente `setup.sh` para configurar el entorno completo.

### Método 4: Solo Configuración (sin ejecutar)

Si prefieres configurar todo primero y ejecutar después:

```bash
# Configurar todo (instala dependencias, Ollama y descarga modelo)
chmod +x setup.sh && ./setup.sh

# Luego ejecutar cuando quieras
python -m streamlit run app.py
```

### Método 5: Configuración Manual

```bash
# Instalar dependencias
pip install -r requirements.txt

# Instalar Ollama
python install_ollama.py

# Verificar instalación
python test_installation.py

# Ejecutar app
python -m streamlit run app.py
```

## 🔧 Configuración (Opcional)

Puedes personalizar el modelo de Ollama creando un archivo `.env`:

```bash
OLLAMA_MODEL=qwen2.5:0.5b  # Modelo ultra-rápido (recomendado para Codespaces)
```

### Modelos Recomendados por Velocidad

**Para GitHub Codespaces (recursos limitados):**
- `qwen2.5:0.5b` - ~0.4GB, **ultra-rápido** (~5-10s), ideal para demos ⚡
- `tinyllama` - ~0.6GB, **muy rápido** (~8-12s), buena calidad
- `phi3:mini` - ~2.3GB, rápido (~10-15s), excelente para producción
- `llama3.2:1b` - ~1.3GB, balanceado (~20-25s) (por defecto)

**Para desarrollo local (más recursos):**
- `phi3` - ~2.3GB, rápido y eficiente
- `llama3.2:3b` - ~2GB, rendimiento balanceado
- `llama3.1:8b` - ~5GB, mejor calidad

**Cambiar modelo:**
```bash
# Descargar modelo más rápido
ollama pull qwen2.5:0.5b

# Actualizar variable de entorno
echo "OLLAMA_MODEL=qwen2.5:0.5b" > .env

# O exportar temporalmente
export OLLAMA_MODEL=qwen2.5:0.5b
```

📖 **Ver guía completa de modelos:** [MODELS.md](MODELS.md)

## 🧪 Pruebas

Antes de ejecutar la aplicación, puedes verificar que todo funciona:

```bash
# Prueba 1: Verificar instalación
python3 test_installation.py

# Prueba 2: Probar respuesta de Ollama
python3 test_ollama_response.py
```

## 💻 Uso

Una vez iniciada la aplicación con `python -m streamlit run app.py`:

1. Abre tu navegador en `http://localhost:8501`
2. Usa la interfaz para:
   - Ver información del cliente
   - Consultar estado de pedidos
   - Acceder a información de envíos
   - Ver políticas de devolución
   - Obtener información de garantías

## 📁 Estructura del Proyecto

```
├── app.py                # Interfaz Streamlit
├── support_system.py     # Sistema de agentes principal
├── ollama_manager.py     # Gestión del servidor y modelos Ollama
├── install_ollama.py     # Instalador automático de Ollama
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Documentación
```

## 🔄 Alternativa: Usar OpenAI API

Si prefieres usar OpenAI en lugar de Ollama local:

1. Obtén una API key de [platform.openai.com](https://platform.openai.com/api-keys)

2. Crea un archivo `.env`:
```
OPENAI_API_KEY=tu_api_key_aqui
USE_OPENAI=true
```

3. El sistema usará automáticamente el modelo GPT-4o-mini de OpenAI

**Beneficios:**
- Sin descargas de modelos locales
- Inferencia más rápida
- Rendimiento consistente
- Sin límites de recursos

## 🔧 Instalación Manual de Ollama

Si prefieres instalar Ollama manualmente:

```bash
# Método recomendado (script oficial)
curl -fsSL https://ollama.com/install.sh | sh

# Iniciar servidor
ollama serve

# Descargar modelo (en otra terminal)
ollama pull llama3.2:1b
```

## ⚠️ Consideraciones para Codespaces

- **Límites de recursos**: Los Codespaces tienen límites de CPU/memoria que pueden afectar el rendimiento
- **Almacenamiento**: Los modelos se descargan al almacenamiento del Codespace
- **Red**: La descarga inicial del modelo requiere conexión a internet
- **Persistencia**: Los modelos persisten entre sesiones pero pueden necesitar re-descarga si se reinicia el entorno

# Modificado de repositorio original como demo:
https://github.com/Croups/agentic-customer-support-system


