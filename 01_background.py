import marimo

__generated_with = "0.11.13"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # **Build Your Own LP Solver: Background**
        This project is a step-by-step walkthrough of how to build your own LP solver.
    
        This is the second notebook in the series and is an optional file filled with exercises on Linear Programming, Python, Matrices, and algorithm implementation. Although these exercises are optional, they are **highly recommended** to solidify your understanding of the concepts discussed in the main notebook.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"## **1. Linear Programming Exercises**")
    return


@app.cell
def _(mo):
    mo.md(r"### **1.1. Protein Shake Formulation**")
    return


@app.cell
def _(mo):
    mo.md(r"## **2. Python Exercises**")
    return


@app.cell
def _(mo):
    mo.md(r"### **2.1. Python Basics**")
    return


@app.cell
def _(mo):
    mo.md(r"## **3. NumPy Matrix Exercises**")
    return


@app.cell
def _(mo):
    mo.md(r"### **3.1. Matrix Operations**")
    return


@app.cell
def _(mo):
    mo.md(r"## **4. Algorithm Exercises**")
    return


@app.cell
def _(mo):
    mo.md(r"### **4.1. Simplex Algorithm**")
    return


@app.cell
def _(mo):
    mo.md(r"## File Imports")
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


if __name__ == "__main__":
    app.run()
