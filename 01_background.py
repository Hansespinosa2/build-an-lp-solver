import marimo

__generated_with = "0.11.13"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"# Hi")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
