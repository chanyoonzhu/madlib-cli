import re

def parse_blanks(template):
    blanks = []
    regexp = r'\{.*?\}'
    matches = re.findall(regexp, template)
    for item in matches:
        blanks.append(item)
    return blanks

def parse_original(template):
    regexp = r'\{.*?\}'
    return re.split(regexp, template)

def get_input(blanks):
    prompt = "Please type in a(n) "
    inputs = []
    for blank in blanks:
        input_value = input(prompt + blank.lower() + ": ")
        inputs.append(input_value)
    return inputs

def get_result(original_parsed, inputs):
    output = []
    for i in range(len(inputs)):
        if i < len(original_parsed):
            output.append(original_parsed[i])
        output.append(inputs[i])
    for i in range(len(inputs), len(original_parsed)):
        output.append(original_parsed[i])
    return ''.join(output)

def display(content):
    print(content)

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def write_to_file(content):
    with open('assets/output.txt', 'w') as file:
        file.write(content)

def welcome():
    print("welcome to the mad lib game!")
    
def main():
    welcome()
    template = read_file('assets/template.txt')
    blanks = parse_blanks(template)
    original = parse_original(template)
    inputs = get_input(blanks)
    output = get_result(original, inputs)
    display(output)
    write_to_file(output)

if __name__ == "__main__":
    main()

