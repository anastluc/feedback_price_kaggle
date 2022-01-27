import pandas as pd
from termcolor import cprint
from argparse import ArgumentParser

def print_highlighted_text(text, discource_type):
    if discource_type == "Lead":
        cprint(text, 'white', 'on_blue')
    elif discource_type == "Position":
        cprint(text, 'white', 'on_green')
    elif discource_type == "Evidence":
        cprint(text, 'magenta', 'on_white')
    elif discource_type == "Claim":
        cprint(text, 'white', 'on_magenta')
    elif discource_type == "Concluding Statement":
        cprint(text, 'white', 'on_cyan')
    elif discource_type == "Counterclaim":
        cprint(text, 'red', 'on_white')
    elif discource_type == "Rebuttal":
        cprint(text, 'white', 'on_blue')
    else:
        cprint(text, 'white', 'on_grey')

def read_training_frame():
    df = pd.read_csv("../data/train.csv")
    return df

def print_essay_with_discource_highlighted(essay_id, legends=True, print_unlabelled_text=True):
    with open("../data/train/{}.txt".format(essay_id), "r") as f:
        full_essay_text = f.read()
    
    df = read_training_frame()
    annotations_frame = df[df["id"]==essay_id].sort_values(by="discourse_start",ascending=True)
    # print(len(full_essay_text))

    if not print_unlabelled_text:   
        for index, row in annotations_frame.iterrows():
            annotation_start = int(row["discourse_start"])
            annotation_end = int(row["discourse_end"])
            annotation_type = str(row["discourse_type"])

            print_highlighted_text(full_essay_text[annotation_start:annotation_end], annotation_type)
    
    else: 
        previous_start = -1
        for index, row in annotations_frame.iterrows():
            annotation_start = int(row["discourse_start"])
            annotation_end = int(row["discourse_end"])
            annotation_type = str(row["discourse_type"])

            # print the text between the previous and the current annotation
            if previous_start != annotation_start - 1:
                # print(f"I found a gap!", previous_start, annotation_start)
                print(full_essay_text[previous_start:annotation_end])
            
            print_highlighted_text(full_essay_text[annotation_start:annotation_end], annotation_type)
            
            previous_start =  annotation_end
        
        # print unlabelled text after the last annotation
        if annotation_end>len(full_essay_text):
            print(full_essay_text[annotation_end:])

            
    
    if legends:
        print("\nLegend:")
        print_highlighted_text("Lead", "Lead")
        print_highlighted_text("Position", "Position")
        print_highlighted_text("Evidence", "Evidence")
        print_highlighted_text("Claim", "Claim")
        print_highlighted_text("Concluding Statement", "Concluding Statement")
        print_highlighted_text("Counterclaim", "Counterclaim")
        print_highlighted_text("Rebuttal", "Rebuttal")
        print("Unlabelled")

def print_random():
    df = read_training_frame()
    essay_id = df["id"].sample(1).values[0]
    print(f"Printing essay {essay_id}\n")
    return print_essay_with_discource_highlighted(essay_id, True, True)

if __name__=="__main__":

    parser = ArgumentParser()

    parser.add_argument("--random", metavar="random", help="Print a random essay", nargs="?",const='random_set', default = "None")
    parser.add_argument("essay_id", metavar="essay_id", type=str, help="The essay id to print", nargs="?")
    

    args = parser.parse_args()

    # print(args)
    # print(args.random)
    # print(args.essay_id)

    if args.random is not None:
        print_random()
    elif args.essay_id is not None:
        print_essay_with_discource_highlighted(essay_id=args.essay_id, legends=True, print_unlabelled_text=True)
    else:
        print("Something went wrong")



# print_essay_with_discource_highlighted("DBF7EB6A9E02",True, True)