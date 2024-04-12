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

function [avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history] = PO_S(N, Max_iter, lb, ub, dim, fobj)

% BestF: Best value in a certain iteration
% WorstF: Worst value in a certain iteration
% GBestF: Global best fitness value
% AveF: Average value in each iteration

if (max(size(ub)) == 1)
    ub = ub .* ones(1, dim);
    lb = lb .* ones(1, dim);
end

%% Initialization
X0 = initialization(N, dim, ub, lb); % Initialization
X = X0;

% Compute initial fitness values
fitness = zeros(1, N);
for i = 1:N
    fitness(i) = fobj(X(i, :));
end
[fitness, index] = sort(fitness); % sort
GBestF = fitness(1); % Global best fitness value
AveF = mean(fitness);
for i = 1:N
    X(i, :) = X0(index(i), :);
end
curve = zeros(1, Max_iter);
avg_fitness_curve = zeros(1, Max_iter);
GBestX = X(1, :); % Global best position
X_new = X;
search_history = zeros(N, Max_iter, dim);
fitness_history = zeros(N, Max_iter);
%% Start search
for i = 1:Max_iter
    if mod(i,100) == 0
      display(['At iteration ', num2str(i), ' the fitness is ', num2str(curve(i-1))]);
    end
    avg_fitness_curve(i) = AveF;
    alpha = rand(1) / 5;
    sita = rand(1) * pi;
    for j = 1:size(X, 1)
        St = randi([1, 5]);
        % foraging behavior
        if St == 1
                X_new(j, :) = (X(j, :) - GBestX) .* Levy(dim) + rand(1) * mean(X) * (1 - i / Max_iter) ^ (2 * i / Max_iter);

        % staying behavior
        elseif St == 2 || St == 5
                X_new(j, :) = X(j, :) + GBestX .* Levy(dim) + randn() * (1 - i / Max_iter) * ones(1, dim);

        % communicating behavior
        elseif St == 3
                H = rand(1);
                if H < 0.5
                    X_new(j, :) = X(j, :) + alpha * (1 - i / Max_iter) * (X(j, :) - mean(X));
                else
                    X_new(j, :) = X(j, :) + alpha * (1 - i / Max_iter) * exp(-j / (rand(1) * Max_iter));
                end
        % fear of strangers' behavior
        else
                X_new(j, :) = X(j, :) + rand() * cos((pi *i )/ (2 * Max_iter)) * (GBestX - X(j, :)) - cos(sita) * (i / Max_iter) ^ (2 / Max_iter) * (X(j, :) - GBestX);
        end

        % Boundary control
        Flag4ub=X_new(j,:)>ub;
        Flag4lb=X_new(j,:)<lb;
        X_new(j,:)=(X_new(j,:).*(~(Flag4ub+Flag4lb)))+ub.*Flag4ub+lb.*Flag4lb;
       
        % Finding the best location so far
        fitness_new(j) = fobj(X_new(j, :));
        if fitness_new(j) < GBestF
            GBestF = fitness_new(j);
            GBestX = X_new(j, :);
        end
    end
   
    % Update positions
    X = X_new;
    fitness = fitness_new;
    curve(i) = GBestF;
    Best_pos = GBestX;
    Best_score = curve(end);
    search_history(:, i, :) = X;
    fitness_history(:, i) = fitness;

end


%%  Levy search strategy
function o = Levy(d)
    beta = 1.5;
    sigma = (gamma(1 + beta) *sin(pi * beta / 2) / (gamma((1 + beta) / 2) * beta * 2^((beta - 1) / 2)))^(1 / beta);
    u = randn(1, d) * sigma;
    v = randn(1, d);
    step = u ./ abs(v).^(1 / beta);
    o = step;
end   

end