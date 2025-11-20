# Proyecto de Análisis de Datos – Vivienda en California y Mercado Eléctrico en España

Este repositorio contiene un proyecto de análisis exploratorio de datos (EDA) que trabaja con **dos datasets principales de Kaggle**:

1. **California Housing Prices**  
   `camnugent/california-housing-prices`  
   → Precios medianos de vivienda y variables socioeconómicas/geográficas por distrito censal en California.

2. **Spanish Electricity Market: Demand, Generation, Price**  
   `manualrg/spanish-electricity-market-demand-gen-price`  
   → Serie temporal del mercado eléctrico español: precios spot, demanda, generación total y por tecnología.

El objetivo del proyecto es:

- Practicar un **flujo de trabajo reproducible** de ciencia de datos.
- Realizar un **EDA profundo** de cada dataset por separado.
- Construir un **resumen comparativo integrado** entre ambos datasets.

---

## Estructura del proyecto

```
.
├── data
│   ├── interim/
│   ├── processed/
│   │   └── energy_spain_clean.csv
│   └── raw/
│       ├── california_housing/
│       │   └── housing.csv
│       └── energy_spain/
│           └── spain_energy_market.csv
│
├── notebooks/
│   ├── 00_setup_descarga_kaggle.ipynb
│   ├── 01_california_housing_eda.ipynb
│   ├── 02_energy_timeseries_eda.ipynb
│   └── 03_resumen_integrado.ipynb
│
├── reports/
│   ├── figures/
│   └── tables/
│
├── scripts/
│   └── make_figures.py
│
├── src/
│   ├── data/
│   │   └── download_kaggle.py
│   ├── features/
│   └── viz/
│       ├── plots.py
│       └── __init__.py
│
├── README.md
└── requirements.txt
```

---

## Reproducir el entorno

### 1. Crear y activar entorno virtual

```
python -m venv .venv
```

Windows:  
```
.venv\Scripts\activate
```

Linux/Mac:  
```
source .venv/bin/activate
```

### 2. Instalar dependencias

```
pip install -r requirements.txt
```

### 3. Configurar credenciales de Kaggle

Crear archivo `.env`:

```
KAGGLE_USERNAME=tu_usuario
KAGGLE_KEY=tu_api_key
```

### 4. Descargar datos

Ejecutar `00_setup_descarga_kaggle.ipynb`.

---

## Descripción de los notebooks

### **Notebook 01 – California Housing EDA**
- Limpieza inicial
- Diccionario de datos
- Distribuciones e histogramas
- Heatmaps de correlación
- Relaciones clave (ingreso–valor, habitaciones–valor, etc.)

### **Notebook 02 – Spain Energy EDA**
- Conversión de serie temporal
- Pivot para obtener columnas como:
  - `price_es`
  - `demand_es`
  - `generation_total`
  - `generation_wind`
- Análisis de estacionalidad
- Correlaciones energéticas
- Impacto del viento en el precio

### **Notebook 03 – Resumen Integrado**
- Tablas comparativas:
  - `summary`
  - `kpis`
- Conclusiones integradas entre ambos mercados
- Gráfico final comparativo del coeficiente de variación

---

## Resultados principales

### 🔹 California Housing
- Mercado **muy heterogéneo** y disperso.
- Coeficiente de variación ≈ **0.56**  
  → Muestra alta desigualdad en precios.

### 🔹 Mercado eléctrico español
- Precio promedio ≈ **48 €/MWh**
- Variabilidad reducida (coef. variación ≈ **0.28**)
- Fuerte relación inversa entre **generación eólica** y **precio**.

---

## Regenerar todas las figuras

```
python scripts/make_figures.py
```

Todas se guardan en `reports/figures/`.

---

## English Summary

This repository includes a reproducible data analysis project using two Kaggle datasets:
- California Housing Prices  
- Spanish Electricity Market (demand, generation, price)

The project includes:
- Clean data pipeline  
- Reusable visualization tools (`src/viz/plots.py`)  
- Deep EDA for each dataset  
- An integrated comparative notebook (Notebook 03)

---

## Autor
Alejandro A.

Programador en constante formación.

---
