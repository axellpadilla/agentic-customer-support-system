# Guía de Modelos Ollama para el Sistema

## 🚀 Cambio Rápido de Modelo

### Opción 1: Usando variable de entorno (temporal)
```bash
# Descargar el modelo
ollama pull qwen2.5:0.5b

# Ejecutar con el nuevo modelo
OLLAMA_MODEL=qwen2.5:0.5b python3 -m streamlit run app.py
```

### Opción 2: Archivo .env (permanente)
```bash
# Editar .env
echo "OLLAMA_MODEL=qwen2.5:0.5b" > .env

# Ejecutar normalmente
python3 -m streamlit run app.py
```

## 📊 Comparativa de Modelos

### Ultra-Rápidos (Recomendados para Codespaces)

**qwen2.5:0.5b** ⚡ **[RECOMENDADO]**
- Tamaño: ~0.4GB
- Velocidad: ~5-10 segundos en cpu/codespaces
- Calidad: Buena para soporte básico
- Mejor para: Demos rápidos, pruebas, recursos limitados

**tinyllama**
- Tamaño: ~0.6GB
- Velocidad: ~8-12 segundos en cpu/codespaces
- Calidad: Buena
- Mejor para: Balance velocidad/calidad

### Rápidos

**phi3:mini**
- Tamaño: ~2.3GB
- Velocidad: ~10-15 segundos en cpu/codespaces
- Calidad: Excelente
- Mejor para: Producción con recursos moderados

**llama3.2:1b**
- Tamaño: ~1.3GB
- Velocidad: ~20-25 segundos en cpu/codespaces
- Calidad: Muy buena
- Mejor para: Balance general

### Alta Calidad (Requiere más recursos)

**llama3.2:3b**
- Tamaño: ~2GB
- Velocidad: ~30-40 segundos en cpu/codespaces
- Calidad: Excelente
- Mejor para: Desarrollo local

**llama3.1:8b**
- Tamaño: ~5GB
- Velocidad: ~60-90 segundos en cpu/codespaces
- Calidad: Superior
- Mejor para: Producción con buenos recursos

## 🔄 Comandos Útiles

```bash
# Listar modelos instalados
ollama list

# Descargar un modelo
ollama pull <nombre-modelo>

# Eliminar un modelo
ollama rm <nombre-modelo>

# Probar un modelo
ollama run <nombre-modelo> "Hola, ¿cómo estás?"

# Ver información del sistema
ollama show <nombre-modelo>
```

## 💡 Recomendaciones

**Para GitHub Codespaces:**
1. **Primera opción:** `qwen2.5:0.5b` - Respuestas en ~5-10s
2. **Segunda opción:** `tinyllama` - Respuestas en ~8-12s
3. **Tercera opción:** `phi3:mini` - Respuestas en ~10-15s

**Para desarrollo local:**
1. **Primera opción:** `phi3:mini` - Excelente balance
2. **Segunda opción:** `llama3.2:3b` - Mejor calidad
3. **Tercera opción:** `llama3.1:8b` - Máxima calidad

## 🎯 Instalación de Modelo Alternativo

```bash
# Descargar modelo ultra-rápido
ollama pull qwen2.5:0.5b

# Actualizar configuración
echo "OLLAMA_MODEL=qwen2.5:0.5b" > .env

# Probar el modelo
python3 test_ollama_response.py

# Ejecutar aplicación
python3 -m streamlit run app.py
```

## ⚠️ Notas

- Los tiempos son aproximados y dependen de los recursos del sistema
- Los modelos más pequeños son más rápidos pero pueden tener menor calidad
- Para producción, considera usar OpenAI API en lugar de Ollama local
- En Codespaces, se recomienda usar modelos ≤ 2GB para mejor rendimiento
