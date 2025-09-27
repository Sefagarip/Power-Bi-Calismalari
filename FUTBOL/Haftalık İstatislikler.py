from datafc.sofascore import (
    match_data,
    match_odds_data,
    match_stats_data,
    momentum_data,
    lineups_data,
    coordinates_data,
    substitutions_data,
    goal_networks_data,
    shots_data
)
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus  # <- eklendi
# MSSQL bağlantısı – Windows Authentication (Trusted_Connection)
conn_str = (
    "DRIVER=Driver adı;"
    "SERVER=Server adı;"
    "DATABASE=Database adı;"
    "Trusted_Connection=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quote_plus(conn_str)}")
tournament_id = 52
season_id = 63814
all_match_data = []
all_match_odds = []
all_match_stats = []
all_momentum = []
all_lineups = []
all_substitutions = []
all_goal_networks = []
all_shots = []
all_coordinates = []
for week in range(1, 40):  # Tahmini sezon haftası
    try:
        match_df = match_data(tournament_id=tournament_id, season_id=season_id, week_number=week)
        if match_df.empty:
            print(f"{week}. hafta henüz oynanmadı, döngü durduruluyor.")
            break

        # Her fonksiyon çalıştırılıyor
        match_odds_df = match_odds_data(match_df=match_df)
        match_stats_df = match_stats_data(match_df=match_df)
        momentum_df = momentum_data(match_df=match_df)
        lineups_df = lineups_data(match_df=match_df)
        substitutions_df = substitutions_data(match_df=match_df)
        goal_networks_df = goal_networks_data(match_df=match_df)
        shots_df = shots_data(match_df=match_df)
        coordinates_df = coordinates_data(lineups_df=lineups_df)
        # Hepsi listelere ekleniyor
        all_match_data.append(match_df)
        all_match_odds.append(match_odds_df)
        all_match_stats.append(match_stats_df)
        all_momentum.append(momentum_df)
        all_lineups.append(lineups_df)
        all_substitutions.append(substitutions_df)
        all_goal_networks.append(goal_networks_df)
        all_shots.append(shots_df)
        all_coordinates.append(coordinates_df)
        print(f"Hafta {week} verileri başarıyla çekildi.")
    except Exception as e:
        print(f"{week}. hafta verisi alınamadı: {e}")
        break
# Tüm haftaları birleştirme
all_match_data_df = pd.concat(all_match_data, ignore_index=True)
all_match_odds_df = pd.concat(all_match_odds, ignore_index=True)
all_match_stats_df = pd.concat(all_match_stats, ignore_index=True)
all_momentum_df = pd.concat(all_momentum, ignore_index=True)
all_lineups_df = pd.concat(all_lineups, ignore_index=True)
all_substitutions_df = pd.concat(all_substitutions, ignore_index=True)
all_goal_networks_df = pd.concat(all_goal_networks, ignore_index=True)
all_shots_df = pd.concat(all_shots, ignore_index=True)
all_coordinates_df = pd.concat(all_coordinates, ignore_index=True)
print("Tüm fonksiyonların sezon verileri başarıyla birleştirildi.")
# DataFrame'leri MSSQL'e kaydet (append: mevcut tabloya ekler)
all_match_data_df.to_sql("MatchData", engine, if_exists="append", index=False)
all_match_odds_df.to_sql("MatchOdds", engine, if_exists="append", index=False)
all_match_stats_df.to_sql("MatchStats", engine, if_exists="append", index=False)
all_momentum_df.to_sql("Momentum", engine, if_exists="append", index=False)
all_lineups_df.to_sql("Lineups", engine, if_exists="append", index=False)
all_substitutions_df.to_sql("Substitutions", engine, if_exists="append", index=False)
all_goal_networks_df.to_sql("GoalNetworks", engine, if_exists="append", index=False)
all_shots_df.to_sql("Shots", engine, if_exists="append", index=False)
all_coordinates_df.to_sql("Coordinates", engine, if_exists="append", index=False)
print("Tüm DataFrame'ler MSSQL veritabanına aktarıldı.")