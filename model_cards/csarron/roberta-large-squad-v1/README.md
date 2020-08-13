---
language: en
thumbnail: 
license: mit
tags:
- question-answering
- roberta
- roberta-large
datasets:
- squad
metrics:
- squad
widget:
- text: "Which name is also used to describe the Amazon rainforest in English?"
  context: "The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain \"Amazonas\" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species."
- text: "How many square kilometers of rainforest is covered in the basin?"
  context: "The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain \"Amazonas\" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species."
---

## RoBERTa-large fine-tuned on SQuAD v1

This model was fine-tuned from the HuggingFace [RoBERTa](https://arxiv.org/abs/1907.11692) base checkpoint on [SQuAD1.1](https://rajpurkar.github.io/SQuAD-explorer).
This model is case-sensitive: it makes a difference between english and English.

## Details

| Dataset  | Split | # samples |
| -------- | ----- | --------- |
| SQuAD1.1 | train | 96.8K      |
| SQuAD1.1 | eval  | 11.8k     |


### Fine-tuning
- Python: `3.7.5`

- Machine specs: 

  `CPU: Intel(R) Core(TM) i9-7900X CPU @ 3.30GHz`
  
  `Memory: 64 GiB`

  `GPUs: 2 GeForce GTX 1080 Ti, each with 11.2GiB memory`
  
  `GPU driver: 418.39, CUDA: 10.1`

- script:

  ```shell
  # after install https://github.com/huggingface/transformers

  cd examples/question-answering
  mkdir -p data

  wget -O data/train-v1.1.json https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json

  wget -O data/dev-v1.1.json  https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json

  python run_squad.py \
    --model_type roberta \
    --model_name_or_path roberta-large \
    --do_train \
    --do_eval \
    --train_file train-v1.1.json \
    --predict_file dev-v1.1.json \
    --per_gpu_train_batch_size 4 \
    --per_gpu_eval_batch_size 10 \
    --learning_rate 2e-5 --save_steps 4000 \
    --num_train_epochs 2.0 \
    --max_seq_length 320 \
    --doc_stride 128 \
    --data_dir data --warmup_steps 2400 \
    --output_dir data/roberta-large-squad-v1 2>&1 | tee train-roberta-large-squad-v1-warmup.log
  ```

It took about 5 and half hours to finish.

### Results

**Model size**: `1.4G`

| Metric | # Value   | [# Original](https://github.com/pytorch/fairseq/tree/master/examples/roberta#results)|
| ------ | --------- | --------- |
| **EM** | **87.5** | **88.9** |
| **F1** | **93.8** | **94.6** |

Note that the above results didn't involve any hyperparameter search.

## Example Usage


```python
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="csarron/roberta-large-squad-v1",
    tokenizer="csarron/roberta-large-squad-v1"
)

predictions = qa_pipeline({
    'context': "The game was played on February 7, 2016 at Levi's Stadium in the San Francisco Bay Area at Santa Clara, California.",
    'question': "What day was the game played on?"
})

print(predictions)
# output:
# {'score': 0.8625259399414062, 'start': 23, 'end': 39, 'answer': 'February 7, 2016'}
```

> Created by [Qingqing Cao](https://awk.ai/) | [GitHub](https://github.com/csarron) | [Twitter](https://twitter.com/sysnlp) 

> Made with ❤️ in New York.
