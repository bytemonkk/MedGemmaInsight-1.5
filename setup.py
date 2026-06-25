```python
from setuptools import setup, find_packages

setup(
    name="MedGemmaInsight-1.5",
    version="1.0.0",
    author="Manoj",
    description="Efficient Fine-Tuning of MedGemma-1.5-4B-IT for Medical Question Answering using Unsloth",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "torch",
        "torchvision",
        "torchaudio",
        "unsloth",
        "transformers>=4.45.0",
        "trl",
        "peft",
        "accelerate",
        "bitsandbytes",
        "datasets",
        "evaluate",
        "numpy",
        "pandas",
        "scikit-learn",
        "tqdm",
        "sentencepiece",
        "protobuf",
        "huggingface_hub",
        "safetensors",
    ],
)
```
