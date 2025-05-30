import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('example.xml')
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)
        if subchild.tag == 'timingExbytes':

            st = ET.SubElement(subchild, 'custom_sub_tag')
            st.text = 'some text'


            for c_of_timingExbytes in subchild:
                print(f'timingExbytes: {c_of_timingExbytes.tag}, {c_of_timingExbytes.text}')


tree = ET.ElementTree(root)
tree.write('output_updated.xml')
