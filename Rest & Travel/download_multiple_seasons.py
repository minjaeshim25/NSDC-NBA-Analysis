# downloading multiple seasons (23-24 and 24-25)

import time
import pandas as pd
from nba_api.stats.endpoints import leaguegamelog

# specify which seasons to download
seasons = ["2023-24", "2024-25", "2025-26"]

for season in seasons:
    print(f"Downloading {season} regular-season data...")

    game_log = leaguegamelog.LeagueGameLog(
        season=season,
        season_type_all_star="Regular Season",
        player_or_team_abbreviation="T",
        sorter="DATE",
        direction="ASC",
        timeout=60
    )

    df = game_log.get_data_frames()[0]

    filename = f"team_game_logs_{season.replace('-', '_')}.csv"
    df.to_csv(filename, index=False)

    print(f"Saved {filename}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print()

    time.sleep(2)

print("Finished downloading the seasons.")
