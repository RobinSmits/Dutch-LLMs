# Dutch LLM's
Various training, inference and validation code and results related to Open LLM's that were pretrained (full or partially) on the Dutch language.

At this moment (October 12th, 2023) this repository contains the Google Colaboratory notebooks for finetuning and inference of the following Open LLM's:
* Open LLaMA 7B and 13B
* PolyLM 1.7B and 13B

## Training and Evaluation

### OpenLLaMA

I've used Google Colaboratory to finetune the 2 largest LLM base models from openlm_research on the Alpaca Cleaned instruction dataset that was translated to Dutch.

In some early experiments I started with the open_llama_3b model. It turned out however that the results from the 7B and 13B models were a lot better.

Below you can find the Google Colab Training and Inference notebooks. The link to the basemodel and the link to the finetuned model at Huggingface.co.

Each Inference notebooks contains 50 samples with a generated Answer for an Instruction/Input prompt from the validation dataset.

Basemodel [openlm-research/open_llama_7b](https://huggingface.co/openlm-research/open_llama_7b):
* Training Notebook [Open_Llama_7B_Alpaca_Clean_Dutch_Qlora](Open_Llama_7B_Alpaca_Clean_Dutch_Qlora.ipynb)
* Inference Notebook [Open_Llama_7B_Alpaca_Clean_Dutch_Inference](Open_Llama_7B_Alpaca_Clean_Dutch_Inference.ipynb)
* Huggingface Model [open_llama_7b_alpaca_clean_dutch](https://www.huggingface.co/robinsmits/open_llama_7b_alpaca_clean_dutch_qlora)

Basemodel [openlm-research/open_llama_13b](https://huggingface.co/openlm-research/open_llama_13b):
* Training Notebook [Open_Llama_13B_Alpaca_Clean_Dutch_Qlora](Open_Llama_13B_Alpaca_Clean_Dutch_Qlora.ipynb)
* Inference Notebook [Open_Llama_13B_Alpaca_Clean_Dutch_Inference](Open_Llama_13B_Alpaca_Clean_Dutch_Inference.ipynb)
* Huggingface Model [open_llama_13b_alpaca_clean_dutch](https://www.huggingface.co/robinsmits/open_llama_13b_alpaca_clean_dutch_qlora)

In the near future I would like to do a more indepth analysis of the generated answers for the various prompts.

For now a quick summary of my first impression on the results that I have gathered with the finetuned open_llmama models sofar:
* Both the 7B and 13B models suffer occassionally from repetitions and hallucinations.
* Occassionally no answer is generated. Or there is plain garbage output...specifically the 13B model suffers from this .. (the ///// sequences)
* A small but significant percentage of generated answers make some sense in the Dutch language.
* Some average/good examples for the 7B model are: 0, 2, 3, 5, 7, 8, 10, 12, 13, 19, 20, 23
* Some average/good examples for the 13B model are: 0, 2, 5, 8, 9, 13, 21, 22

The above mentioned average and good examples have a reasonably good quality. This list is by no means complete. There can be some typos, repetitions etc ... in the context of the small portion of the original training set that is applicable to the Dutch language it is my personal opinion that these are acceptible. With more and diverse Dutch training dataset I would expect a higher quality.

!! TODO: Implement one of the mainstream multi-lingual evaluation scenario's

It is very clear that these models should not be used in any reallife or production scenario related to the Dutch language. These finetuned models are primarily intended for research purposes. The percentage of Dutch language text in the training set is to small to achieve a performance comparable to the main (English) language in the training set.

That said, with all the issues mentioned above, it is still interresting to observe that a significant percentage of the generated answers make some sense in the Dutch language.

### PolyLM

Recently some researchers from Alibaba released the Open LLM PolyLM models with 1.7B and 13B parameters. There motivation was to create an Open LLM model that supports multiple languages besides the regularly used English language. PolyLM was trained on 18 languages and Dutch was one of those languages.

According to the research paper PolyLM surpasses models like LLaMA and Bloom on multilingual tasks while scoring comparable on English.

More information about the model can be found in the [research paper](https://arxiv.org/abs/2307.06018).

I've used Google Colaboratory to finetune the 2 Open LLM PolyLM base models on the Alpaca Cleaned instruction dataset that was translated to Dutch.

Below you can find the Google Colab Training and Inference notebooks, the link to the basemodel and the link to the finetuned model at Huggingface.co.

Each Inference notebooks contains 50 samples with a generated Answer for an Instruction/Input prompt from the validation dataset.

Basemodel [DAMO-NLP-MT/polylm-1.7b](https://huggingface.co/DAMO-NLP-MT/polylm-1.7b):
* Training Notebook [PolyLM_1.7B_Alpaca_Clean_Dutch_Qlora](PolyLM_1_7B_Alpaca_Clean_Dutch_Qlora.ipynb)
* Inference Notebook [PolyLM_1.7B_Alpaca_Clean_Dutch_Inference](PolyLM_1_7B_Alpaca_Clean_Dutch_Inference.ipynb)
* Huggingface Model [polylm_1.7b_ft_alpaca_clean_dutch](https://huggingface.co/robinsmits/polylm_1.7b_ft_alpaca_clean_dutch)

Basemodel [DAMO-NLP-MT/polylm-13b-fine-grained-shards](https://huggingface.co/DAMO-NLP-MT/polylm-13b-fine-grained-shards):
* Training Notebook [PolyLM_13B_Alpaca_Clean_Dutch_Qlora](PolyLM_13B_Alpaca_Clean_Dutch_Qlora.ipynb)
* Inference Notebook [PolyLM_13B_Alpaca_Clean_Dutch_Inference](PolyLM_13B_Alpaca_Clean_Dutch_Inference.ipynb)
* Huggingface Model [polylm_13b_ft_alpaca_clean_dutch](https://huggingface.co/robinsmits/polylm_13b_ft_alpaca_clean_dutch)

For now a quick summary of my first impression on the results that I have gathered with the finetuned PolyLM models so far:
* Both the 1.7B and 13B models suffer occassionally from repetitions and hallucinations.
* A small but significant percentage of generated answers make some sense in the Dutch language.
* The 13B model is giving better quality answers than the 1.7B model.
* It is also worth noting that the quality of both the PolyLM models is far better than the Open LLama models. Based on the larger size of the Dutch language in the pretraining dataset for the PolyLM models this is as expected.

## Datasets

Below a description of the various dataset(s) that have been used for training and evaluation.

### Alpaca Dutch Cleaned

Alpaca is a dataset containing roughly 51K rows of data that can be used to finetune any Large Language Model. The original dataset is in the English language only.

Recently I came across a version of the dataset that was completely translated into the Dutch language. Use the following link for the dataset: [Alpaca Dutch Cleaned](https://www.huggingface.co/datasets/BramVanroy/alpaca-cleaned-dutch)

During training of the first Colab Notebook the dataset was split into a training and validation part. The size of the validation set is 2048 rows.
Since I would like to be able to compare the various training runs and evaluation results the training and validation datasets are stored within a subfolder (alpaca_clean_dutch) in this Github repo.

## Citations

```
@misc{https://doi.org/10.57967/hf/0530,
  doi = {10.57967/HF/0530},
  url = {https://huggingface.co/datasets/BramVanroy/alpaca-cleaned-dutch},
  author = {{Bram Vanroy}},
  title = {{A}lpaca {C}leaned {D}utch},
  publisher = {Hugging Face},
  year = {2023}
}
```

```
@misc{wei2023polylm,
      title={PolyLM: An Open Source Polyglot Large Language Model}, 
      author={Xiangpeng Wei and Haoran Wei and Huan Lin and Tianhao Li and Pei Zhang and Xingzhang Ren and Mei Li and Yu Wan and Zhiwei Cao and Binbin Xie and Tianxiang Hu and Shangjie Li and Binyuan Hui and Bowen Yu and Dayiheng Liu and Baosong Yang and Fei Huang and Jun Xie},
      year={2023},
      eprint={2307.06018},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```
@software{openlm2023openllama,
  author = {Geng, Xinyang and Liu, Hao},
  title = {OpenLLaMA: An Open Reproduction of LLaMA},
  month = May,
  year = 2023,
  url = {https://github.com/openlm-research/open_llama}
}
```