from huggingface_hub import login, snapshot_download
import os

# HF Login
login("hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXX") # Fill in your own token

# Set Model Name
model_name = "robinsmits/Qwen1.5-7B-Dutch-Chat"

# Download HF Model
snapshot_download(repo_id = model_name, 
                  local_dir = "Qwen1.5-7B-Dutch-Chat",
                  local_dir_use_symlinks = False, 
                  revision = "main")

# Convert
os.system("python convert-hf-to-gguf.py Qwen1.5-7B-Dutch-Chat --outfile Qwen1.5-7B-Dutch-Chat_fp16.gguf")

# Quantize
os.system("./quantize Qwen1.5-7B-Dutch-Chat_fp16.gguf Qwen1.5-7B-Dutch-Chat-Q5_K_M.gguf Q5_K_M")

# Simple Test
os.system("./main -m Qwen1.5-7B-Dutch-Chat-Q5_K_M.gguf -n 512 --temp 0.1 --top-k 50 --color -f dutch-chat.txt")
