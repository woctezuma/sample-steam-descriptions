# Sample Steam Descriptions

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to sample Steam store descriptions, with the GPT-2 language model.

![Generated description, using GPT-2](https://github.com/woctezuma/sample-steam-reviews/wiki/img/cover.png)

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/). For CNTK, you will need Python 3.6.
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Download Steam descriptions

```
python download_description_data.py
```

### Concatenate descriptions in a large text file

```
python export_description_data.py
```

### Fine-tune a pre-trained GPT-2 model

Run the [`gpt_2_for_descriptions.ipynb`](gpt_2_for_descriptions.ipynb) notebook on Google Colab, which relies on the [`gpt_2_simple`](https://github.com/minimaxir/gpt-2-simple) package.

## Results

Seed:
```
```

Generated samples:
```
TODO
```

## References

-   [OpenAI, a blog post about GPT-2, 2019](https://openai.com/blog/better-language-models/)
-   [Max Woolf, API for GPT-2, 2019](https://github.com/minimaxir/gpt-2-simple)
-   My repository to sample reviews for Steam games: [`sample-steam-reviews`](https://github.com/woctezuma/sample-steam-reviews)

[build]: <https://travis-ci.org/woctezuma/sample-steam-descriptions>
[build-image]: <https://travis-ci.org/woctezuma/sample-steam-descriptions.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/sample-steam-descriptions/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-descriptions/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-descriptions/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/sample-steam-descriptions>
[codecov-image]: <https://codecov.io/gh/woctezuma/sample-steam-descriptions/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/sample-steam-descriptions>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/TODO>
