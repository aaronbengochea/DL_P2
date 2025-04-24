### Experiments for DL Project 2  
**Exploring LoRA on AG News Category Classification**

This repository—[agnews-classifier-experiments](https://github.com/aaronbengochea/agnews-classifier-experiments)—contains all the experiments we performed for Project 2, where we systematically evaluate Low-Rank Adaptation (LoRA) configurations on the AG News category classification task. Our goal is to balance classification accuracy, computational efficiency, and generalization with fewer than 1M trainable parameters.

The best-performing setup is located in the `top_performing_experiment/` directory. Inside, you’ll find:

- A Jupyter notebook demonstrating how to recreate the top model  
- Configuration files and saved checkpoints for reference  

Feel free to explore each experiment folder for detailed results, hyperparameter sweeps, and analysis notebooks.

##### Visualization of Training Metrics

- **Loss Charts**  
  All training and validation loss curves for each experiment are compiled in `experiments_loss_charts.pdf`. Open this file to review how the training loss and test loss evolve over each training step.

- **Accuracy Charts**  
  Similarly, you can examine per-step training and validation accuracy in `experiments_acc_charts.pdf`. Each page shows the training accuracy alongside the test accuracy for a given experiment.

Both PDFs provide a quick visual summary of model convergence, overfitting behavior, and learning-rate schedules across our low-rank and high-rank LoRA configurations. ```
