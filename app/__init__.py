from flask import Flask
import pandas as pd
import logging as lg

from .views import app
from .models import cast_dataframe_types, Car, db

@app.cli.command()
def init_db():
    db.drop_all()
    db.create_all()
    df = pd.read_csv(app.config['DATABASE_CSV'], index_col=0)
    df = cast_dataframe_types(df)
    for _, row in df.iterrows():
        db.session.add(Car(row))
    db.session.commit()
    lg.warning('Database initialized!')