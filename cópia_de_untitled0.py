# -*- coding: utf-8 -*-
"""Cópia de Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Yo_8i2D5hE9NGp_s0DJKeea4ChjPMSlD
"""

from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [200000, 300000, 400000, 500000, 600000]

model = LinearRegression()

model.fit(X, y)

num_quartos =  7
preco_previsto = model.predict([[num_quartos]])
print(f"O valor previsto para uma casa de {num_quartos} quartos é de: ${preco_previsto[0]:.2f}")



