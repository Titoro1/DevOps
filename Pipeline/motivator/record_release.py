import os
import sqlite3
from datetime import datetime

import tomllib
from dotenv import load_dotenv

load_dotenv()

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

package_name = config["project"]["name"]
version = config["project"]["version"]

# Simulates a secret that would normally be required by a remote database.
db_password = os.getenv("DB_PASSWORD")

if not db_password:
    raise RuntimeError("DB_PASSWORD environment variable is not set")

conn = sqlite3.connect("releases.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS package_releases (
        package_name TEXT,
        version TEXT,
        published_at TEXT
    )
    """
)

cursor.execute(
    """
    INSERT INTO package_releases (package_name, version, published_at)
    VALUES (?, ?, ?)
    """,
    (package_name, version, datetime.now().isoformat()),
)

conn.commit()
conn.close()

print(f"Recorded release: {package_name} {version}")