import torch

# 1. Check if CUDA is available
is_cuda = torch.cuda.is_available()
print(f"CUDA Available: {is_cuda}")

if is_cuda:
    # 2. Get the number of available GPUs
    print(f"GPU Count: {torch.cuda.device_count()}")
    
    # 3. Get the name of the current GPU
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    
    # 4. Check the CUDA version PyTorch was built with
    print(f"CUDA Version: {torch.version.cuda}")
