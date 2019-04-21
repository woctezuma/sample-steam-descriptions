# Sample Steam Descriptions

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to sample Steam store descriptions, with the GPT-2 language model.

![Generated description, using GPT-2](https://github.com/woctezuma/sample-steam-descriptions/wiki/img/cover.png)

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Download app details, which include Steam store descriptions

Store descriptions are parsed from app details, which can be downloaded with `steam_spy.py` in my [`steam-api`](https://github.com/woctezuma/steam-api) repository.

A data snapshot is available in my [`steam-api-data`](https://github.com/woctezuma/steam-api-data) Github repository.

### Concatenate Steam store descriptions in a large text file

```
python export_description_data.py
```

A data snapshot is available in [`data/`](data/).

### Fine-tune a pre-trained GPT-2 model

Run the [`gpt_2_for_descriptions.ipynb`](gpt_2_for_descriptions.ipynb) notebook on [Google Colab](https://colab.research.google.com/), which relies on the [`gpt_2_simple`](https://github.com/minimaxir/gpt-2-simple) package.

## Results

Results obtained after 5000 steps:

-   [Unconditional generation](https://github.com/woctezuma/sample-steam-descriptions/wiki/Unconditional_Generation)
-   [Half-life 3](https://github.com/woctezuma/sample-steam-descriptions/wiki/Half_Life_3)
-   [Spelunky 2](https://github.com/woctezuma/sample-steam-descriptions/wiki/Spelunky_2)

## References

-   [OpenAI, a blog post about GPT-2, 2019](https://openai.com/blog/better-language-models/)
-   [Max Woolf, API for GPT-2, 2019](https://github.com/minimaxir/gpt-2-simple)
-   My repositories to sample reviews for Steam games:
    - [`sample-steam-reviews`](https://github.com/woctezuma/sample-steam-reviews)
    - [`sample-steam-reviews-with-gpt-2`](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2)

[build]: <https://travis-ci.org/woctezuma/sample-steam-descriptions>
[build-image]: <https://travis-ci.org/woctezuma/sample-steam-descriptions.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/sample-steam-descriptions/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-descriptions/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-descriptions/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/sample-steam-descriptions>
[codecov-image]: <https://codecov.io/gh/woctezuma/sample-steam-descriptions/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/sample-steam-descriptions>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/4d9e2b7f7ed54542972038cf7a9e7e6c>
