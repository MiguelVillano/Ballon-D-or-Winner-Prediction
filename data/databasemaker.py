import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    from sqlalchemy import create_engine

    return (pd,)


@app.cell
def _(pd):
    players_df = pd.read_csv("rawdata/")
    ballondor_df = pd.read_csv("rawdata/")
    return


if __name__ == "__main__":
    app.run()
