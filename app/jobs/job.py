import logging
from typing import Any
import requests
from flask_restful import reqparse, Resource
import requests
from config import JOB_URL

logging.basicConfig(level=logging.INFO)

class Job:
  @staticmethod
  def add(url:str, payload:dict[str, Any]):
    response = requests.post(url, data=payload)
    response.raise_for_status()

  @staticmethod
  def add_bulk(url, payload:list[dict[str, Any]]):
    response = requests.post(url, data=payload)  # type: ignore
    response.raise_for_status()

  @staticmethod
  def delete(url, id)->list[dict[str, Any]]:
    response = requests.delete(f"{url}/{id}")
    response.raise_for_status()
    return response.json()



parser = reqparse.RequestParser()
parser.add_argument('job')
parser.add_argument('jobs')

class JobsResource(Resource):
    def post(self):
      try:
        args = parser.parse_args()
        payload = args['job']

        if args['job']:
          Job.add(JOB_URL, args['job'])  # type: ignore
        elif args['jobs']:
          Job.add_bulk(JOB_URL, args['jobs'])  # type: ignore

        return payload, 201
      except Exception as err:
        logging.error("An exception occurred ::", err)
        return {'error': err}, 500

class JobResource(Resource):
    def delete(self, job_id):
      try:
        Job.delete(JOB_URL, job_id)  # type: ignore
        return job_id, 200
      except Exception as err:
        logging.error("An exception occurred ::", err)
        return {'error': err}, 500


