# Applications of the Parrot Optimizer in Medical Image Segmentation

In this section, we discuss the application of the Parrot Optimizer in the context of medical image segmentation, as presented in our research paper. The Parrot Optimizer is employed in a Multi-Threshold Image Segmentation (MTIS) model, enhancing the segmentation of histopathology microscopy images of breast tissues stained with H&E.

## Multi-Threshold Image Segmentation (MTIS)

MTIS is a powerful method for partitioning an image into distinct regions using one or more thresholds. Our approach combines non-local mean filtering, 2D histograms, Kapur entropy, and the Parrot Optimizer algorithm. This combination addresses challenges posed by images with multiple objects or discontinuous color and brightness variations.

The MTIS process involves the following steps:

1. **Preprocessing:**
   - Transform the input image into grayscale.
   - Apply non-local mean filtering to reduce noise.

2. **Threshold Selection:**
   - Construct a 2D histogram.
   - Use Kapur's entropy to calculate information content for different threshold combinations.
   - Utilize the Parrot Optimizer to maximize entropy, optimizing information preservation.

3. **Segmentation:**
   - Apply the optimal threshold set to segment the image.

## Experimental Setup

To evaluate the segmentation performance, we conducted two sets of experiments with low and high threshold levels. The experiments involved six cancer pathology images sourced from the invasive ductal carcinoma (IDC) dataset. These images are histopathology microscopy images of breast tissues stained with H&E, annotated based on their grade and magnification level.

## Evaluation Metrics

We compared the segmentation results of the Parrot Optimizer with five other algorithms. The compared algorithms and their parameter settings are listed in Table 18. The evaluation relied on the following key metrics:

- **Peak Signal-to-Noise Ratio (PSNR)**
- **Structural Similarity Index (SSIM)**
- **Feature Similarity Index (FSIM)**

The mean and variance of these metrics were calculated for thorough performance evaluation.

## Experimental Conditions

All compared algorithms were subjected to identical experimental conditions:
- 100 iterations
- Image size: 512×512
- Solution space size: 30
- Each algorithm independently run 10 times.

## Results

The segmentation results of the Parrot Optimizer were compared with other algorithms using the metrics mentioned above. For a visual overview of the MTIS operation process, refer to the flowchart presented in Fig. 16.

Feel free to explore the detailed results and findings in the paper for a comprehensive understanding of the Parrot Optimizer's performance in medical image segmentation.
