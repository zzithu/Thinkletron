# Thinkletron
This project explores creative AI use for simulating unique dungeon crawling instances

## Usage
Run main after installing dependencies

## Packages
Pytorch / Transformers - model
Tkinter - Gui
PILLOW - Images within Tkinter

## Model
We are running [Qwen 2.5 - 1.5b]{https://huggingface.co/Qwen}, which is lighter weight and provides fairly unique responses
    Should ram be an issue, may swap to the .5B param model

This is the base with no additional changes.

Cite: 
    @misc{qwen2.5,
        title = {Qwen2.5: A Party of Foundation Models},
        url = {https://qwenlm.github.io/blog/qwen2.5/},
        author = {Qwen Team},
        month = {September},
        year = {2024}
    }

    @article{qwen2,
        title={Qwen2 Technical Report}, 
        author={An Yang and Baosong Yang and Binyuan Hui and Bo Zheng and Bowen Yu and Chang Zhou and Chengpeng Li and Chengyuan Li and Dayiheng Liu and Fei Huang and Guanting Dong and Haoran Wei and Huan Lin and Jialong Tang and Jialin Wang and Jian Yang and Jianhong Tu and Jianwei Zhang and Jianxin Ma and Jin Xu and Jingren Zhou and Jinze Bai and Jinzheng He and Junyang Lin and Kai Dang and Keming Lu and Keqin Chen and Kexin Yang and Mei Li and Mingfeng Xue and Na Ni and Pei Zhang and Peng Wang and Ru Peng and Rui Men and Ruize Gao and Runji Lin and Shijie Wang and Shuai Bai and Sinan Tan and Tianhang Zhu and Tianhao Li and Tianyu Liu and Wenbin Ge and Xiaodong Deng and Xiaohuan Zhou and Xingzhang Ren and Xinyu Zhang and Xipin Wei and Xuancheng Ren and Yang Fan and Yang Yao and Yichang Zhang and Yu Wan and Yunfei Chu and Yuqiong Liu and Zeyu Cui and Zhenru Zhang and Zhihao Fan},
        journal={arXiv preprint arXiv:2407.10671},
        year={2024}
    }

For image generation we are using Stable Diffusion
    [Stable Diffusion]{https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0}
    This is the base with no additional changes at the moment (Code is directly used)

## Dependencies
    Uses pytorch (model framework), transformers (text generation), stablediffusion (photo gen), tkinter (gui), and pillow (photo)


    pip install torch 
    Note: this one may require additional setup, visit [pytorch]{https://pytorch.org/} for more details

    pip install transformers
    pip install diffusers --upgrade
    pip install pillow