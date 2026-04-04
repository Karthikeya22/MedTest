import pandas as pd
from datetime import date
from dialer import call_parent

def run():
    df = pd.read_csv("schedule.csv")

    today = date.today().isoformat()  # e.g. 2026-03-21
    due = df[df["call_date"].astype(str) == today]

    print(f"Found {len(due)} rows for {today}")

    for _, row in due.iterrows():
        row_dict = row.to_dict()
        print(f"Calling {row_dict.get('parent_phone')} for {row_dict.get('patient_name')}")
        call_parent(row_dict)

if __name__ == "__main__":
    run()