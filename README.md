# robo-advisor
Robo Advisor project for investing stocks

## Prerequisites
  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Clone the repo from (https://github.com/aaldridge81/robo-advisor), then navigate into the project repo

``` sh
cd robo-advisor
```

## Environment Setup

Use Anaconda to create and activate a new virtual environment, called "stocks-env"

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```

from inside virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: If installation causes an error message, make sure you are navigating within the repository's root directory, where the requirements.txt file exists 

## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your real API Key:
    
    ALPHAVANTAGE_API_KEY="abc123"



## Usage

To run the program, in the command line:
``` py
python app/robo_advisor.py
```
