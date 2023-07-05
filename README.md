# Dutch LLM's
Various training, inference and validation code and results related to Open LLM's that were pretrained (full or partially) on the Dutch language.

## Training and Evaluation

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

It is very clear that these models should not be used in any reallife or production scenario related to the Dutch language. The percentage of Dutch text within the training set was just to small for a serious usage.

That said, with all the issues mentioned above, it is still interresting to observe that a significant percentage of the generated answers make some sense in the Dutch language.

I'am looking forward to the first open LLM model that is trained on a dataset with a larger percentage of the data based on the Dutch language.

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