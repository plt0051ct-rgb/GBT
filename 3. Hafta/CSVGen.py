import csv
import random
from pathlib import Path


def generate_normal_dataset(row_count: int = 500) -> list[tuple[float, float]]:
	"""Iki degiskenli normal dagilim verisi uretir."""
	data = []

	for _ in range(row_count):
		# Ornek kurgu: sinav puani ve calisma suresi.
		sinav_puani = random.gauss(mu=70, sigma=10)
		calisma_suresi_saat = random.gauss(mu=6, sigma=1.5)
		data.append((round(sinav_puani, 4), round(calisma_suresi_saat, 4)))

	return data


def write_csv(file_path: Path, data: list[tuple[float, float]]) -> None:
	"""Uretilen veriyi CSV dosyasina yazar."""
	with file_path.open(mode="w", newline="", encoding="utf-8") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["sinav_puani", "calisma_suresi_saat"])
		writer.writerows(data)


def main() -> None:
	output_path = Path(__file__).with_name("normal_dagilim_veri.csv")
	dataset = generate_normal_dataset(row_count=500)
	write_csv(output_path, dataset)
	print(f"CSV olusturuldu: {output_path}")
	print(f"Toplam satir: {len(dataset)}")


if __name__ == "__main__":
	main()
