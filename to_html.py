def html_to_str(filename):
    with open(filename) as htmlfile:
        return htmlfile.read()
