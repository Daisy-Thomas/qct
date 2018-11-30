import re
list_input=[]
def open_input(in_file):
    item=[]
    input_ptr = open(in_file, 'r')
    input_content = input_ptr.read()
    input_lines = input_content.split('\n')
    for lines in input_lines:
        if(re.search('mybls=',item)):
            iostream=item
        if(re.search('ref_csv=',item1)):
            csv=item1
        if(re.search('my_view=',item2)):
            view=item2
        if(re.search('DL1_component=',item)):
            DL1_comp=item
    return iostream,csv,view,DL1_comp
list_input=open_input('input.txt')
