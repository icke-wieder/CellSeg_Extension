from pathlib import Path

train_images_dir = Path('./YOUR_data/train_images')
train_masks_dir  = Path('./YOUR_data/train_masks')
test_images_dir  = Path('./YOUR_data/test_images')
test_masks_dir   = Path('./YOUR_data/test_masks')

Path(train_images_dir).mkdir(parents=True, exist_ok=True)
Path(train_masks_dir).mkdir(parents=True, exist_ok=True)
Path(test_images_dir).mkdir(parents=True, exist_ok=True)
Path(test_masks_dir).mkdir(parents=True, exist_ok=True)