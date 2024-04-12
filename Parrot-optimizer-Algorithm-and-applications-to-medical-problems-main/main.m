%___________________________________________________________________________________________________________________________________________________%
% Parrot Optimizer (PO) source codes (version 2.0)
% Main function
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


close all
clear
clc
N = 30; % Number of search agents
Function_name='F1'; % Name of the test function that can be from F1 to F23 
Max_iteration = 1000; % Maximum numbef of iterations

% Load details of the selected benchmark function
[lb,ub,dim,fobj] = Get_Functions_details(Function_name);
[avg_fitness_curve1, Best_pos1, Best_score1, Convergence1, search_history1, fitness_history1] = PO(N,Max_iteration,lb,ub,dim,fobj);
[avg_fitness_curve2, Best_pos2, Best_score2, Convergence2, search_history2, fitness_history2] = PO_F(N,Max_iteration,lb,ub,dim,fobj);
[avg_fitness_curve3, Best_pos3, Best_score3, Convergence3, search_history3, fitness_history3] = PO_S(N,Max_iteration,lb,ub,dim,fobj);
[avg_fitness_curve4, Best_pos4, Best_score4, Convergence4, search_history4, fitness_history4] = PO_C(N,Max_iteration,lb,ub,dim,fobj);
[avg_fitness_curve5, Best_pos5, Best_score5, Convergence5, search_history5, fitness_history5] = PO_O(N,Max_iteration,lb,ub,dim,fobj);


figure('Position',[454 445 1600 300])
%Draw search space
subplot(1,4,1);
func_plot(Function_name);
title('Parameter space')
xlabel('x_1');
ylabel('x_2');
zlabel([Function_name,'( x_1 , x_2 )'])


%
subplot(1,4,2);
hold on
for k1 = 1:size(search_history1, 1)
    for k2 = 1:size(search_history1, 2)
        plot(search_history1(k1, k2, 1), search_history1(k1, k2, 2), '.', 'markersize', 1, 'MarkerEdgeColor', 'k', 'markerfacecolor', 'k');
    end
end
title('PO (x1 and x2 only)')
xlabel('x1')
ylabel('x2')
box on
axis tight




%
subplot(1,4,3);
hold on
plot(mean(fitness_history1),'Linewidth', 1.5);
title('Average fitness')
xlabel('Iteration')
box on
axis tight



%Draw objective space
subplot(1,4,4);
semilogy(Convergence1,'Color','k','Linewidth', 1.5)
hold on
semilogy(Convergence2,'Color','r','Linewidth', 1.5)
semilogy(Convergence3,'Color','b','Linewidth', 1.5)
semilogy(Convergence4,'Color','c','Linewidth', 1.5)
semilogy(Convergence5,'Color','y','Linewidth', 1.5)
title('Objective space')
xlabel('Iteration');
ylabel('Best score obtained so far');
axis tight
grid on
box on
legend('PO','PO-F','PO-S','PO-C','PO-O')



