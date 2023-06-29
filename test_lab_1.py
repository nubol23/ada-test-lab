import sqlite3
import pandas as pd


def _check(db_name: str, result_csv: str, solution_file: str):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    expected = pd.read_csv(result_csv)

    with open(solution_file) as f:
        statement = f.read()
        
    result = conn.execute(statement).fetchall()
    
    assert len(result) == expected.shape[0]
    for (_, expected), actual in zip(expected.iterrows(), result):
        assert dict(expected) == dict(actual)


def test_solution_1():
    _check("db.sqlite", "result_1.csv", "solucion_1.sql")
    

def test_solution_2():
    _check("db.sqlite", "result_2.csv", "solucion_2.sql")
