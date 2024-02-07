# Parrot Optimizer: Algorithm and Applications to Medical Problems

![GitHub](https://img.shields.io/github/license/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub repo size](https://img.shields.io/github/repo-size/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub language count](https://img.shields.io/github/languages/count/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub last commit](https://img.shields.io/github/last-commit/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub issues](https://img.shields.io/github/issues/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub forks](https://img.shields.io/github/forks/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub stars](https://img.shields.io/github/stars/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub watchers](https://img.shields.io/github/watchers/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)
![GitHub contributors](https://img.shields.io/github/contributors/aliasgharheidaricom/Parrot-optimizer-Algorithm-and-applications-to-medical-problems)

## Introduction

Welcome to the Parrot Optimizer repository! The Parrot Optimizer (PO) is an innovative optimization algorithm inspired by the behaviors of trained Pyrrhura Molinae parrots. This repository contains the source code for the PO, along with comprehensive documentation to help you understand and utilize this powerful optimization tool.
<div align="center">
  <img src="image1.png" width="200" />
  <img src="image2.png" width="200" />
  <img src="image3.png" width="200" />
</div>

## Overview

This repository houses the implementation of the PO algorithm, introduced and detailed in the research paper titled "Parrot optimizer: Algorithm and applications to medical problems." The paper, authored by Junbo Lian, Guohua Hui, Ling Ma, Ting Zhu, Xincan Wu, Ali Asghar Heidari, Yi Chen, and Huiling Chen, was published in Computers in Biology and Medicine in 2024.

1. **Parameter Inputs:**
   - `N`: Number of individuals in the population.
   - `Max_iter`: Maximum number of iterations.
   - `lb` and `ub`: Lower and upper bounds for the optimization variables.
   - `dim`: Dimensionality of the problem.
   - `fobj`: Objective function to be minimized.

2. **Initialization:**
   - The optimization process begins with the initialization of the population.

3. **Foraging Behaviors:**
   - The algorithm incorporates different foraging behaviors including searching, staying, communicating, and fear of strangers.

4. **Levy Flight Strategy:**
   - The Levy flight strategy is employed for exploration, enhancing the global search capability.

5. **Boundary Control:**
   - The algorithm ensures that individuals stay within the specified search space boundaries.

6. **Sorting and Updating:**
   - Individuals are sorted based on their fitness values, and the global best solution is updated accordingly.

7. **Levy Search Strategy:**
   - A Levy search strategy is used to balance exploration and exploitation.

8. **Fitness Tracking:**
   - Fitness values and positions are tracked throughout the optimization process.

### Usage Example:


[N, Max_iter, lb, ub, dim, fobj] = set_your_parameters();
[avg_fitness_curve, Best_pos, Best_score, curve, search_history, fitness_history] = PO(N, Max_iter, lb, ub, dim, fobj); 

**Note:**
Please replace set_your_parameters() with appropriate parameter values based on your optimization problem.

Ensure that the objective function (fobj) is defined according to your optimization task.

Feel free to explore and utilize the Parrot Optimizer for your optimization needs. If you have any questions or feedback, please reach out to the authors.

Thank you for your interest in the Parrot Optimizer!

## Key Features

- Efficient optimization inspired by parrot behaviors.
- Qualitative analysis and experiments on 35 functions.
- Benchmarking against popular algorithms.
- Adaptability demonstrated in engineering design, disease diagnosis, and medical image segmentation.


# Applications

Explore the applications of the Parrot Optimizer in medical image segmentation:

- [Multi-Threshold Image Segmentation (MTIS)](applications.md#multi-threshold-image-segmentation-mtis)
  - Learn about our approach combining non-local mean filtering, 2D histograms, Kapur entropy, and the Parrot Optimizer for enhanced segmentation of histopathology microscopy images.

For detailed experiments, evaluation metrics, and results, refer to the [Applications.md](applications.md) file.

![Flowchart of MTIS Method](The%20flowchart%20of%20MTIS%20method.png)



## Contributing

We welcome contributions from the community! If you'd like to contribute to the Parrot Optimizer project, please contact us
If you have any questions, suggestions, or feedback, feel free to reach out to the authors:


- **Junbo Lian**
  - Email: [junbolian@qq.com](mailto:junbolian@qq.com)

- **Ali Asghar Heidari**
  - Email: [as_heidari@ut.ac.ir](mailto:as_heidari@ut.ac.ir), [aliasghar68@gmail.com](mailto:aliasghar68@gmail.com)

- **Huiling Chen**
  - Email: [chenhuiling.jlu@gmail.com](mailto:chenhuiling.jlu@gmail.com)


## Acknowledgments

We extend our gratitude to all contributors and organizations that supported the development of the Parrot Optimizer. 

## License

The Parrot Optimizer is licensed under the [MIT License](LICENSE). Please review the license for details on how you can use and distribute this software.

## Contact Information

If you have any questions, feedback, or collaboration inquiries, feel free to reach out to us

- **Junbo Lian**
  - Email: [junbolian@qq.com](mailto:junbolian@qq.com)

- **Ali Asghar Heidari**
  - Email: [as_heidari@ut.ac.ir](mailto:as_heidari@ut.ac.ir), [aliasghar68@gmail.com](mailto:aliasghar68@gmail.com)

- **Huiling Chen**
  - Email: [chenhuiling.jlu@gmail.com](mailto:chenhuiling.jlu@gmail.com)


## Citation

If you use the Parrot Optimizer in your academic research, please cite our paper. 


## Supplementary Files and Code

For additional resources, supplementary files, and open-source code, visit [aliasgharheidari.com/PO.html](https://aliasgharheidari.com/PO.html).

## MATLAB File Exchange

Find the Parrot Optimizer on MathWorks File Exchange: [Parrot Optimizer - Algorithm and Application to Medical Problem](https://ch.mathworks.com/matlabcentral/fileexchange/158681-parrot-optimizer-algorithm-application-to-medical-problem)

## Flowchart

![Flowchart of Parrot Optimizer (PO)](Flowchart%20of%20Parrot%20Optimizer%20(PO).png)

Feel free to explore the code, contribute to the project, and leverage the Parrot Optimizer for your optimization needs. Thank you for your interest in the Parrot Optimizer!
