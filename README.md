

🌎 English | [Vietnamese](README_vn.md)

# 🔧 Dependencies

- Python >= 3.7 (Recommend to use Anaconda or Miniconda, Default: Miniconda)
- PyTorch >= 1.7
- Option: NVIDIA GPU + CUDA

# 🛠️ Installation

- Clone  this project:

```[bash]
git clone https://github.com/KaiKenju/FaceRestoration_GFPGAN.git
```

- Initial enviromment with Miniconda (Default: python 3.10):

```[bash]
conda create -n <env_name> python=3.10
```
- Activate conda
```[bash]
conda activate <env_name> 
cd FaceRestoration_GFPGAN
```
- Run the commands:
```[bash]
pip install -r GFPGAN/requirements.txt
```
- After install requirements, you need to run the [fix_torchvision.py](fix_torchvision.py) to avoid the problem of basicsr module after install.
```[bash]
python fix_torchvision.py
``` 
# ⚡ Quick Inference
```[bash]
python main.py -i old_images_ori --output_dir my_result --upscale 2 --version 1.4
``` 

```console
Usage: python main.py -i old_images_ori --output_dir my_result --upscale 2 --version 1.4 

  -h                   show this help
  -i input             Input image or folder. Default: old_images_ori
  --output_dir output            Output folder. Default: my_results
  -v version           GFPGAN model version. Option: 1 | 1.2 | 1.3. Default: 1.4
  -s upscale           The final upsampling scale of the image. Default: 2
  -bg_upsampler        background upsampler. Default: realesrgan
  -bg_tile             Tile size for background sampler, 0 for no tile during testing. Default: 400
  -suffix              Suffix of the restored faces
  -only_center_face    Only restore the center face
  -aligned             Input are aligned faces
  -ext                 Image extension. Options: auto | jpg | png, auto means using the same extension as inputs. Default: auto
```