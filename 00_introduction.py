import marimo

__generated_with = "0.11.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Build Your Own LP Solver: Introduction
        This project is a step-by-step walkthrough of how to build your own LP solver.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Project Introduction and Overview**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### **Project Introduction**
        This project aims to provide an educational platform where users can build their own Linear Programming (LP) Simplex Solver from scratch. 
        The Simplex algorithm is one of the most widely used methods for solving LP problems, and by building it from scratch, users will gain a deeper understanding of optimization theory, linear algebra, and algorithmic implementation.
        This project has tremendous value to any students studying Industrial Engineering, Operations Research, or Computer Science.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### **Project Overview**
        This project consists of six structured files, completed in the following order:

        1. **`00_introduction.py`**: Provides an overview of the project, its goals, and required knowledge. No coding is required.
        2. **`01_background.py`** (optional): Contains exercises on Linear Programming, NumPy matrix operations, Python, and algorithm implementation. 
        3. **`02_simplex_standard_form.py`**: Guides the implementation of the Simplex algorithm for solving LP problems in standard form.
        4. **`03_lp_reductions.py`**: Introduces an object-oriented approach to converting LP problems into standard form.
        5. **`04_simplex_solver.py`**: Combines previous work into a Pythonic LP solver.
        6. **`05_conclusion.py`**: Demonstrates the solver, compares it with open-source solvers, and provides guidance on sharing and presenting the project.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## **Linear Programming Overview**
        Linear Programming is a subsection of mathematical optimization that deals with a linear objective function and a linear set of constraints.
        A *linear program* is a mathematical formulation that models a real-world problem.

        A well-known example is the *diet problem*.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### **Example Problem - Protein Shake Diet**
        Take the following example:

        You just got back from a great workout, and are making a protein shake with two ingredients, protein powder and banana.
        Your body is your temple and you would like to make sure that the amount of each ingredient you make satisfies the following criteria:

        - The overall sugar of the drink cannot exceed 20g
        - The overall protein level of the drink must be above 30g
        - Your blender cannot fit more than 500g of ingredient 


        You want to maximize the *taste* of your drink while adhering to the above constraints and the below nutrition profiles.
        You want to maximize the *taste* of your drink while adhering to the above constraints and the following nutrition profiles of the ingredients:

        | Ingredient        | Protein (g) | Sugar (g) | Weight (g) | Taste Score (arbitrary units) |
        |-------------------|-------------|-----------|------------|-----------------------------|
        | Protein Powder  (100g)  | 20          | 5         | 100        | 4                          |
        | Banana          (100g)  | 1           | 10        | 100        | 10                         |

        Where:

        - **Protein Powder**: Each 100g serving contains 20g of protein, 5g of sugar, and has a taste score of 4.
        - **Banana**: Each 100g serving contains 1g of protein, 10g of sugar, and has a taste score of 10.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **Example Formulation - Protein Shake Diet**

        Now, we can formulate this as a Linear Programming problem:

        **Objective Function**:  
        Maximize the taste score of the shake:
        $$\text{Maximize } 4x_1 + 10x_2$$
        Where:
        - $x_1$ is the amount of protein powder (in grams).
        - $x_2$ is the amount of banana (in grams).

        **Subject to the following constraints**:

        1. **Sugar constraint**:
        $5x_1 + 10x_2 \leq 20$
        (The total sugar cannot exceed 20g.)

        2. **Protein constraint**:
        $20x_1 + x_2 \geq 30$
        (The total protein must be at least 30g.)

        3. **Weight constraint**:
        $x_1 + x_2 \leq 500$
        (The total weight cannot exceed 500g.)

        4. **Non-negativity constraints**:
        $x_1 \geq 0, \quad x_2 \geq 0$
        (You can't use negative amounts of ingredients.)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## **Simplex Algorithm Overview**
        The Simplex method is a powerful algorithm used to solve LP problems. 
        In this project, we will implement the Simplex method step-by-step to build a custom LP solver.
        """
    )
    return
# Add a sliding visual interpretation of the simplex algorithm and LPs using marimo

@app.cell
def _(mo):
    mo.md(r"""
        # **The Simplex Algorithm: A Step-by-Step Overview**

        The **Simplex Algorithm** is one of the most widely used methods for solving **Linear Programming (LP) problems**. It is an iterative, **tableau-based** method that efficiently finds the optimal solution by moving along the edges of the feasible region.

        ## **1. Understanding the Simplex Algorithm**

        Given a **linear program in standard form**:

        **Objective Function**:  
        $$\text{Maximize } Z = c^T x$$

        **Subject to Constraints**:  
        $$Ax = b, \quad x \geq 0$$

        where:
        - \( x \) is the vector of **decision variables**.
        - \( A \) is the **constraint coefficient matrix**.
        - \( b \) is the **right-hand side (RHS)** vector.
        - \( c^T \) is the **cost (objective) vector**.

        The **Simplex Method** starts at a **basic feasible solution** (BFS) and iteratively improves it by pivoting between adjacent extreme points until the optimal solution is found.

        ---
        ## **2. Simplex Tableau Representation**

        We convert the standard form LP into a **Simplex Tableau**, an augmented matrix that allows efficient row operations.

        A **Simplex Tableau** for the LP:

        | Basis  | \( x_1 \) | \( x_2 \) | \( s_1 \) | \( s_2 \) | RHS  |
        |--------|------|------|------|------|------|
        | \( s_1 \)  | 2  | 1  | 1  | 0  | 4  |
        | \( s_2 \)  | 1  | 2  | 0  | 1  | 6  |
        | **Z-row** | -3  | -5  | 0  | 0  | 0  |

        - **Decision variables** (\( x_1, x_2 \)) are in columns.
        - **Slack variables** (\( s_1, s_2 \)) track excess capacity.
        - **RHS (b-column)** holds constraint values.
        - **Z-row (bottom row)** represents the negative reduced costs.

        ---
        ## **3. The Simplex Algorithm Steps**

        The algorithm follows **three key steps** iteratively until the optimal solution is reached:

        ### **Step 1: Identify Entering Variable (Pivot Column)**
        - Choose the most negative coefficient in the **Z-row** (Objective row).
        - This corresponds to the variable that **most improves the objective function**.
        - If all coefficients are **non-negative**, the current solution is **optimal**.

        $$x_{\text{enter}} = \arg\min(c_j)$$

        ### **Step 2: Identify Leaving Variable (Pivot Row)**
        - Compute the **minimum ratio test** to determine the **leaving variable**.
        - The row with the **smallest positive** \( \frac{\text{RHS}}{\text{Pivot Column}} \) value is chosen.

        $$x_{\text{leave}} = \arg\min \left( \frac{b_i}{a_{i,j}} \right), \quad a_{i,j} > 0$$

        - If no **valid positive ratios** exist, the problem is **unbounded**.

        ### **Step 3: Pivoting**
        - Perform **row operations** to make the pivot column into a **unit column**.
        - Normalize the pivot row by dividing it by the pivot element.
        - Update other rows using row reduction.

        ---
        ## **4. Iterating Until Optimality**
        - Repeat **Steps 1 to 3** until:
            - No negative coefficients remain in the Z-row (**Optimal Solution Found**).
            - No valid pivot exists (**Unbounded Solution**).
            - Degeneracy occurs (**Cycling Prevention Needed**).

        ---
        ## **5. Example Walkthrough**
        Consider the LP:

        $$\text{Maximize } Z = 3x_1 + 5x_2$$

        Subject to:

        $$2x_1 + x_2 \leq 4$$
    
        $$x_1 + 2x_2 \leq 6$$
    
        $$x_1, x_2 \geq 0$$

        **Standard Form Conversion:**
        - Introduce slack variables \( s_1, s_2 \).
        - The tableau representation is set up as shown earlier.

        The **Simplex Algorithm** iterates through pivot operations until an **optimal solution** is found.

        ---
        ## **6. Implementation Notes**
        - Commercial solvers like **Gurobi and CPLEX** use **advanced pivoting strategies**.
        - Variants like **Revised Simplex Method** and **Dual Simplex** improve performance.

        ---
        ## **7. Next Steps**
        - **Implementing the Simplex Algorithm in Python**
        - **Handling Degeneracy, Cycling, and Special Cases**
        - **Comparing Against Commercial Solvers**

        """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## **Project Dependencies**
        To follow along, ensure you have the following dependencies installed:

        ```bash
        pip install numpy pandas matplotlib cvxpy marimo
        ```
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    mo.md("""## **File Imports**""")
    return (mo,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
