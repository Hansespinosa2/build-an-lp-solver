import marimo

__generated_with = "0.11.13"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Build Your Own LP Solver: Background
        This project is a step-by-step walkthrough of how to build your own LP solver.
    
        This is the second notebook in the series and is an optional file filled with exercises on Linear Programming, Matrices, Python, and algorithm implementation.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
