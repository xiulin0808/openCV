import kagglehub

# Download latest version
path = kagglehub.dataset_download("sanidhyak/human-face-emotions")

print("Path to dataset files:", path)