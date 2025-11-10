#!/bin/bash
# Script de configuración para Agentic Customer Support System
# Solo instala y configura, sin ejecutar la aplicación

echo "⚙️  Configurando Agentic Customer Support System"
echo "================================================"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Actualizar pip
echo "🔄 Actualizando pip..."
python3 -m pip install --upgrade pip --quiet 2>/dev/null || true

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
if python3 -m pip install -r requirements.txt; then
    echo "✅ Dependencias instaladas"
else
    echo "❌ Error instalando dependencias"
    exit 1
fi
echo ""

# Verificar/Instalar Ollama
echo "🔍 Verificando Ollama..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama ya está instalado: $(ollama --version 2>/dev/null | head -n1)"
else
    echo "📥 Instalando Ollama..."
    if curl -fsSL https://ollama.com/install.sh | sh; then
        echo "✅ Ollama instalado correctamente"
    else
        echo "❌ Error instalando Ollama"
        exit 1
    fi
fi
echo ""

# Iniciar servidor Ollama
echo "🖥️  Iniciando servidor Ollama..."
if pgrep -x ollama > /dev/null; then
    echo "✅ Servidor Ollama ya está corriendo"
else
    nohup ollama serve > /tmp/ollama.log 2>&1 &
    echo "⏳ Esperando a que el servidor inicie..."
    sleep 5
    
    if pgrep -x ollama > /dev/null; then
        echo "✅ Servidor Ollama iniciado"
    else
        echo "⚠️  El servidor puede no haber iniciado correctamente"
        echo "📋 Verifica con: ps aux | grep ollama"
    fi
fi
echo ""

# Descargar modelo
MODEL_NAME="${OLLAMA_MODEL:-qwen2.5:0.5b}"
echo "🤖 Descargando modelo $MODEL_NAME (ultra-rápido)..."
if ollama list 2>/dev/null | grep -q "$MODEL_NAME"; then
    echo "✅ Modelo $MODEL_NAME ya está disponible"
else
    echo "📥 Descargando (esto puede tomar varios minutos)..."
    if ollama pull "$MODEL_NAME"; then
        echo "✅ Modelo descargado correctamente"
    else
        echo "⚠️  Error descargando modelo"
    fi
fi
echo ""

echo "🎉 ¡Configuración completa!"
echo "================================================"
echo "Para iniciar la aplicación, ejecuta:"
echo "  python3 -m streamlit run app.py"
echo ""
echo "O usa el script de inicio rápido:"
echo "  ./start.sh"
echo "================================================"
