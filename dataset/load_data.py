import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_ROOT / "dataset"

# PostgreSQL configuration
DB_HOST = os.getenv("DATABASE_HOST", "localhost")
DB_PORT = os.getenv("DATABASE_PORT", "5432")
DB_NAME = os.getenv("DATABASE_NAME", "agentic_bi")
DB_USER = os.getenv("DATABASE_USER", "")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "")


def get_database_url():
    """Build the PostgreSQL connection URL."""
    return (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


def load_table(csv_file: str, table_name: str):
    """Load a CSV file into a PostgreSQL table."""
    csv_path = DATASET_DIR / csv_file

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {csv_path}"
        )

    df = pd.read_csv(csv_path)

    engine = create_engine(get_database_url())

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
    )

    print(
        f"Loaded {len(df):,} records into "
        f"'{table_name}'"
    )


def main():
    """Load all project datasets into PostgreSQL."""

    tables = [
        ("customers.csv", "customers"),
        ("products.csv", "products"),
        ("orders.csv", "orders"),
        ("order_items.csv", "order_items"),
        ("inventory.csv", "inventory"),
        ("marketing_campaigns.csv", "marketing_campaigns"),
        ("returns.csv", "returns"),
        ("business_scenarios.csv", "business_scenarios"),
    ]

    for csv_file, table_name in tables:
        load_table(csv_file, table_name)

    print("Dataset loading completed successfully.")


if __name__ == "__main__":
    main()