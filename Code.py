from openpyxl import load_workbook
import os
from jinja2 import Template

file_path = os.path.dirname(os.path.realpath(__file__))
wb = load_workbook(filename = file_path + '/input/1.xlsx',read_only=True)

with open(file_path + '/input_template/telemetry.j2','r') as f:
    Temp = f.read()

def Create_config(node):
    with open(file_path + f"/output/{node['node_name']}.txt", 'w+') as file_open:
        config_command = Template(Temp).render(**node)
        file_open.write(config_command)
        print(f"**** file created for {node['node_name']}")
for row in wb.active.rows:
    node = {}
    node['node_name'] = row[0].value
    node['role'] = row[1].value
    node['PM_IP'] = row[2].value
    node['PM_Port'] = row[3].value
    Create_config(node)