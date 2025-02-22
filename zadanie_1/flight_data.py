import sqlite3

try:
    import pandas as pd
    import requests
    import matplotlib.pyplot as plt
except ImportError as e:
    raise ImportError(f"Brakuje modułu: {e.name}. Zainstaluj go używając 'pip install {e.name}'.")

def create_table(max_repeats, databasefile="flights.db"):
    """Tworzy bazę danych SQLite i tabelę na podstawie specyfikacji."""
    connection = sqlite3.connect(databasefile)
    cursor = connection.cursor()
    try:
        if max_repeats > 0:
            cursor.execute("DROP TABLE IF EXISTS airport_atl")
            cursor.execute(
                '''CREATE TABLE airport_atl (
                    icao24 TEXT,
                    callsign TEXT,
                    origin_country TEXT,
                    time_position INTEGER,
                    last_contact INTEGER,
                    long REAL,
                    lat REAL,
                    baro_altitude REAL,
                    on_ground TEXT,
                    velocity REAL,
                    true_track REAL,
                    vertical_rate REAL,
                    sensors TEXT,
                    geo_altitude REAL,
                    squawk TEXT,
                    spi TEXT,
                    position_source INTEGER
                )'''
            )
            connection.commit()
    finally:
        connection.close()

def save_to_db(flight_df, databasefile="flights.db"):
    """Zapisuje dane do bazy SQLite."""
    connection = sqlite3.connect(databasefile)
    try:
        flight_df.to_sql("airport_atl", connection, if_exists="append", index=False)
    finally:
        connection.close()

def load_flight_data(databasefile="flights.db"):
    """Odczytuje dane lotnicze z bazy SQLite i zwraca DataFrame."""
    connection = sqlite3.connect(databasefile)
    try:
        return pd.read_sql_query("SELECT * FROM airport_atl", connection)
    finally:
        connection.close()

def fetch_flight_data(databasefile="flights.db"):
    """Pobiera dane z OpenSky Network API i zapisuje do bazy danych SQLite."""
    lon_min, lat_min = -85.4277, 32.6407
    lon_max, lat_max = -83.4277, 34.6407
    
    url_data = (
        f'https://opensky-network.org/api/states/all?'
        f'lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}'
    )
    
    try:
        response = requests.get(url_data)
        response.raise_for_status()
        data = response.json()
        
        if "states" not in data or data["states"] is None:
            print("Brak danych do zapisania.")
            return
        
        col_names = [
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact',
            'long', 'lat', 'baro_altitude', 'on_ground', 'velocity',
            'true_track', 'vertical_rate', 'sensors', 'geo_altitude',
            'squawk', 'spi', 'position_source'
        ]
        
        flight_df = pd.DataFrame(data["states"], columns=col_names).dropna(subset=['velocity', 'geo_altitude'])
        save_to_db(flight_df, databasefile)
        print("Dane zapisano do bazy danych!")
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania danych: {e}")

def plot_flight_data(databasefile="flights.db", show_plot=True):
    """Generuje wykres zależności wysokości od prędkości."""
    flight_df = load_flight_data(databasefile)
    
    if flight_df.empty:
        print("⚠️ Brak danych do wyświetlenia.")
        return
    
    flight_df = flight_df.dropna(subset=['velocity', 'geo_altitude'])
    flight_df['velocity'] = pd.to_numeric(flight_df['velocity'], errors='coerce') * 3.6  # m/s -> km/h
    flight_df['geo_altitude'] = pd.to_numeric(flight_df['geo_altitude'], errors='coerce') / 1000  # m -> km
    flight_df = flight_df.sort_values(by='velocity').drop_duplicates(subset='icao24', keep='first')
    
    plt.figure(figsize=(8, 6))
    plt.scatter(flight_df['velocity'], flight_df['geo_altitude'], alpha=0.6)
    plt.xlabel("Velocity (km/h)")
    plt.ylabel("Geometric Altitude (km)")
    plt.title("Aircraft Velocity vs. Geometric Altitude")
    plt.xlim(0, 1200)
    plt.ylim(0, 14)
    plt.grid(True)
    
    if show_plot:
        plt.show(block=False)
        plt.pause(3)
        plt.close()
    else:
        plt.savefig("flight_plot.png")
        print("Wykres zapisano jako 'flight_plot.png'")
