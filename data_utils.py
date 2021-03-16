import os
import json
import pandas as pd

import xmltodict
import xml.etree.ElementTree as ET

from tqdm import tqdm


def xml_to_txt(in_path, out_path):
    """Converts .xml files to .txt files for preprocessing.
    Args:
        in_path  (path) : location of .xml input files
        out_path (path) : location of .txt output files
    """
    for root, dirs, in_files in os.walk(in_path):
        for in_file in tqdm(in_files):

            out_file = in_file.split('.')[0] + '.txt'
            with open(f'{in_path}/{in_file}', 'r') as i:
                tree = ET.parse(i)
                root = tree.getroot()
            i.close()

            with open(f'{out_path}/{out_file}', 'w') as o:
                for child in root:
                    o.write(child.tag + ' ' + child.text + '\n')
                    for grandchild in child:
                        o.write(grandchild.tag + ' ' + grandchild.text + '\n')
            o.close()
    return


def xml_to_csv(in_path, out_path):
    """Converts .xml files to .csv files for downstream merger step.
    Args:
        in_path  (str) : location of .xml input files
        out_path (str) : location of .csv output files
    """
    for root, dirs, in_files in os.walk(in_path):
        for in_file in tqdm(in_files):
            out_file = in_file.split('.')[0] + '.csv'
            with open(f'{in_path}/{in_file}', 'r') as i:
                xml_dict = json.dumps(xmltodict.parse(i.read()))
                json_dict = json.loads(xml_dict)
            
            df = pd.json_normalize(json_dict['clinical_study'])
            df.to_csv(f'{out_path}/{out_file}')
    return


def merge_csv_records(csv_path):
    """Combines all .csv files for downstream EDA and modeling.
    Args:
        csv_path (str) : location of .csv files to be combined
    """
    data_frames = []
    out_file = 'covid-19-clinical-trials-master.csv'
    
    for root, dirs, in_files in os.walk(csv_path):
        for in_file in tqdm(in_files):
            df = pd.read_csv(f'{csv_path}/{in_file}')
            data_frames.append(df)

    final_df = pd.concat(data_frames)
    final_df.to_csv(f'{csv_path}/{out_file}')