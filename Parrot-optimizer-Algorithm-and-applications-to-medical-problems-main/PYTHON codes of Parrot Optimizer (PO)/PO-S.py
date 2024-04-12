'''
%___________________________________________________________________________________________________________________________________________________%
% Parrot Optimizer (PO) source codes (version 2.0)
% PO
% Parrot optimizer: Algorithm and applications to medical problems
% Website and codes of Parrot optimizer(PO):http://www.aliasgharheidari.com/PO.html

% Junbo Lian, Guohua Hui, Ling Ma, Ting Zhu, Xincan Wu, Ali Asghar Heidari, Yi Chen, Huiling Chen

% Last update: Apr 07 2024

% E-Mail: as_heidari@ut.ac.ir, aliasghar68@gmail.com, chenhuiling.jlu@gmail.com

%----------------------------------------------------------------------------------------------------------------------------------------------------%

% Authors: Junbo Lian (junbolian@qq.com), Ali Asghar Heidari(as_heidari@ut.ac.ir, aliasghar68@gmail.com), Huiling Chen(chenhuiling.jlu@gmail.com)

%----------------------------------------------------------------------------------------------------------------------------------------------------%

% After use of code, please users cite to the main paper on Parrot optimizer (PO):
% Junbo Lian, Guohua Hui, Ling Ma, Ting Zhu, Xincan Wu, Ali Asghar Heidari, Yi Chen, Huiling Chen*
% Parrot optimizer: Algorithm and applications to medical problems
% Computers in Biology and Medicine, ELSEVIER - 2024

%----------------------------------------------------------------------------------------------------------------------------------------------------%
% You can also follow the paper for related updates in researchgate:

% https://www.researchgate.net/profile/Ali_Asghar_Heidari.

% Website and codes of Parrot optimizer (PO):%  http://www.aliasgharheidari.com/PO.html

% You can also use and compare with our other new optimization methods:
                                                                       %(RIME)-2023-http://www.aliasgharheidari.com/RIME.html
																	   %(INFO)-2022- http://www.aliasgharheidari.com/INFO.html
																	   %(RUN)-2021- http://www.aliasgharheidari.com/RUN.html
                                                                       %(HGS)-2021- http://www.aliasgharheidari.com/HGS.html
                                                                       %(SMA)-2020- http://www.aliasgharheidari.com/SMA.html
                                                                       %(HHO)-2019- http://www.aliasgharheidari.com/HHO.html
%____________________________________________________________________________________________________________________________________________________%
'''

import numpy as np

def PO_S(N, Max_iter, lb, ub, dim, fobj):

    # BestF: Best value in a certain iteration
    # WorstF: Worst value in a certain iteration
    # GBestF: Global best fitness value
    # AveF: Average value in each iteration

    if np.isscalar(ub):
        ub = np.ones(dim) * ub
        lb = np.ones(dim) * lb

    # Initialization
    X0 = initialization(N, dim, ub, lb)
    X = X0

    # Compute initial fitness values
    fitness = np.zeros(N)
    for i in range(N):
        fitness[i] = fobj(X[i, :])
    index = np.argsort(fitness)
    fitness = np.sort(fitness)
    GBestF = fitness[0]
    GBestX = X[index[0], :]
    X_new = X[index, :]
    X = X_new
    curve = np.zeros(Max_iter)
    avg_fitness_curve = np.zeros(Max_iter)
    search_history = np.zeros((N, Max_iter, dim))
    fitness_history = np.zeros((N, Max_iter))

    # Start search
    for i in range(Max_iter):
        if i % 100 == 0 and i > 0:
            print(f'At iteration {i}, the fitness is {curve[i-1]}')
        avg_fitness_curve[i] = np.mean(fitness)
        alpha = np.random.rand() / 5
        sita = np.random.rand() * np.pi

        for j in range(N):
            St = np.random.randint(1, 6)
            if St == 1:
                X_new[j, :] = (X[j, :] - GBestX) * levy(dim) + np.random.rand() * np.mean(X, axis=0) * (1 - i / Max_iter) ** (2 * i / Max_iter)
            elif St == 2 or St == 5:
                X_new[j, :] = X[j, :] + GBestX * levy(dim) + np.random.randn() * (1 - i / Max_iter) * np.ones(dim)
            elif St == 3:
                H = np.random.rand()
                if H < 0.5:
                    X_new[j, :] = X[j, :] + alpha * (1 - i / Max_iter) * (X[j, :] - np.mean(X, axis=0))
                else:
                    X_new[j, :] = X[j, :] + alpha * (1 - i / Max_iter) * np.exp(-j / (np.random.rand() * Max_iter))
            else:
                X_new[j, :] = X[j, :] + np.random.rand() * np.cos((np.pi * i) / (2 * Max_iter)) * (GBestX - X[j, :]) - np.cos(sita) * (i / Max_iter) ** (2 / Max_iter) * (X[j, :] - GBestX)

            # Boundary control
            X_new[j, :] = np.clip(X_new[j, :], lb, ub)

            # Finding the best location so far
            if fobj(X_new[j, :]) < GBestF:
                GBestF = fobj(X_new[j, :])
                GBestX = X_new[j, :]

        # Update positions and fitness
        fitness_new = np.array([fobj(ind) for ind in X_new])
        for s in range(N):
            if fitness_new[s] < GBestF:
                GBestF = fitness_new[s]
                GBestX = X_new[s, :]
        X = X_new
        fitness = fitness_new

        # Sorting and updating
        index = np.argsort(fitness)
        fitness = np.sort(fitness)
        X = X[index, :]
        curve[i] = GBestF
        search_history[:, i, :] = X
        fitness_history[:, i] = fitness

    Best_pos = GBestX
    Best_score = GBestF
    return avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history


def levy(d):
    beta = 1.5
    sigma = (np.math.gamma(1 + beta) * np.sin(np.pi * beta / 2) / (
                np.math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
    u = np.random.randn(1, d) * sigma
    v = np.random.randn(1, d)
    step = u / np.power(np.abs(v), (1 / beta))
    return step

def initialization(N, dim, ub, lb):
    return np.random.rand(N, dim) * (ub - lb) + lb



