import marimo

__generated_with = "0.11.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Build Your Own LP Solver: Introduction
        This project is a step-by-step walkthrough of how to build your own LP solver.

        This notebook is the first in a series of tutorial notebooks that will guide you in your own implementation of the Simplex algorithm to solve linear programming problems.
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        ## **Simplex Algorithm Overview**
        The Simplex method is a powerful algorithm used to solve LP problems. 
        In this project, we will implement the Simplex method step-by-step to build a custom LP solver.

        The **Simplex Algorithm** is one of the most widely used methods for solving **Linear Programming (LP) problems**. It is an iterative, **tableau-based** method that efficiently finds the optimal solution by moving along the edges of the feasible region.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### **Visualizing the Simplex Algorithm**
        Use the below slider and corresponding to visual to visualize the way the Simplex algorithm moves along the edges of the feasible region
        """
    )
    return


@app.cell(hide_code=True)
def _(mo, np):

    vertices = [
        [0, 0, 200],
        [0, 100, 200],
        [200,50,300],
        [300,200,-100],
        [300, 300, -200],
    ]
    vertex_values = np.arange(0,len(vertices))


    simplex_slider = mo.ui.slider(steps=vertex_values,show_value=True,label="Vertex")

    simplex_slider
    return simplex_slider, vertex_values, vertices


@app.cell(hide_code=True)
def _(np, plt, simplex_slider, vertices):
    from matplotlib.colors import colorConverter

    edgecolor = colorConverter.to_rgba('k', alpha=.1)

    # Define the constraints
    def constraint_1(x1):
        return 200 - x1

    def constraint_2(x2):
        return 300 - x2

    def constraint_3(x1, x2):
        return 400 - (x1 + x2)

    def constraint_4(x2, x3):
        return 600 - (x2 + 3*x3)


    def plot_polyhedron(vertex_index):
        # Create a grid of x1, x2, x3 values to check the feasibility region
        x1_vals = np.linspace(0, 300, 10)
        x2_vals = np.linspace(0, 300, 10)
        x3_vals = np.linspace(0, 300, 10)

        # Create meshgrid for plotting
        X1, X2 = np.meshgrid(x1_vals, x2_vals)
        X3 = np.zeros_like(X1)

        # Apply constraints
        for i in range(len(x1_vals)):
            for j in range(len(x2_vals)):
                x1 = X1[i,j]
                x2 = X2[i,j]
                # Define maximum possible x3 value based on constraints
                x3_1 = constraint_1(x1)
                x3_2 = constraint_2(x2)
                x3_3 = constraint_3(x1, x2)
                x3_4 = constraint_4(x2, 0)
                X3[i,j] = min(x3_1, x3_2, x3_3, x3_4)
                x3 = X3[i,j]


        vertex_to_add = vertices[vertex_index]


        # Create the plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X1, X2, X3, cmap='viridis', edgecolor=edgecolor,alpha=1,zorder=1)

        # Add the selected vertex as a red point
        ax.scatter(vertex_to_add[0], vertex_to_add[1], vertex_to_add[2], color='r', s=50,zorder=20)

        for i in range(1, vertex_index + 1):
            ax.plot([vertices[i-1][0], vertices[i][0]], 
                    [vertices[i-1][1], vertices[i][1]], 
                    [vertices[i-1][2], vertices[i][2]], color='r',
                    linewidth=5, linestyle=":",zorder=5)

        # Label the axes
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('x3')

        plt.title("Simplex Visualization")

        # Show the plot
        plt.show()

    plot_polyhedron(simplex_slider.value)
    return (
        colorConverter,
        constraint_1,
        constraint_2,
        constraint_3,
        constraint_4,
        edgecolor,
        plot_polyhedron,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **1. Understanding the Simplex Algorithm**
        Given a **linear program in standard form**:

        **Objective Function**:  
        $$\text{Minimize } c^T x$$

        **Subject to Constraints**:  
        $$Ax = b, \quad x \geq 0$$

        where:

        - $x$ is the vector of **decision variables**.
        - $A$ is the **constraint coefficient matrix**.
        - $b$ is the **right-hand side (RHS)** vector.
        -  $c^T$ is the **cost (objective) vector**.

        The **Simplex Method** starts at a **basic feasible solution** (BFS) and iteratively improves it by pivoting between adjacent extreme points until the optimal solution is found.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **2. Simplex Tableau Representation**

        We convert the standard form LP into a **Simplex Tableau**, an augmented matrix that allows efficient row operations.

        A **Simplex Tableau** for the LP:

        | Basis  |  $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS  |
        |--------|------|------|------|------|------|
        | $s_1$  | 2  | 1  | 1  | 0  | 4  |
        | $s_2$  | 1  | 2  | 0  | 1  | 6  |
        | **Reduced Costs** | -3  | -5  | 0  | 0  | 0  |

        - **Decision variables** (\( x_1, x_2 \)) are in columns.
        - **Slack variables** (\( s_1, s_2 \)) track excess capacity.
        - **RHS (b-column)** holds constraint values.
        - **Reduced Costs** represents the negative reduced costs.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **3. The Simplex Algorithm Steps**

        The algorithm follows **three key steps** iteratively until the optimal solution is reached:

        #### **Step 1: Identify Entering Variable (Pivot Column)**
        - Choose the most negative coefficient in the **Z-row** (Objective row).
               -  *Note: There exist many other criteria to determine the entering variable, which we be explored in the code later in this tutorial.*
        - This corresponds to the variable that **most improves the objective function**.
        - If all coefficients are **non-negative**, the current solution is **optimal**.

        $$x_{\text{enter}} = \arg\min(c_j)$$

        #### **Step 2: Identify Leaving Variable (Pivot Row)**
        - Compute the **minimum ratio test** to determine the **leaving variable**.
        - The row with the **smallest positive**  $\frac{\text{RHS}}{\text{Pivot Column}}$ value is chosen.

        $$x_{\text{leave}} = \arg\min \left( \frac{b_i}{a_{i,j}} \right), \quad a_{i,j} > 0$$

        - If no **valid positive ratios** exist, the problem is **unbounded**.

        #### **Step 3: Pivoting**
        - Perform **row operations** to make the pivot column into a **unit column**.
        - Normalize the pivot row by dividing it by the pivot element.
        - Update other rows using row reduction.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **4. Iterating Until Optimality**
        - Repeat **Steps 1 to 3** until:
            - No negative coefficients remain in the Z-row (**Optimal Solution Found**).
            - No valid pivot exists (**Unbounded Solution**).
            - Degeneracy occurs (**Cycling Prevention Needed**).
                - *Note: Ignore cycling for now*
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **5. Example Walkthrough**
        Consider the LP:

        $$\text{Minimize } Z = 3x_1 + 5x_2$$

        Subject to:

        $$2x_1 + x_2 \leq 4$$

        $$x_1 + 2x_2 \leq 6$$

        $$x_1, x_2 \geq 0$$

        **Standard Form Conversion:**
        - Introduce slack variables \( s_1, s_2 \).
        - The tableau representation is set up as shown earlier.

        The **Simplex Algorithm** iterates through pivot operations until an **optimal solution** is found.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### **6. Implementation Notes**
        - Commercial solvers like **Gurobi and CPLEX** use **advanced pivoting strategies**.
        - Variants like **Revised Simplex Method** and **Dual Simplex** improve performance.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## **Project Dependencies**
        To follow along, ensure you have the following dependencies installed:

        ```bash
        pip install numpy pandas matplotlib cvxpy marimo
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **File Imports**""")
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    return Axes3D, mo, np, plt


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
