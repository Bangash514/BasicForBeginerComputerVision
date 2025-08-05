# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 11:20:42 2025

@author: Administrator
"""

import os
import urllib.request
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models

def download_labels(label_path):
    label_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
    if not os.path.exists(label_path):
        print("Downloading imagenet class labels...")
        urllib.request.urlretrieve(label_url, label_path)
        print("Download complete.")

def main():
    # Paths
    image_path = image_path = "D:\Let's learning Coding\Practice of Basic Image processing\Kareena_Kapoor_at_TOIFA16.jpg"  # adjust relative path if needed
    label_path = 'imagenet_classes.txt'  # put this file in same folder or let script download

    # Download labels if missing
    download_labels(label_path)

    # Load class labels
    with open(label_path) as f:
        labels = [line.strip() for line in f.readlines()]

    # Load pretrained model
    model = models.resnet18(pretrained=True)
    model.eval()

    # Image preprocessing
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])

    # Load image
    img = Image.open(image_path)
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)  # batch dimension

    # Inference
    with torch.no_grad():
        out = model(batch_t)
        probabilities = torch.nn.functional.softmax(out[0], dim=0)

    # Show top 5 results
    _, indices = torch.sort(probabilities, descending=True)
    print("Top 5 Predictions:")
    for idx in indices[:5]:
        print(f"{labels[idx]}: {probabilities[idx].item():.4f}")

if __name__ == "__main__":
    main()
