#!/bin/bash
# Script de inicio rápido para Agentic Customer Support System
# Configura el sistema y ejecuta la aplicación
# Funciona en Codespaces recién creados

set -e  # Salir si hay error crítico

echo "🚀 Agentic Customer Support System - Inicio Rápido"
echo "=================================================="
echo ""

# Obtener directorio del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ejecutar configuración si existe el script
if [ -f "$SCRIPT_DIR/setup.sh" ]; then
    echo "📋 Ejecutando configuración inicial..."
    bash "$SCRIPT_DIR/setup.sh"
    if [ $? -ne 0 ]; then
        echo "❌ Error durante la configuración"
        exit 1
    fi
else
    echo "⚠️  Script setup.sh no encontrado, intentando configuración básica..."
    
    # Configuración básica de respaldo
    python3 -m pip install --upgrade pip --quiet 2>/dev/null || true
    python3 -m pip install -r "$SCRIPT_DIR/requirements.txt" --quiet
fi

echo ""
echo "🎉 Iniciando aplicación Streamlit..."
echo "=================================================="
echo "📍 La aplicación se abrirá en tu navegador"
echo "📍 Si no se abre automáticamente, visita: http://localhost:8501"
echo "📍 Para detener: presiona Ctrl+C"
echo "=================================================="
echo ""

# Ejecutar Streamlit usando python -m para evitar problemas de PATH
cd "$SCRIPT_DIR"
python3 -m streamlit run app.py
