import xml.etree.ElementTree as ET
import xml.sax
import datetime
import matplotlib.pyplot as plt

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.current_tag = ''
        self.current_namespace = ''

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == 'namespace':
            self.current_namespace = attributes.get('value', '')

    def endElement(self, tag):
        if self.current_tag == 'term' and self.current_namespace in self.counts:
            self.counts[self.current_namespace] += 1

    def characters(self, content):
        pass

def parse_with_dom(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    for term in root.findall('.//term'):
        namespace = term.find('namespace').text
        if namespace in counts:
            counts[namespace] += 1
    return counts


def parse_with_sax(xml_file):
    counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    return handler.counts


xml_file = 'c:/Users/lhx\Desktop/IBI1/IBI1_2023-24/Practical14/go_obo.xml'


start_time_dom = datetime.datetime.now()
dom_counts = parse_with_dom(xml_file)
end_time_dom = datetime.datetime.now()


start_time_sax = datetime.datetime.now()
sax_counts = parse_with_sax(xml_file)
end_time_sax = datetime.datetime.now()


print("DOM API counts:", dom_counts)
print("SAX API counts:", sax_counts)


labels = ['Molecular Function', 'Biological Process', 'Cellular Component']
dom_bars = dom_counts.values()
sax_bars = sax_counts.values()

plt.figure(figsize=(10, 6))
plt.bar(labels, dom_bars, label='DOM API')
plt.bar(labels, sax_bars, label='SAX API', alpha=0.5)
plt.legend()
plt.title('GO Term Counts in Three Ontologies')
plt.xlabel('Ontology')
plt.ylabel('Number of Terms')
plt.show()


dom_time = (end_time_dom - start_time_dom).total_seconds()
sax_time = (end_time_sax - start_time_sax).total_seconds()

print(f"DOM API took {dom_time} seconds")
print(f"SAX API took {sax_time} seconds")


if dom_time < sax_time:
    print("# DOM API was faster")
else:
    print("# SAX API was faster")