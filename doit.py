#! /usr/bin/env python

import os
import ibis
import pandas as pd

def get_postgres_creds():
    kwargs = {
        'host': os.environ['PGHOST'],
        'user': os.environ['PGUSER'],
        'password': os.environ['PGPASSWORD'],
        'database': os.environ['PGDATABASE']
    }
    return kwargs


def get_postgres_ibis_connection():
    kwargs = get_postgres_creds()
    conn = ibis.postgres.connect(**kwargs)
    return conn


conn = get_postgres_ibis_connection()
conn.raw_sql("drop table if exists test")

conn.raw_sql("create table test (id bigserial primary key, x float)")

for nn in range(10):
    df = pd.DataFrame({'x': [1., 2., 3.]})
    conn.insert('test', df)

t = conn.table('test')
print()
print(t.execute().to_string())
