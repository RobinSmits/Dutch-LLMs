# Dutch LLM's
Various training, inference and validation code and results related to Open LLM's that were pretrained (full or partially) on the Dutch language.

## Training

The following Google Colab Notebook was used to finetune an [openlm-research/open_llama_7b](https://huggingface.co/openlm-research/open_llama_7b) LLM model on the translated Alpaca instruct dataset.

Notebook: [Open_Llama_7B_Alpaca_Clean_Dutch_Qlora](Open_Llama_7B_Alpaca_Clean_Dutch_Qlora.ipynb)


<< TODO >>

## Evaluation

<< TODO >>


## Datasets

Below a description of the various dataset(s) that have been used for training and evaluation.

### Alpaca Dutch Cleaned

Alpaca is a dataset containing roughly 51K rows of data that can be used to finetune any Large Language Model. The original dataset is in the English language only.

Recently I came across a version of the dataset that was completely translated into the Dutch language. Use the following link for the dataset: [Alpaca Dutch Cleaned](https://www.huggingface.co/datasets/BramVanroy/alpaca-cleaned-dutch)

During training of the first Colab Notebook the dataset was split into a training and validation part. The size of the validation set is 2048 rows.
Since I would like to be able to compare the various training runs and evaluation results the training and validation datasets are stored within a subfolder (alpaca_clean_dutch) in this Github repo.

## References

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