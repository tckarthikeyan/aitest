#
#!/bin/bash
# 
python3 -m venv aienv
source aienv/bin/activate
pip3 install numpy
pip3 install pandas
pip3 install huggingface_hub
pip3 install tensorflow
pip3 install matplotlib
pip3 install transformers
pip install transformers[torch]
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip3 install datasets
pip3 install --upgrade openai
pip3 install jupyter
