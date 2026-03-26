import csv
from pathlib import Path

import matplotlib.pyplot as plt


def read_csv_data(file_path: Path) -> tuple[list[float], list[float]]:
    """CSV dosyasindan iki degiskeni okur."""
    sinav_puani = []
    calisma_suresi_saat = []

    with file_path.open(mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            sinav_puani.append(float(row["sinav_puani"]))
            calisma_suresi_saat.append(float(row["calisma_suresi_saat"]))

    return sinav_puani, calisma_suresi_saat


def create_plot(file_path: Path, sinav_puani: list[float], calisma_suresi_saat: list[float]) -> None:
    """Histogram ve sacilim grafigi olusturup PNG olarak kaydeder."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].hist(sinav_puani, bins=30, alpha=0.75, label="sinav_puani")
    axes[0].hist(calisma_suresi_saat, bins=30, alpha=0.75, label="calisma_suresi_saat")
    axes[0].set_title("Normal Dagilim Histogrami")
    axes[0].set_xlabel("Deger")
    axes[0].set_ylabel("Frekans")
    axes[0].legend()

    axes[1].scatter(sinav_puani, calisma_suresi_saat, alpha=0.6, s=16)
    axes[1].set_title("Sinav Puani - Calisma Suresi")
    axes[1].set_xlabel("Sinav Puani (puan)")
    axes[1].set_ylabel("Calisma Suresi (saat)")

    fig.tight_layout()
    fig.savefig(file_path, dpi=150)
    plt.close(fig)


def main() -> None:
    base_path = Path(__file__).parent
    csv_path = base_path / "normal_dagilim_veri.csv"
    png_path = base_path / "normal_dagilim_grafik.png"

    if not csv_path.exists():
        raise FileNotFoundError("once CSVGen.py calistirilarak normal_dagilim_veri.csv olusturulmalidir")

    sinav_puani, calisma_suresi_saat = read_csv_data(csv_path)
    create_plot(png_path, sinav_puani, calisma_suresi_saat)
    print(f"Gorsel olusturuldu: {png_path}")


if __name__ == "__main__":
    main()
