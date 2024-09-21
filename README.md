

🌎 English | [Vietnamese](README_vn.md)

<img src="my_result/cmp/16864688-290777354672479-5494028598530650668-n-1487686959579-1522248859846848960801_00.png " style="width: 80%;">

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
Dowload pre-trained models : [GFPGANv1.4.pth](https://drive.google.com/file/d/1PYZa2PP3qbs9_7uB7JSUPk2hF-S1ePWm/view?usp=drive_link) and put them following path `model/GFPGANv1.4.pth`

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

**Tips**

The first time you run the model and use CPU, it can be more time to load data, so to reduce time you can put weight file following path:
1. Download pre-trained models and other data. Put them in the `GFPGAN/gfpgan/weights` folder.
    1. [Detection_Resnet50](https://drive.google.com/file/d/1xrJsMbCZMfn7ovumCBmhlp9VVs2rIJ1z/view?usp=drive_link)
    1. [Parsing_Parsenet](https://drive.google.com/file/d/1WprE4914U3MYiU6p6oVjVRm_tCs4lsY_/view?usp=drive_link)
1. Also in the `GFPGAN/weights` folder.
    1. [GFPGANv1.4.pth](https://drive.google.com/file/d/1PYZa2PP3qbs9_7uB7JSUPk2hF-S1ePWm/view?usp=drive_link)