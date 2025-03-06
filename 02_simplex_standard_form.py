import marimo

__generated_with = "0.11.13"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # **Build Your Own LP Solver: Simplex Standard Form**
        This project is a step-by-step walkthrough of how to build your own LP solver.
    
        This is the third notebook in the series and will walk you through the implementation of the Simplex algorithm for solving LPs in standard form. First, we will implement the Simplex algorithm given an initial feasible solution. Then, we will implement the Two-Phase Simplex algorithm to find an initial feasible solution if one does not exist.
    
        This notebook relies heavily on `numpy` for matrix operations and `pandas` for displaying tables. Make sure you have these libraries installed before running the code. The imports are handled at the bottom of this notebook in the **File Imports** section.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## **1. Standard Form of Linear Programs**
        Before implementing the Simplex algorithm, we must ensure that our LP is in **standard form**:
    
        - **Objective Function:** Minimize or maximize a linear function.
        - **Constraints:** All constraints should be in the form of equality constraints (i.e., `Ax = b`).
        - **Non-Negativity:** All decision variables must be `≥ 0`.
    
        **Example Standard Form LP:**
        $$\text{Maximize } c^T x$$
        $$\text{subject to } Ax = b, \quad x \geq 0$$
        For this notebook, we will assume all matrices and variables are inputted in standard form.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### **1.1 Example Problem Formulation**
        In order to implement the Simplex algorithm, we will use the Problem <span style="color:blue">1.1. </span> LP from the `01_background.py` notebook. The LP is as follows:
    
        $$\text{Minimize } \mathbf{c}^\top \mathbf{x}$$
    
        $$\text{subject to } \mathbf{A}\mathbf{x} = \mathbf{b}, \quad \mathbf{x} \geq \mathbf{0}$$
    
        where:
    
        $$
        \mathbf{A} = \begin{bmatrix}
        1 & 5 & 40 & 10 & 12 & 20 & -1 & 0 & 0 & 0 \\
        10 & 1 & 6 & 9 & 5 & 3 & 0 & 1 & 0 & 0 \\
        1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 1 & 0 \\
        1 & 3 & -3 & -2 & -1 & 2 & 0 & 0 & 0 & -1
        \end{bmatrix}
        $$
    
        $$
        \mathbf{b} = \begin{bmatrix}
        20 \\
        10 \\
        200,000 \\
        0
        \end{bmatrix}
        $$
    
        $$
        \mathbf{c} = \begin{bmatrix}
        0.10 \\
        0.50 \\
        0.25 \\
        0.30 \\
        0.10 \\
        0.20 \\
        0 \\
        0 \\
        0 \\
        0
        \end{bmatrix}
        $$
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## **2. Setting Up the Initial Simplex Tableau**
        The Simplex method uses a **tableau representation** to keep track of the constraints and objective function.
        The tableau consists of:
        - The constraint matrix `A`.
        - The right-hand side `b`.
        - The cost row containing coefficients from the objective function.
        """
    )
    return


@app.cell
def _(np):
    def initialize_simplex_tableau(A, b, c):
        """Create the initial simplex tableau given A, b, and c."""
        m, n = A.shape
        tableau = np.zeros((m + 1, n + m + 1))  # Extra column for b values
        tableau[:-1, :-1] = np.hstack((A, np.eye(m)))  # Slack variables added
        tableau[:-1, -1] = b  # RHS values
        tableau[-1, :-1] = -c  # Objective function row (negated for maximization)
        return tableau
    return (initialize_simplex_tableau,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## **3. Implementing the Simplex Algorithm**
        The Simplex algorithm iterates through these steps:
        1. **Check for optimality:** If all coefficients in the objective row are non-negative, the solution is optimal.
        2. **Select the entering variable:** Choose the most negative coefficient in the objective row.
        3. **Select the leaving variable:** Use the minimum ratio test to determine which row will leave the basis.
        4. **Pivot:** Update the tableau by making the entering variable a basic variable.
        """
    )
    return


@app.cell
def _(np):
    def simplex_method(tableau):
        """Perform the Simplex algorithm given an initial tableau."""
        while np.any(tableau[-1, :-1] < 0):  # Check for optimality
            entering = np.argmin(tableau[-1, :-1])  # Most negative coefficient
            ratios = tableau[:-1, -1] / tableau[:-1, entering]
            ratios[ratios <= 0] = np.inf  # Ignore non-positive ratios
            leaving = np.argmin(ratios)  # Choose pivot row
            pivot_element = tableau[leaving, entering]
            tableau[leaving, :] /= pivot_element  # Normalize pivot row

            for i in range(len(tableau)):
                if i != leaving:
                    tableau[i, :] -= tableau[i, entering] * tableau[leaving, :]

        return tableau, tableau[:-1, -1]
    return (simplex_method,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## **4. Two-Phase Simplex Method**
        If the initial basic feasible solution is not readily available, we use **Two-Phase Simplex**:
        - **Phase 1:** Introduce artificial variables and solve an auxiliary LP to find a feasible solution.
        - **Phase 2:** Use the standard Simplex method to optimize the original objective function.
        """
    )
    return


@app.cell
def _(initialize_simplex_tableau, np, simplex_method):
    def two_phase_simplex(A, b, c):
        """Solve an LP using the Two-Phase Simplex method."""
        m, n = A.shape

        # Phase 1: Introduce artificial variables
        A_phase1 = np.hstack((A, np.eye(m)))
        c_phase1 = np.concatenate((np.zeros(n), np.ones(m)))
        tableau = initialize_simplex_tableau(A_phase1, b, c_phase1)
        tableau, _ = simplex_method(tableau)

        # Remove artificial variables and proceed with original LP
        tableau = tableau[:, :-(m + 1)]  # Remove last m columns (artificial vars)
        tableau[-1, :-1] = -c  # Restore original objective function

        return simplex_method(tableau)
    return (two_phase_simplex,)


@app.cell
def _(mo):
    mo.md(r"## **File Imports**")
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


if __name__ == "__main__":
    app.run()
