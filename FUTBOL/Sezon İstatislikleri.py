import pandas as pd
from datafc.sofascore import (
    standings_data,
    team_stats_data,
    player_stats_data,
    squad_data
)
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# --- Parametreler ---
tournament_id = 52
season_id = 63814

# --- Data çekme ---
standings_df = standings_data(
    tournament_id=tournament_id,
    season_id=season_id
)

team_stats_df = team_stats_data(
    standings_df=standings_df,
    tournament_id=tournament_id,
    season_id=season_id
)

player_stats_df = player_stats_data(
    standings_df=standings_df,
    tournament_id=tournament_id,
    season_id=season_id
)

squad_df = squad_data(
    standings_df=standings_df
)

# --- MSSQL bağlantısı ---
conn_str = (
    "DRIVER=Driver adı;"
    "SERVER=Server adı;"
    "DATABASE=Database adı;"
    "Trusted_Connection=yes;"
)
quoted_conn_str = quote_plus(conn_str)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted_conn_str}")

# --- DataFrame'leri MSSQL'e yazma ---
standings_df.to_sql("Standings", engine, if_exists="replace", index=False)
team_stats_df.to_sql("TeamStats", engine, if_exists="replace", index=False)
player_stats_df.to_sql("PlayerStats", engine, if_exists="replace", index=False)
squad_df.to_sql("Squad", engine, if_exists="replace", index=False)

print("✅ Tüm tablolar MSSQL'e aktarıldı!")
