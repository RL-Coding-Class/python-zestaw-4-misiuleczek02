import sqlite3
import pandas as pd

def create_table(max_repeats, databasefile="flights.db"):
    """Tworzy tabelę w bazie danych SQLite, jeśli max_repeats > 0."""
    conn = sqlite3.connect(databasefile)
    cursor = conn.cursor()

    if max_repeats > 0:
        # Usunięcie tabeli, jeśli istnieje
        cursor.execute("DROP TABLE IF EXISTS airport_atl")
        
        # Tworzenie nowej tabeli
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
    
    conn.commit()
    conn.close()


def save_to_db(flight_df, databasefile="flights.db"):
    """Zapisuje dane z DataFrame do bazy SQLite."""
    conn = sqlite3.connect(databasefile)
    flight_df.to_sql("airport_atl", conn, if_exists="append", index=False)
    conn.close()


def load_flight_data(databasefile="flights.db"):
    """Odczytuje dane z bazy SQLite i zwraca je jako DataFrame."""
    conn = sqlite3.connect(databasefile)
    flight_df = pd.read_sql_query("SELECT * FROM airport_atl", conn)
    conn.close()
    return flight_df
