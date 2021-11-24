import os

def read_grammar(filename):
    """
    reads the rules of a context free grammar from a text file
    :param filename: name of the text file in current directory
    :return: two lists. v_rules lead to variables and t_rules
    lead to terminals.
    """
    filename = os.path.join(os.curdir, filename)
    with open(filename) as grammar:
        rules = grammar.readlines()
        v_rules = []
        t_rules = []

        for rule in rules:
            left, right = rule.split(" -> ")

            # for two or more results from a variable
            right = right[:-1].split(" | ")
            for ri in right:

                # it is a terminal
                if not(str.isupper(ri)): # bukan kapital maka masuk ke terminal
                    t_rules.append([left, ri])

                # it is a variable
                else:
                    v_rules.append([left, ri.replace(" ", "")])
        # print(v_rules)
        # print(t_rules)
        return v_rules, t_rules