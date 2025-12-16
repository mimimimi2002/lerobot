from huggingface_hub import snapshot_download

local_dir = snapshot_download(
    repo_id="mimimimi2002/libero_spatial",  # データセットのリポジトリ
    repo_type="dataset",
    cache_dir="/home/miki/.cache/huggingface/lerobot/mimimimi2002/libero_spatial",
    revision="main"
)

print("Dataset downloaded to:", local_dir)
