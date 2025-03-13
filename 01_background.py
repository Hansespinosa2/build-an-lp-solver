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
    mo.md(
        r"""
        ### **1.1. Protein Shake Formulation**
        Consider an extension of the protein shake problem from the `00_introduction.py` file. This extension expands the problem to be from the point of view of a company that produces protein shakes. The company has the following ingredients available to them:
    
    
    
        | Ingredient             | Protein (g) | Sugar (g) | Weight (g) | Taste Score | Cost ($) |
        |------------------------|-------------|-----------|------------|-------------|----------|
        | Banana (100g)          | 1           | 10        | 100        | 8           |  0.10    |
        | Cocoa Powder (100g)    | 5           | 1         | 100        | 10          |  0.50    |
        | Whey (100g)            | 40          | 6         | 100        | 4           |  0.25    |
        | Soy (100g)             | 10          | 9         | 100        | 5           |  0.30    |
        | Milk (100g)            | 12          | 5         | 100        | 6           |  0.10    |
        | Peanut Butter (100g)   | 20          | 3         | 100        | 9           |  0.20    |
    
        Based off of their marketing and consumer demand information, they would like to make a protein shake that meets the following criteria:
    
        - At least 20g of protein
        - At most 10g of sugar
        - Meets consumer demand of at least 20,000 kg of protein shakes (each shake weighs 500g)
        - At least a taste score of 7
    
        The company would like to minimize the cost of the protein shake.
    
        **Exercise:** Formulate the above problem as a linear program.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        #### **1.1. Solution to Protein Shake Formulation**
    
        To formulate the protein shake problem as a linear program, we define the following variables:
    
        Let  $x_1$ be the amount of Banana (100g) in the shake.
        Let $x_2$ be the amount of Cocoa Powder (100g) in the shake.
        Let $x_3$ be the amount of Whey (100g) in the shake.
        Let $x_4$ be the amount of Soy (100g) in the shake.
        Let $x_5$ be the amount of Milk (100g) in the shake.
        Let $x_6$ be the amount of Peanut Butter (100g) in the shake.
    
        The objective is to minimize the cost of the protein shake:
    
        $$\text{Minimize } 0.10x_1 + 0.50x_2 + 0.25x_3 + 0.30x_4 + 0.10x_5 + 0.20x_6$$
    
        Subject to the following constraints:
    
        $$1x_1 + 5x_2 + 40x_3 + 10x_4 + 12x_5 + 20x_6 \geq 20 \textit{ (Protein Constraint)}$$ 
    
        $$10x_1 + 1x_2 + 6x_3 + 9x_4 + 5x_5 + 3x_6 \leq 10 \textit{ (Sugar Constraint)}$$
    
        $$x_1 + x_2 + x_3 + x_4 + x_5 + x_6 \geq 200,000 \textit{ (Demand Constraint)}$$
    
        $$8x_1 + 10x_2 + 4x_3 + 5x_4 + 6x_5 + 9x_6 \geq 7(x_1 + x_2 + x_3 + x_4 + x_5 + x_6) \textit{ (Taste Constraint)}$$
    
        $$x_1, x_2, x_3, x_4, x_5, x_6 \geq 0 \textit{ (Non-Negativity Constraint)}$$
    
        *Note: Depending on the specific unit of measurement chosen (kg, g, 100g), your answer may look slightly different.*
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### **1.2. Standard Form Protein Shake**
        Standard form is a way to represent a linear program in a more general form. The standard form of a linear program is as follows:
    
        $$\text{Minimize } c^Tx$$
    
        $$\text{Subject to }  Ax = b$$
    
        $$x \geq 0$$
    
        **Exercise:** Convert the protein shake problem from [1.1.](#1.1.-Protein-Shake-Formulation)  into standard form.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        #### **1.2. Solution to Standard Protein Shake**
        To convert the protein shake problem into standard form, we first distribute and rearrange the  *taste* constraint so all variables are in the left side of either the inequality:
    
        $$x_1 + 3x_2 -3x_3 -2x_4 -x_5 + 2x_6 \geq 0 \textit{ (Rearranged Taste Constraint)}$$
    
        Next we convert each inequality into an equality by introducing slack variables (-) for $\geq$ inequalities and surplus variables (+) for $\leq$ inequalities:
    
        $$1x_1 + 5x_2 + 40x_3 + 10x_4 + 12x_5 + 20x_6 - s_1 = 20 \textit{ (Protein Constraint)}$$
    
        $$10x_1 + 1x_2 + 6x_3 + 9x_4 + 5x_5 + 3x_6 + s_2 = 10 \textit{ (Sugar Constraint)}$$
    
        $$x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + s_3 = 200,000 \textit{ (Demand Constraint)}$$
    
        $$x_1 + 3x_2 -3x_3 -2x_4 -x_5 + 2x_6 - s_4 = 0 \textit{ (Rearranged Taste Constraint)}$$
    
        Finally, we combine all the constraints into a matrix form:
    
        $$
        A = \begin{bmatrix}
        1 & 5 & 40 & 10 & 12 & 20 & -1 & 0 & 0 & 0 \\
        10 & 1 & 6 & 9 & 5 & 3 & 0 & 1 & 0 & 0 \\
        1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 1 & 0 \\
        1 & 3 & -3 & -2 & -1 & 2 & 0 & 0 & 0 & -1
        \end{bmatrix}
        $$
    
        $$
        b = \begin{bmatrix}
        20 \\
        10 \\
        200,000 \\
        0
        \end{bmatrix}
        $$
    
        $$
        c = \begin{bmatrix}
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
    mo.md(r"## **2. Python Exercises**")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### **2.1. Linear Programming Classes**
        We can use an Object-Oriented Programming (OOP) approach to facilitate the way that we build the LP solver later in this tutorial.
        In this problem, we will build our own implementations of a few classes to help the way we perform the reductions in the `03_lp_reductions.py` notebook.
    
        **Exercise**: Implement a class called `ScalarParameter` with the following attributes:
    
        - The class should be initialized with a required `value` attribute and an optional `name` string attribute with a default of "unnamed".
        - The class should have a `shape` attribute. *The shape will always be 1 since this is a scalar parameter*
        - Override the `__add__` method to increase the `value` attribute when two parameters are added.
    
        To check if you implemented this correctly, the following code should work:
    
        ```
        a = ScalarParameter(value=4, name="alpha")
        b = ScalarParameter(value=3)
    
        a = a + b
    
        print(a.value, a.name)
        >>> 7 alpha
        ```
        """
    )
    return


@app.cell
def _():
    #### 2.1. Solution to Linear Programming Classes
    class ScalarParameter():
        def __init__(self, value, name:str="unnamed"):
            self.value = value
            self.name = name
            self.shape = 1

        def __add__(self, other):
            new_scalar_param = ScalarParameter(self.value + other.value, name=self.name)
            return new_scalar_param

    a = ScalarParameter(value=4, name="alpha")
    b = ScalarParameter(value=3)

    a = a + b

    print(a.value, a.name)
    return ScalarParameter, a, b


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
    mo.md(r"### ****")
    return


@app.cell
def _(mo):
    mo.md(r"## **4. Algorithm Exercises**")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### **4.1. The Art of Linear Programming Video**
        **Exercise:** Watch this excellent visual introduction to linear programming and the Simplex method by Tomas Slama:
        [The Art of Linear Programming](https://www.youtube.com/watch?v=E72DWgKP_1Y)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"### **4.2. Simplex Algorithm**")
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
