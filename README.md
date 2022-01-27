# Feedback price kaggle competition

## Task

The task is decribed here https://www.kaggle.com/c/feedback-prize-2021/overview

## Getting the data

Assuming you have kaggle CLI installed:
```
kaggle competitions download -c feedback-prize-2021
```

## Print some data
Use the following CLI to visualise an essay:
```
cd code
python print_essay.py --random
python print_essay.py [essay_id]
```