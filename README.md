# Finetuned LLAVA FOR IMAGE RECEIPT ANALYSIS

> **Important Note**: Ensure you have at least 8GB of GPU memory to load the quantized version of the model. The fine-tuned version of the model is available on my Hugging Face Hub repository at [Finetuned-Llava](https://huggingface.co/abhisheksinghrathore/Finetuned-Llava).

## Overview

This project implements a fine-tuning approach for the Llava model using advanced techniques such as QLoRA, LoRA, and Flash Attention. Before fine-tuning, the Llava 7B model was unable to provide a JSON response detailing the contents of images. However, after fine-tuning with the Naver Clova IX CORD-v2 dataset, the model successfully generates accurate JSON responses describing what is present in images.

## Jupyter Notebook Links

- **Before Fine-Tuning**: [View Notebook](https://github.com/abhishekiiitbh2903/Llava-Finetuned/blob/main/Before_FineTuning.ipynb)  
- **After Fine-Tuning**: [View Notebook](https://github.com/abhishekiiitbh2903/Llava-Finetuned/blob/main/test_finetuned_1.6_7b.ipynb)

> **Project by Abhishek Singh (Guider: Farzad and Andrej)**, a final-year B.Tech CSE undergraduate at IIIT BH. I am open for collaboration and enthusiastic about working on AI and Machine Learning projects.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Dataset](#dataset)
- [Training Steps](#training-steps)
  - [Using PEFT for Fine-tuning](#using-peft-for-fine-tuning)
  - [QLoRA Technique](#qlora-technique)
  - [LoRA Technique](#lora-technique)
  - [Flash Attention](#flash-attention)
- [User Interface](#user-interface)
- [Installation](#installation)

## Introduction

In this project, we leverage the capabilities of the Llava model to perform efficient training and fine-tuning. Initially, the model struggled to interpret images and generate structured JSON responses. After fine-tuning, the model can now accurately analyze images and produce detailed JSON outputs, enhancing its utility in real-world applications.

## Requirements

- Python 3.x
- PyTorch
- Transformers
- PEFT
- Additional dependencies specified in `requirements.txt`

## Dataset

The Naver Clova IX CORD-v2 dataset is utilized for training. This dataset provides diverse content suitable for enhancing the model’s understanding and performance in real-world scenarios.

## Training Steps

### Using PEFT for Fine-tuning

PEFT (Parameter-Efficient Fine-Tuning) is a technique designed to reduce the number of trainable parameters during fine-tuning. By focusing on a subset of parameters, we achieve faster training times and lower resource consumption. Here’s how to implement it:

1. **Select Target Parameters**: Choose specific layers or modules within the model that will be fine-tuned.
2. **Apply Gradient Checkpointing**: Use gradient checkpointing to save memory during backpropagation.
3. **Adjust Optimizer Settings**: Configure the optimizer to update only the selected parameters.

### QLoRA Technique

QLoRA (Quantized Low-Rank Adaptation) is an advanced fine-tuning technique that combines quantization with low-rank adaptation. It works as follows:

1. **Quantization**: Reduces the model size by quantizing weights, which decreases memory usage without significantly impacting performance.
2. **Low-Rank Adaptation**: Focuses on fine-tuning a low-rank approximation of the model weights, allowing for efficient updates.

By integrating QLoRA, we can train larger models effectively on limited hardware.

### LoRA Technique

LoRA (Low-Rank Adaptation) is another efficient fine-tuning method that allows us to adapt pre-trained models without full fine-tuning:

1. **Inject LoRA Layers**: Add low-rank matrices into the transformer architecture.
2. **Train LoRA Weights**: During training, only the LoRA weights are updated, which significantly reduces the computational burden.
3. **Keep Original Weights Frozen**: The original weights of the model remain unchanged, ensuring that the pre-trained knowledge is preserved.

### Flash Attention

Flash Attention is a memory-efficient attention mechanism designed to accelerate the training of transformer models:

1. **Memory Efficiency**: Flash Attention reduces memory usage by computing attention scores more efficiently.
2. **Speed Optimization**: It utilizes faster algorithms to calculate attention weights, which leads to quicker training iterations.

## User Interface

A user interface has been created for this project where the frontend is served using **Streamlit** and the backend is managed by **Flask**. This architecture was chosen to prevent the model from reloading each time an image is analyzed, thereby improving efficiency.

The UI allows users to upload an image and receive the model’s analysis in JSON format. The Streamlit frontend displays the image along with the JSON output, while Flask handles the image processing and model inference in the backend.

## Installation

To set up the environment, run:

```bash
pip install -r requirements.txt
