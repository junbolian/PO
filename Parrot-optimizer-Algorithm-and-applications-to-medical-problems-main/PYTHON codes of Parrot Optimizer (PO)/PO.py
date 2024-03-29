'''
%___________________________________________________________________________________________________________________________________________________%
% Parrot Optimizer (PO) source codes (version 1.0)
% PO
% Parrot optimizer: Algorithm and applications to medical problems
% Website and codes of Parrot optimizer(PO):http://www.aliasgharheidari.com/PO.html

% Junbo Lian, Guohua Hui, Ling Ma, Ting Zhu, Xincan Wu, Ali Asghar Heidari, Yi Chen, Huiling Chen

% Last update: Jan 31 2023

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


def PO(N, Max_iter, lb, ub, dim, fobj):
    # BestF: Best value in a certain iteration
    # WorstF: Worst value in a certain iteration
    # GBestF: Global best fitness value
    # AveF: Average value in each iteration

    if np.max(np.size(ub)) == 1:
        ub = np.multiply(np.ones(dim), ub)
        lb = np.multiply(np.ones(dim), lb)

    # Initialization
    X0 = initialization(N, dim, ub, lb)  # Initialization
    X = X0

    # Compute initial fitness values
    fitness = np.zeros(N)
    for i in range(N):
        fitness[i] = fobj(X[i, :])
    index = np.argsort(fitness)  # sort
    fitness = np.sort(fitness)
    GBestF = fitness[0]  # Global best fitness value
    AveF = np.mean(fitness)
    for i in range(N):
        X[i, :] = X0[index[i], :]
    curve = np.zeros(Max_iter)
    avg_fitness_curve = np.zeros(Max_iter)
    GBestX = X[0, :]  # Global best position
    X_new = X
    search_history = np.zeros((N, Max_iter, dim))
    fitness_history = np.zeros((N, Max_iter))

    # Start search
    for i in range(Max_iter):
        if i % 100 == 0:
            print('At iteration ', i, ' the fitness is ', curve[i - 1])
        avg_fitness_curve[i] = AveF
        alpha = np.random.rand() / 5
        sita = np.random.rand() * np.pi
        for j in range(X.shape[0]):
            St = np.random.randint(1, 5)
            # foraging behavior
            if St == 1:
                X_new[j, :] = (X[j, :] - GBestX) * Levy(dim) + np.random.rand() * np.mean(X) * (
                            1 - i / Max_iter) ** (2 * i / Max_iter)

            # staying behavior
            elif St == 2:
                X_new[j, :] = X[j, :] + GBestX * Levy(dim) + np.random.randn() * (1 - i / Max_iter) * np.ones(dim)

            # communicating behavior
            elif St == 3:
                H = np.random.rand()
                if H < 0.5:
                    X_new[j, :] = X[j, :] + alpha * (1 - i / Max_iter) * (X[j, :] - np.mean(X))
                else:
                    X_new[j, :] = X[j, :] + alpha * (1 - i / Max_iter) * np.exp(-j / (np.random.rand() * Max_iter))
            # fear of strangers' behavior
            else:
                X_new[j, :] = X[j, :] + np.random.rand() * np.cos((np.pi * i) / (2 * Max_iter)) * (
                            GBestX - X[j, :]) - np.cos(sita) * (i / Max_iter) ** (2 / Max_iter) * (
                                          X[j, :] - GBestX)

            # Boundary control
            for a in range(dim):
                X_new[j, a] = min(ub[a], max(lb[a], X_new[j, a]))

            # Update positions
            fitness_new = np.zeros(N)
            for j in range(N):
                fitness_new[j] = fobj(X_new[j, :])

            for j in range(N):
                if fitness_new[j] < GBestF:
                    GBestF = fitness_new[j]
                    GBestX = X_new[j, :]
            X = X_new
            fitness = fitness_new

            # Sorting and updating
            index = np.argsort(fitness)  # sort
            fitness = np.sort(fitness)
            for j in range(N):
                X[j, :] = X[index[j], :]
            curve[i] = GBestF

        Best_pos = GBestX
        Best_score = curve[-1]
        search_history[:, i, :] = X
        fitness_history[:, i] = fitness

    return avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history

def Levy(d):
    beta = 1.5
    sigma = (np.math.gamma(1 + beta) * np.sin(np.pi * beta / 2) / (
                np.math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
    u = np.random.randn(1, d) * sigma
    v = np.random.randn(1, d)
    step = u / np.power(np.abs(v), (1 / beta))
    return step

def initialization(N, dim, ub, lb):
    return np.random.rand(N, dim) * (ub - lb) + lb

'''

def test_function(x):
    # this is a simple test function
    return sum(x**2)

# parameter set
N = 50  
Max_iter = 1000 
lb = -10 
ub = 10  
dim = 10  

avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history = PO(N, Max_iter, lb, ub, dim, test_function)

print("Best Position：", Best_pos)
print("Best Score：", Best_score)

'''
