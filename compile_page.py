from math import floor

from util.file_utils import create_result_template


def generate_form(labels_list):
    create_result_template()

    file = open('result.html', "r")
    page_content = file.readlines()
    file.close()

    page_content = generate_elements(page_content, labels_list)
    page_content = generate_ids(page_content, labels_list)

    file = open('result.html', "w")
    page_content = "".join(page_content)
    file.write(page_content)
    file.close()

    print("Page Generated from uploaded sketch.")


def generate_elements(content, l_list):
    for outer_index, html_line in enumerate(content):
        if '<form' in html_line:
            for inner_index, label in enumerate(l_list):
                content.insert(outer_index + 2, get_element(label[0], inner_index + 1))
    return content


def get_element(element_name, index):
    if element_name == 'dropdown':
        return "\n\t\t<input id=\"s" + str(index) + "\" list=\"items\" name=\"item\">\n" + \
               "\t\t<datalist id=\"items\">\n" + \
               "\t\t\t<option value=\"Item 1\">\n" + \
               "\t\t\t<option value=\"Item 2\">\n" + \
               "\t\t\t<option value=\"Item 3\">\n" + \
               "\t\t</datalist>\n\n"
    else:
        return "\t\t<input type=\"" + element_name + "\" id=\"s" + str(index) + "\">\n"


def generate_ids(content, l_list):
    for outer_index, html_line in enumerate(content):
        if '<style' in html_line:
            for inner_index, label in enumerate(l_list):
                if len(label) == 5:
                    del label[0]  # Deletes class from list
                content.insert(outer_index + 2, get_id(label, inner_index + 1))
    return content


def get_id(positions, index):
    page_positions = cal_positions_on_page(positions)

    return "#s" + str(index) + " {\n" + \
           "\tposition: absolute;\n" + \
           "\tmargin-top: " + str(page_positions[0]) + "px;\n" + \
           "\tmargin-left: " + str(page_positions[1]) + "px;\n" + \
           "\twidth: " + str(page_positions[2]) + "px;\n" + \
           "\theight: " + str(page_positions[3]) + "px;\n" + \
           "}\n\n"


def cal_positions_on_page(positions):
    height = 810  # pixels
    width = 1440  # pixels

    return [floor((float(positions[1]) - (float(positions[3]) / 2)) * height),  # margin-top
            floor((float(positions[0]) - (float(positions[2]) / 2)) * width),  # margin-left
            floor(float(positions[2]) * width),  # width
            floor(float(positions[3]) * height)]  # height
