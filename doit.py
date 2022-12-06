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

# Both integer and uuid currently failing
try_uuid = False
if try_uuid:
    conn.raw_sql("create table test (id uuid, x float, PRIMARY KEY (id))")
else:
    conn.raw_sql("create table test (id integer, x float, PRIMARY KEY (id))")

# Works
df = pd.DataFrame({'id': [1, 2, 3], 'x': [1., 2., 3.]})
conn.insert('test', df)

# Fails
df = pd.DataFrame({'x': [1., 2., 3.]})
conn.insert('test', df)
