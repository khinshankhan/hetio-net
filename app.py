import os

from utils import tsv_splitter
from utils.neo4j import Neo4jController
from utils.mongo import MongoController


WELCOME_MESSAGE = '''Welcome!

This is a simulation of Hetio Net, an integrative network of biomedical
knowledge assembled from 29 different databases of genes, compounds, diseases,
and more. The network combines over 50 years of biomedical information into a
single resource, consisting of 47,031 nodes (11 types) and 2,250,197
relationships (24 types).


This simulation will attempt to answer 2 queries:'''

QUERIES = '''
1 -> Given a disease, what is its name, what are drug names that can treat or
palliate this disease, what are gene names that cause this disease, and where
this disease occurs?

2 -> Supposed that a drug can treat a disease if the drug or its similar drugs
up-regulate/down-regulate a gene, but the location down-regulates/up-regulates
the gene in an opposite direction where the disease occurs. Find all drugs
that can treat new diseases (i.e. the missing edges between drug and disease).
'''

EXITING = '''
y -> Yes, done with program. We should exit program.

n -> No, we still have other queries. We should continue program.
'''


def clear_screen():
    "Clears the screen depending on OS"
    os.system('cls' if os.name == 'nt' else 'clear')


def user_input(choice_details, choices):
    "Handle user input and validation."
    choice = None

    while True:
        choice = input("Enter your choice: ")
        if not choices or choice in choices:
            print()
            break

        clear_screen()
        print("Invalid choice! remember the choices are: ")
        print(choice_details)

    return choice


def main():
    "Executes splash screen and UI to use Hetio Net."

    # take edge and node tsv files and split them up by type
    tsv_splitter.write_node_files()
    tsv_splitter.write_edge_files()

    # define dbs for queries
    mongo_controller = MongoController()
    mongo_controller.create_db()

    neo4j_controller = Neo4jController()
    neo4j_controller.create_db()

    clear_screen()
    print(WELCOME_MESSAGE)

    while True:
        # get user query choice
        print('Query Choices:', QUERIES)
        choice = user_input(QUERIES, ('1', '2'))
        # get information relevant to choice
        clear_screen()
        msg = 'disease' if choice == '1' else 'drug'
        msg = f'Next, for the query, enter the name of the relevant {msg}: '
        query = input(msg)
        # get query from related db
        clear_screen()
        controller = mongo_controller if choice == '1' else neo4j_controller
        controller.query_db(query)
        # ask to exit at this point
        print('\n\n\n\n\nWould you like to exit the program now?', EXITING)
        choice = user_input(EXITING, ('y', 'n'))
        clear_screen()
        if choice == 'y':
            break

    print('Goodbye!')


if __name__ == "__main__":
    # run main program
    main()
