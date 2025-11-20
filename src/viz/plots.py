from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FIG_DIR = Path(__file__).resolve().parents[2] / "reports" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

def line_dual(df: pd.DataFrame, x, y_left, y_right, title, ylabel_left, ylabel_right, fname=None):
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(df[x], df[y_left], label=y_left, alpha=0.9)
    ax1.set_ylabel(ylabel_left)
    ax1.set_xlabel("")
    ax2 = ax1.twinx()
    ax2.plot(df[x], df[y_right], label=y_right, alpha=0.7, linestyle="--")
    ax2.set_ylabel(ylabel_right)
    plt.title(title)
    fig.tight_layout()
    if fname:
        out = FIG_DIR / fname
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print("Figura guardada:", out)
    plt.close(fig)

def monthly_dual(df_ts: pd.DataFrame, y_bar, y_line, title, fname=None):
    m = df_ts.resample("M").mean().copy()
    m["month"] = m.index.month
    fig, ax1 = plt.subplots(figsize=(10,5))
    sns.barplot(data=m, x="month", y=y_bar, color="skyblue", ax=ax1)
    ax1.set_ylabel(y_bar)
    ax1.set_xlabel("Mes")
    ax2 = ax1.twinx()
    sns.lineplot(data=m, x="month", y=y_line, color="tab:red", marker="o", ax=ax2)
    ax2.set_ylabel(y_line)
    plt.title(title)
    if fname:
        out = FIG_DIR / fname
        fig.savefig(out, dpi=150, bbox_inches="tight")
        print("Figura guardada:", out)
    plt.close(fig)

def corr_heatmap(df: pd.DataFrame, cols, title, fname=None):
    corr = df[cols].corr()
    fig = plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
    plt.title(title)
    if fname:
        out = FIG_DIR / fname
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print("Figura guardada:", out)
    plt.close(fig)

def hist_grid(df: pd.DataFrame, cols, title, fname=None, bins=30):
    fig = plt.figure(figsize=(14,10))
    df[cols].hist(bins=bins, edgecolor="black")
    plt.suptitle(title)
    if fname:
        out = FIG_DIR / fname
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print("Figura guardada:", out)
    plt.close(fig)

def heatmap_month_year(df_ts: pd.DataFrame, col, title, fname=None):
    m = df_ts.resample("M").mean().copy()
    m["year"] = m.index.year
    m["month"] = m.index.month
    pv = m.pivot_table(values=col, index="year", columns="month")
    fig = plt.figure(figsize=(10,6))
    sns.heatmap(pv, cmap="viridis", cbar_kws={"label": col})
    plt.title(title)
    if fname:
        out = FIG_DIR / fname
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print("Figura guardada:", out)
    plt.close(fig)
