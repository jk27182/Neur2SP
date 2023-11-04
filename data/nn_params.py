""" 
    This file constrains best paramaters found by random search over 100 configurations
    for each instance and NN-{E,P} model.  These can be imported directly to train each model 
    and reproduce the results.  
"""

# Optimal parameters for NN-P
nn_p_params =  {
    'cflp_10_10': {
        'hidden_dims': [64],
        'lr': 0.00768,
        'dropout': 0.07346,
        'optimizer_type': 'RMSprop',
        'batch_size': 32,
        'loss_fn': 'MSELoss',
        'wt_lasso': 0.0,
        'wt_ridge': 0.0,
        'log_freq': 10,
        'n_epochs': 1000,
        'use_wandb': 0},
    # 'cflp_25_25': {
    #     'hidden_dims': [64],
    #     'lr': 0.01522,
    #     'dropout': 0.12911,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 32,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.00411,
    #     'wt_ridge': 0.01378,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'cflp_50_50': {
    #     'hidden_dims': [64],
    #     'lr': 0.04842,
    #     'dropout': 0.0957,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.0622,
    #     'wt_ridge': 0.00984,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'sslp_5_25': {
    #     'hidden_dims': [64],
    #     'lr': 0.04383,
    #     'dropout': 0.04066,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 16,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.00976,
    #     'wt_ridge': 0.0,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'sslp_10_50': {
    #     'hidden_dims': [64],
    #     'lr': 0.04383,
    #     'dropout': 0.04066,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 16,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.00976,
    #     'wt_ridge': 0.0,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'sslp_15_45': {
    #     'hidden_dims': [64],
    #     'lr': 0.04383,
    #     'dropout': 0.04066,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 16,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.00976,
    #     'wt_ridge': 0.0,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'ip_b_E': {
    #     'hidden_dims': [64],
    #     'lr': 0.00433,
    #     'dropout': 0.04056,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.005,
    #     'wt_ridge': 0.00841,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'ip_b_H': {
    #     'hidden_dims': [64],
    #     'lr': 0.00768,
    #     'dropout': 0.07346,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 32,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.0,
    #     'wt_ridge': 0.0,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'ip_i_E': {
    #     'hidden_dims': [64],
    #     'lr': 0.00768,
    #     'dropout': 0.07346,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 32,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.0,
    #     'wt_ridge': 0.0,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'ip_i_H': {
    #     'hidden_dims': [64],
    #     'lr': 0.00768,
    #     'dropout': 0.07346,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 32,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.0,
    #     'wt_ridge': 0.0,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0},
    # 'pp': {
    #     'hidden_dims': [64],
    #     'lr': 0.00086,
    #     'dropout': 0.13771,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 64,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.02835,
    #     'wt_ridge': 0.08205,
    #     'log_freq': 10,
    #     'n_epochs': 1000,
    #     'use_wandb': 0}
    }

# Optimal parameters for NN-E
nn_e_params = {
    'cflp_10_10': {
        'embed_hidden_dim': 512,
        'embed_dim1': 64,
        'embed_dim2': 16,
        'relu_hidden_dim': 512,
        'agg_type': 'mean',
        'lr': 0.00436,
        'dropout': 0.04226,
        'optimizer_type': 'Adam',
        'batch_size': 128,
        'loss_fn': 'MSELoss',
        'wt_lasso': 0.09067,
        'wt_ridge': 0.02603,
        'log_freq': 10,
        # 'n_epochs': 2000,
        'n_epochs': 10,
        'use_wandb': 0},
    # 'cflp_25_25': {
    #     'embed_hidden_dim': 64,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 512,
    #     'agg_type': 'mean',
    #     'lr': 0.08384,
    #     'dropout': 0.00238,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.03226,
    #     'wt_ridge': 0.07454,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'cflp_50_50': {
    #     'embed_hidden_dim': 64,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 512,
    #     'agg_type': 'mean',
    #     'lr': 0.08384,
    #     'dropout': 0.00238,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.03226,
    #     'wt_ridge': 0.07454,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'sslp_5_25': {
    #     'embed_hidden_dim': 64,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 512,
    #     'agg_type': 'mean',
    #     'lr': 0.08384,
    #     'dropout': 0.00238,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.03226,
    #     'wt_ridge': 0.07454,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'sslp_10_50': {
    #     'embed_hidden_dim': 64,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 512,
    #     'agg_type': 'mean',
    #     'lr': 0.08384,
    #     'dropout': 0.00238,
    #     'optimizer_type': 'RMSprop',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.03226,
    #     'wt_ridge': 0.07454,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'sslp_15_45': {
    #     'embed_hidden_dim': 256,
    #     'embed_dim1': 64,
    #     'embed_dim2': 64,
    #     'relu_hidden_dim': 128,
    #     'agg_type': 'mean',
    #     'lr': 0.09621,
    #     'dropout': 0.01053,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.02965,
    #     'wt_ridge': 0.0004,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'ip_b_E': {
    #     'embed_hidden_dim': 512,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 128,
    #     'agg_type': 'mean',
    #     'lr': 0.00433,
    #     'dropout': 0.04056,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.005,
    #     'wt_ridge': 0.00841,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'ip_b_H': {
    #     'embed_hidden_dim': 512,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 128,
    #     'agg_type': 'mean',
    #     'lr': 0.00433,
    #     'dropout': 0.04056,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.005,
    #     'wt_ridge': 0.00841,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'ip_i_E': {
    #     'embed_hidden_dim': 512,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 128,
    #     'agg_type': 'mean',
    #     'lr': 0.00433,
    #     'dropout': 0.04056,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.005,
    #     'wt_ridge': 0.00841,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'ip_i_H': {
    #     'embed_hidden_dim': 512,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 128,
    #     'agg_type': 'mean',
    #     'lr': 0.00433,
    #     'dropout': 0.04056,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.005,
    #     'wt_ridge': 0.00841,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0},
    # 'pp': {
    #     'embed_hidden_dim': 512,
    #     'embed_dim1': 128,
    #     'embed_dim2': 8,
    #     'relu_hidden_dim': 128,
    #     'agg_type': 'mean',
    #     'lr': 0.00433,
    #     'dropout': 0.04056,
    #     'optimizer_type': 'Adam',
    #     'batch_size': 128,
    #     'loss_fn': 'MSELoss',
    #     'wt_lasso': 0.005,
    #     'wt_ridge': 0.00841,
    #     'log_freq': 10,
    #     'n_epochs': 2000,
    #     'use_wandb': 0}
    }

