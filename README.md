# Wikipedia/DBpedia NLP Project

This project provided me with a solid foundation in clustering algorithms and Natural Language Processing (NLP). By leveraging data from DBpedia, I developed a tool that allows users to search for a specific person of interest within the dataset. Once a person is selected, the tool employs a K-Nearest Neighbors (KNN) algorithm to identify and suggest the most similar individuals based on their description!

## Usage

In a bash terminal:

1. Clone the repo:

```bash
git clone https://github.com/brooksburkhead/wikipedia-nlp.git
```

2. Download data:

```bash
curl -K https://ddc-datascience.s3.amazonaws.com/Projects/Project.5-NLP/Data/NLP.csv >> data/dbpedia.csv
```

3. Create a virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Have fun exploring DBpedia data!

```bash
python3 main.py
```
