import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import ttk

df_total = pd.read_csv('producao_total_leite.csv')
df_regiao = pd.read_csv('producao_regiao_leite.csv')
df_estado = pd.read_csv('producao_estado_leite.csv')

root = tk.Tk()
root.title("Análise da Produção de Leite")

explanation_frame = tk.Frame(root)
explanation_frame.pack()

explanation_label = tk.Label(explanation_frame, font=('Arial', 12), text="Bem-vindo à análise da produção de leite no Brasil!\n\nOs dados apresentados incluem:\n- Produção total de leite por ano\n- Produção de leite por região (Brasil, Sudeste, Sul, Nordeste, Centro-Oeste, Norte)\n- Produção de leite por estado (Minas Gerais, Paraná, Rio Grande do Sul, \nSanta Catarina, Goiás, São Paulo, Bahia, Pernambuco, Ceará, Rondônia)\n\nOs gráficos disponíveis são:\n1. Produção de Leite por Região\n2. Produção de Leite por Ano e por Região\n3. Distribuição de Produção por Ano\n4. Produção de Leite por Estado\n5. Correlação entre Produção e Ano\n6. Previsão de Produção\n7. Tela Única\n\nPor favor, selecione o gráfico que deseja visualizar abaixo.")
explanation_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

current_choice = 0

def show_graph(choice):
    global current_choice
    current_choice = choice

    def plot_graph():
        plt.ion()

        if current_choice == 1:
            plt.figure(num="Produção de Leite por Região", figsize=(12, 8))
            sns.barplot(x='regiao', y='producao', data=df_regiao, palette='viridis')
            plt.title('Produção de Leite por Região')
            plt.xlabel('Região')
            plt.ylabel('Produção (milhões de litros)')
        elif current_choice == 2:
            plt.figure(num="Produção de Leite por Ano e por Região", figsize=(12, 8))
            sns.lineplot(x='ano', y='producao', hue='regiao', data=df_regiao, palette='tab10', marker='o')
            plt.title('Produção de Leite por Ano e por Região')
            plt.xlabel('Ano')
            plt.ylabel('Produção (milhões de litros)')
            plt.legend(title='Região')
        elif current_choice == 3:
            plt.figure(num="Distribuição de Produção por Ano", figsize=(12, 8))
            sns.histplot(df_total['producao'], bins=15, kde=True, color='skyblue')
            plt.title('Distribuição de Produção por Ano')
            plt.xlabel('Produção (milhões de litros)')
            plt.ylabel('Frequência')
        elif current_choice == 4:
            plt.figure(num="Produção de Leite por Estado", figsize=(12, 8))
            sns.barplot(x='estado', y='producao', data=df_estado, palette='coolwarm', ci=None)
            plt.title('Produção de Leite por Estado')
            plt.xlabel('Estado')
            plt.ylabel('Produção (milhões de litros)')
            plt.xticks(rotation=45)
        elif current_choice == 5:
            plt.figure(num="Correlação entre Produção e Ano", figsize=(12, 8))
            sns.regplot(x='ano', y='producao', data=df_total, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
            plt.title('Correlação entre Produção e Ano')
            plt.xlabel('Ano')
            plt.ylabel('Produção (milhões de litros)')
        elif current_choice == 6:
            X = df_total[['ano']]
            y = df_total['producao']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)

            new_data = pd.DataFrame({'ano': [2023]})
            predicted_production = model.predict(new_data)

            plt.figure(num="Previsão de Produção", figsize=(12, 8))
            sns.scatterplot(x='ano', y='producao', data=df_total, color='blue')
            plt.plot(new_data['ano'], predicted_production, 'ro', label='Previsão para 2023')
            plt.title('Previsão de Produção')
            plt.xlabel('Ano')
            plt.ylabel('Produção (milhões de litros)')
            plt.legend()
        elif current_choice == 7:

            fig, axes = plt.subplots(2, 3, figsize=(16, 10), num="Todos os gráficos para a visualização")
            fig.tight_layout(pad=3.0)

            sns.barplot(x='regiao', y='producao', data=df_regiao, palette='viridis', ax=axes[0, 0])
            axes[0, 0].set_title('Produção de Leite por Região')
            axes[0, 0].set_xlabel('Região')
            axes[0, 0].set_ylabel('Produção (milhões de litros)')

            sns.lineplot(x='ano', y='producao', hue='regiao', data=df_regiao, palette='tab10', marker='o', ax=axes[0, 1])
            axes[0, 1].set_title('Produção de Leite por Ano e por Região')
            axes[0, 1].set_xlabel('Ano')
            axes[0, 1].set_ylabel('Produção (milhões de litros)')
            axes[0, 1].legend(title='Região')

            sns.histplot(df_total['producao'], bins=15, kde=True, color='skyblue', ax=axes[0, 2])
            axes[0, 2].set_title('Distribuição de Produção por Ano')
            axes[0, 2].set_xlabel('Produção (milhões de litros)')
            axes[0, 2].set_ylabel('Frequência')

            sns.barplot(x='estado', y='producao', data=df_estado, palette='coolwarm', ci=None, ax=axes[1, 0])
            axes[1, 0].set_title('Produção de Leite por Estado')
            axes[1, 0].set_xlabel('Estado')
            axes[1, 0].set_ylabel('Produção (milhões de litros)')
            axes[1, 0].tick_params(axis='x', rotation=45)

            sns.regplot(x='ano', y='producao', data=df_total, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'}, ax=axes[1, 1])
            axes[1, 1].set_title('Correlação entre Produção e Ano')
            axes[1, 1].set_xlabel('Ano')
            axes[1, 1].set_ylabel('Produção (milhões de litros)')

            X = df_total[['ano']]
            y = df_total['producao']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)

            new_data = pd.DataFrame({'ano': [2023]})
            predicted_production = model.predict(new_data)

            axes[1, 2].scatter(df_total['ano'], df_total['producao'], color='blue')
            axes[1, 2].plot(new_data['ano'], predicted_production, 'ro', label='Previsão para 2023')
            axes[1, 2].set_title('Previsão de Produção')
            axes[1, 2].set_xlabel('Ano')
            axes[1, 2].set_ylabel('Produção (milhões de litros)')
            axes[1, 2].legend()

            single_window.mainloop()

    plot_graph()

button1 = tk.Button(button_frame, text="Produção de Leite por Região", command=lambda: show_graph(1), font=('Arial', 12))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(button_frame, text="Produção de Leite por Ano e por Região", command=lambda: show_graph(2), font=('Arial', 12))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(button_frame, text="Distribuição de Produção por Ano", command=lambda: show_graph(3), font=('Arial', 12))
button3.grid(row=0, column=2, padx=10, pady=10)

button4 = tk.Button(button_frame, text="Produção de Leite por Estado", command=lambda: show_graph(4), font=('Arial', 12))
button4.grid(row=1, column=0, padx=10, pady=10)

button5 = tk.Button(button_frame, text="Correlação entre Produção e Ano", command=lambda: show_graph(5), font=('Arial', 12))
button5.grid(row=1, column=1, padx=10, pady=10)

button6 = tk.Button(button_frame, text="Previsão de Produção", command=lambda: show_graph(6), font=('Arial', 12))
button6.grid(row=1, column=2, padx=10, pady=10)

button7 = tk.Button(button_frame, text="Todos os Gráficos", command=lambda: show_graph(7), font=('Arial', 12))
button7.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
