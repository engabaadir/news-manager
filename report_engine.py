#!/usr/bin/env python3
import psycopg2

def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""

    db = psycopg2.connect(
        user="postgres",
        password="Abc123",
        host="127.0.0.1",
        port="5432",
        database="news"
    )

    cr = db.cursor()
    cr.execute(query)
    rows = cr.fetchall()
    db.close()
    return rows
