# appends all individual league csvs from poe.ninja in to 1 for database upload

import pandas as pd

path = '/home/gstoltman/projects/analysis/poe-economy-analysis/poe-ninja-exports/sc/currency/'

csv_files = [f'{path}Essence.currency.csv', 
             f'{path}Breach.currency.csv', 
             f'{path}Legacy.currency.csv', 
             f'{path}Harbinger.currency.csv', 
             f'{path}Abyss.currency.csv', 
             f'{path}Bestiary.currency.csv', 
             f'{path}Incursion.currency.csv', 
             f'{path}Delve.currency.csv', 
             f'{path}Betrayal.currency.csv', 
             f'{path}Synthesis.currency.csv', 
             f'{path}Legion.currency.csv', 
             f'{path}Blight.currency.csv', 
             f'{path}Metamorph.currency.csv', 
             f'{path}Delirium.currency.csv', 
             f'{path}Harvest.currency.csv', 
             f'{path}Heist.currency.csv', 
             f'{path}Ritual.currency.csv', 
             f'{path}Ultimatum.currency.csv', 
             f'{path}Expedition.currency.csv', 
             f'{path}Scourge.currency.csv', 
             f'{path}Archnemesis.currency.csv', 
             f'{path}Sentinel.currency.csv', 
             f'{path}Kalandra.currency.csv', 
             f'{path}Sanctum.currency.csv']

combined_data = pd.DataFrame()

for file in csv_files:
    data = pd.read_csv(file)
    combined_data = pd.concat([combined_data, data], ignore_index=True)

combined_data.to_csv(f'{path}all_leagues.csv', index=False)