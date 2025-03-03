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
    mo.md(r"""
        ## **Project Introduction and Overview**
    """)
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
    mo.md(r"""
        ### **Project Overview**
        There are a total of 6 files associated with this project.
        There are 6 files to completed in the following order:

        1. `00_introduction.py`: This file will cover an introduction of the project and the concepts applied throughout.
        This section contains no coding and is purely to give an overview of the value, effort, and knowledge this project will build.
        2. `01_background.py` (optional): This file contains optional exercises that serve as a review to anyone who already feels comfortable with the concepts, or an introduction to the concepts for those who are interested in learning the concepts from the beginning.
        There are questions relating to Linear Programming, Matrix Manipulation withg NumPy, Python, and Algorithm Implementation.
        These questions are not directly necessary for the completion of the project, but understanding of them signifies a general understanding of the concepts used throughout the project.
        3. `02_simplex_standard_form.py`: This file will guide you through an implementation of the Simplex algorithm from a Standard Form LP.
        4. `03_lp_reductions.py`: This file will guide you through an Object-Oriented Programming (OOP) method of reducing any inputted LP model into Standard Form.
        5. `04_simplex_solver.py`: This file will guide you through combining the previous work into a packaged Solver with a Pythonic modeling language.
        6. `05_conclusion.py`: This file will demonstrate the Solver created previously and compare with other Open Source solvers. This file will also guide you in how to display and distribute the work done in this project to demonstrate the skills and knowl
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Linear Programming Overview
    Linear Programming is a subsection of mathematical optimization that deals with a linear objective function and a linear set of contraints.
    A *linear program* is a set of mathematical expressions that translate and represent a real-world problem. 

    A very famous toy example is the *diet problem*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### Example Problem - Protein Shake Diet 
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


    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" ### Formulating the Linear Program

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
    (You can't use negative amounts of ingredients.)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""



        ## Simplex Algorithm Overview
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Project Dependencies
        """
         )
    return


@app.cell
def _():
    import marimo as mo
    mo.md("""## File Imports""")
    return (mo,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
