# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": "output",
    "train_data_path": "data/train_dataset.csv",
    "valid_data_path": "data/test_dataset.csv",
    "vocab_path":"chars.txt",
    "model_type":"lstm",
    "max_length": 30,
    "hidden_size": 256,
    "kernel_size": 3,
    "num_layers": 2,
    "epoch": 15,
    "batch_size": 128,
    "pooling_style":"max",
    "optimizer": "adam",
    "learning_rate": 1e-3,
    "pretrain_model_path":r"E:\AI\第六周 语言模型\bert-base-chinese",
    "seed": 987
}

