from dataclasses import dataclass
import logging
from typing import Any, TypedDict
from flask_restful import reqparse, Resource
import requests

from config import JOB_BOARD_URL

class JobBoardSchema(TypedDict):
    host: str
    url: str
    filename_format: str

class JobBoard:
  @staticmethod
  def add(url:str, payload:JobBoardSchema):
    response = requests.post(url, data=payload)
    response.raise_for_status()

  @staticmethod
  def get_all(url)->list[dict[str, Any]]:
    response = requests.get(f"{url}/all")
    print(response.json())
    response.raise_for_status()
    return response.json()

parser = reqparse.RequestParser()
parser.add_argument('job_board')

class JobBoardsResource(Resource):
    def post(self):
      try:
        args = parser.parse_args()
        payload = args['job_board']
        JobBoard.add(JOB_BOARD_URL, payload)  # type: ignore
        return payload, 201
      except Exception as err:
        logging.error("An exception occurred ::", err)
        return {'error': err}, 500

class JobBoardResource(Resource):
    def get(self, job_board_id):
      try:
        response = JobBoard.get_all(JOB_BOARD_URL)
        return response, 200
      except Exception as err:
        logging.error("An exception occurred ::", err)
        return {'error': err}, 500



