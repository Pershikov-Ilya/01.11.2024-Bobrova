import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
T_prib = 7  # Среднее время прибытия (в минутах)
T_obsl = 9  # Среднее время обслуживания (в минутах)
T_rab = 480  # Период функционирования системы в минутах (8 часов = 480 минут)
C1 = 500  # Средняя стоимость покупки (в рублях)
C2_base = 1000  # Базовая стоимость обслуживания одного канала (в рублях)
N_channels = np.arange(1, 6)  # Количество каналов обслуживания от 1 до 5

# Интенсивности обслуживания и прибытия
lambda_prib = 1 / T_prib  # Интенсивность прибытия клиентов
lambda_obsl = 1 / T_obsl  # Интенсивность обслуживания клиентов


# Функция расчета количества обслуженных клиентов
def calculate_served_clients(N):
    rho = lambda_prib / (N * lambda_obsl)  # Коэффициент загрузки канала
    if rho >= 1:
        return 0  # Если система перегружена, обслуживание невозможно
    return int(N * lambda_obsl * T_rab * (1 - rho))  # Ожидаемое число обслуженных клиентов


# Функция издержек обслуживания для заданного количества каналов
def service_cost(N):
    return C2_base * (1 - 0.5 * N + 0.5 * N ** 2)


# Расчёты для графиков чистой прибыли и средней относительной прибыли
total_profits = []  # Для хранения значений чистой прибыли C
average_relative_profits = []  # Для хранения значений средней относительной прибыли C_cp.отн

for N in N_channels:
    # Количество обслуженных клиентов при N каналах
    N_served = calculate_served_clients(N)

    # Чистая прибыль C = суммарный доход - издержки
    revenue = N_served * C1  # Общий доход
    cost = service_cost(N)  # Общие издержки на обслуживание
    total_profit = revenue - cost
    total_profits.append(total_profit)

    # Средняя относительная прибыль
    average_served_clients = N_served  # Среднее количество обслуженных клиентов
    average_relative_profit = average_served_clients - (cost / C1)
    average_relative_profits.append(average_relative_profit)

# Построение графика зависимости чистой прибыли от количества каналов (рис. 1)
plt.figure(figsize=(10, 6))
plt.plot(N_channels, total_profits, marker='o', color='g', label="Чистая прибыль C")
plt.xlabel("Количество каналов обслуживания")
plt.ylabel("Чистая прибыль (руб)")
plt.title("Зависимость чистой прибыли от количества каналов обслуживания")
plt.grid()
plt.legend()
plt.show()

# Построение графика зависимости средней относительной прибыли от количества каналов (рис. 2)
plt.figure(figsize=(10, 6))
plt.plot(N_channels, average_relative_profits, marker='o', color='b', label="Средняя относительная прибыль C_ср.отн")
plt.xlabel("Количество каналов обслуживания")
plt.ylabel("Средняя относительная прибыль")
plt.title("Зависимость средней относительной прибыли от количества каналов обслуживания")
plt.grid()
plt.legend()
plt.show()