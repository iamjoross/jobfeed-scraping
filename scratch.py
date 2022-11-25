  # # todo: try
  # # job_conn = Job("https://eopd1rh9mtrqb0.m.pipedream.net/jobs")
  # # # job_conn.remove("test.com")
  # # job_conn.add({'job': 1})

  # job_boards_conn = JobBoard("https://eoj57c5qqcjh1v6.m.pipedream.net/job-boards")
  # # job_conn.remove("test.com")
  # # job_boards_conn.add({
  # #   'host': 'theguardiannews.com',
  # #   "url": "https://jobfeed-assignment-data.s3.eu-west-1.amazonaws.com/",
  # #   "filename_format": "Jobs.{year}-{month}-{date}.0.xml"
  # # })
  from multiprocessing import cpu_count
from app.etParser import ETParser
from app.xmlHandler import XmlHandler
from memory_profiler import profile as MEM_PROFILER
import line_profiler
from timeit import default_timer as timer
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib3

url = 'https://jobfeed-assignment-data.s3.eu-west-1.amazonaws.com/Jobs.2022-07-07.0.xml'

def elem2dict(node, attributes=True):
    """
    Convert an lxml.etree node tree into a dict.
    """

    result = {}
    if attributes:
        for item in node.attrib.items():
            key, result[key] = item

    for element in node.iterchildren():
        # Remove namespace prefix
        key = element.tag.split('}')[1] if '}' in element.tag else element.tag

        # Process element as tree element if the inner XML contains non-whitespace content
        if element.text and element.text.strip():
            value = element.text
        else:
            value = elem2dict(element)
        if key in result:
            if type(result[key]) is list:
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value

    return result

def loadXML():

    # url of rss feed
    url = 'https://jobfeed-assignment-data.s3.eu-west-1.amazonaws.com/Jobs.2022-07-07.0.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open(url, 'r') as f:
        data = f.read()


def parseXML(xmlfile):

    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []


def main():

    loadXML()
    # parseXML("Jobs.2022-07-07.0.xml")


def aa():
    url = 'https://jobfeed-assignment-data.s3.eu-west-1.amazonaws.com/Jobs.2022-07-07.0.xml'

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="xml")
    # tree = ET.parse(response.data)


def download_xml():
    response = requests.get(url)
    with open('Jobs.2022-07-07.0.xml', 'wb') as file:
        file.write(response.content)


def sample_xml(opts, _url=url):
    """Return the sample XML file as a string."""
    with open(_url, opts) as xml:
        return xml.read()


def sample_xml_1(opts):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data

# xmltodict--------------------------------------------------------------------


def parse_xmltodict():
    import xmltodict

    xml_as_string = sample_xml_1('wb')

    timer_start = timer()

    print('[xmltodict] Starting to parse XML')

    xml_xmltodict = xmltodict.parse(xml_as_string, dict_constructor=dict)

    seconds = timer() - timer_start

    print(f'[xmltodict] Finished parsing XML in {seconds} seconds')


# etree with Python's standard library ----------------------------------------
def parse_etree_stdlib():
    import xml.etree.ElementTree as etree_stdlib

    xml_as_string = sample_xml_1('r')

    timer_start = timer()

    print('[etree stdlib] Starting to parse XML')

    tree = etree_stdlib.fromstring(xml_as_string)

    xml_etree_stdlib = tree.findall('./Job', {})

    seconds = timer() - timer_start

    print(f'[etree stdlib] Finished parsing XML in {seconds} seconds')


# etree with lxml -------------------------------------------------------------
# @MEM_PROFILER
def parse_etree_lxml():
    from lxml import etree as etree_lxml

    xml_as_bytes = sample_xml('rb', _url="Jobs.2022-07-07.0.xml")

    timer_start = timer()

    print('[etree lxml] Starting to parse XML')

    tree = etree_lxml.fromstring(xml_as_bytes)

    xml_etree_lxml = tree.findall('./Job', {})

    seconds = timer() - timer_start

    print(f'[etree lxml] Finished parsing XML in {seconds} seconds')

    timer_start = timer()
    a = [elem2dict(item) for item in xml_etree_lxml]
    seconds = timer() - timer_start
    print(seconds)

    num_workers = max(1, cpu_count() - 1)
    print(num_workers)
    print(len(a), len(a)//num_workers)

def test():
    all_records = []
    is_a_job = False
    job = {}
    prev_tag = None
    for event, elem in ET.iterparse("Jobs.2022-07-07.0.xml", events=("start", "end")):
        if event == "start":
            if elem.tag == "Job":
                is_a_job = True
                job= {}
            if job is not None and elem.tag != "Job":
                if elem.tag == 'entry' and isinstance(job[prev_tag], str):
                    job[prev_tag] = [elem.text]
                elif elem.tag == 'entry' and isinstance(job[prev_tag], list):
                    job[prev_tag].append(elem.text)
                else:
                    job[elem.tag] = elem.text
                    prev_tag = elem.tag

        else:  # elif event == "end"
              if job is not None:
                if elem.tag == "Job" and is_a_job:
                    all_records.append(job)
                    job = None
                    is_a_job = False

        elem.clear()
    print(len(all_records)) #5878
    print(all_records[0])

        # if event == "end":
        #     print(elem.tag, 'text=', elem.text)


if __name__ == "__main__":
    # parse_xmltodict()
    # parse_etree_stdlib()
    # parse_etree_lxml()
    # test()
    xml_filename = XmlHandler.download(url)
    print(xml_filename)
    # results = ETParser("Jobs.2022-07-07.0.xml").parse()
    # print(len(results))
    # from line_profiler import LineProfiler

    # lprofiler = LineProfiler()

    # lp_wrapper = lprofiler(parse_etree_lxml)

    # lp_wrapper()
    # lprofiler.print_stats()


#
