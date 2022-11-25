import logging
import os
from typing import Any
import xml.etree.ElementTree as ET

from xml_parser.constants import END, ENTRY_TAG_NAME, JOB_TAG_NAME, START

logging.basicConfig(level=logging.INFO)

class ETParser:
  def __init__(self, file_url: str):
    self._file_url: str = file_url
    self._is_a_job: bool = False
    self.results: list[dict[str, Any]] = []
    self._prev_tag: str = ""

  def parse(self) -> list[dict[str, Any]]:
    logging.info(f"Parsing...")
    _job: dict[str, Any] | None = {}

    url = f"{os.path.abspath(os.curdir)}/temp/{self._file_url}"
    if not os.path.exists(url):
        raise FileNotFoundError

    for event, elem in ET.iterparse(url, events=(START, END)):
        if event == START:
            if elem.tag == JOB_TAG_NAME:
                self._is_a_job = True
                _job= {}
            if _job is not None and elem.tag != JOB_TAG_NAME:
                if elem.tag == ENTRY_TAG_NAME and isinstance(_job[self._prev_tag], str):
                    _job[self._prev_tag] = [elem.text]
                elif elem.tag == ENTRY_TAG_NAME and isinstance(_job[self._prev_tag], list):
                    _job[self._prev_tag].append(elem.text)
                else:
                    _job[elem.tag] = elem.text
                    self._prev_tag = elem.tag
        else:
              if _job is not None:
                if elem.tag == JOB_TAG_NAME and self._is_a_job:
                    self.results.append(_job)
                    _job = None
                    self._is_a_job = False

        elem.clear()

    return self.results

