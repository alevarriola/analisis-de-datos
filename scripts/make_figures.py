from pathlib import Path
import sys
import pandas as pd

# añadir la raíz del proyecto al sys.path 
ROOT = Path(__file__).resolve().parents[1]  # esto apunta a /analisis-de-datos
sys.path.append(str(ROOT))

from src.viz.plots import (
    line_dual,
    monthly_dual,
    corr_heatmap,
    hist_grid,
    heatmap_month_year,
)

PROC = ROOT / "data" / "processed" / "energy_spain_clean.csv"
CA_RAW = ROOT / "data" / "raw" / "california_housing" / "housing.csv"

def main():
    # --- Energía España ---
    df_es = pd.read_csv(PROC, parse_dates=["datetime"])
    df_es = df_es.sort_values("datetime").set_index("datetime")

    # figuras energía
    line_dual(df_es.reset_index(), "datetime", "price_es", "generation_wind",
              "Precio vs Generación Eólica (España)",
              "Precio (€)", "Generación eólica (MW)",
              fname="es_price_vs_wind.png")

    monthly_dual(df_es, y_bar="generation_wind", y_line="price_es",
                 title="Promedio mensual: Eólica (barras) y Precio (línea)",
                 fname="es_monthly_wind_price.png")

    corr_heatmap(df_es, ["price_es", "demand_es", "generation_total"],
                 "Correlación variables energéticas",
                 fname="es_corr_core.png")

    heatmap_month_year(df_es, "generation_wind",
                       "Estacionalidad anual de la generación eólica",
                       fname="es_wind_heatmap.png")

    # --- California Housing ---
    df_ca = pd.read_csv(CA_RAW)
    hist_grid(df_ca, ["median_house_value","median_income","total_rooms","housing_median_age"],
              "Distribuciones California Housing",
              fname="ca_hist_core.png")

    corr_heatmap(df_ca, ["median_house_value","median_income","total_rooms","housing_median_age"],
                 "Correlaciones California Housing",
                 fname="ca_corr_core.png")

if __name__ == "__main__":
    main()
