import schedule
import time
from database import create_table
from flight_data import fetch_flight_data, plot_flight_data

def main(interval, max_repeats):
    create_table(max_repeats)

    counter = 0

    def job_wrapper():
        nonlocal counter
        if counter < max_repeats:
            print(f"⏳ Pobieranie danych... Iteracja {counter + 1} z {max_repeats}")
            fetch_flight_data()
            counter += 1
        else:
            print("✅ Wszystkie zadania zakończone. Kończę program.")
            schedule.clear()  # Zatrzymanie harmonogramu

    schedule.every(interval).seconds.do(job_wrapper)

    while counter < max_repeats:
        schedule.run_pending()
        time.sleep(interval)  # Oczekiwanie na kolejną iterację

    print("📊 Generowanie wykresu...")
    plot_flight_data()
    print("✅ Program zakończył działanie.")

if __name__ == '__main__':
    FETCH_INTERVAL = 10  # Skróć czas na testy (np. 10 sekund zamiast 60)
    MAX_REPEATS = 3  # Zmniejsz liczbę powtórzeń na testy

    main(FETCH_INTERVAL, MAX_REPEATS)

