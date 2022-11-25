from datetime import datetime, timedelta
import json
import logging
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
from jobs.board import JobBoard
from config import JOB_BOARD_URL
from xml_parser.xmlHandler import XmlHandler
from xml_parser.etParser import ETParser


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def get_date_yesterday()->tuple[str, str, str]:
  yesterday = datetime.now() - timedelta(1)
  year = yesterday.strftime('%Y')
  month = yesterday.strftime('%m')
  date = yesterday.strftime('%d')

  return (year, month, date)


class Pipeline:
  @staticmethod
  def process():
    try:
      job_boards = JobBoard.get_all(JOB_BOARD_URL)
      NUMBER_OF_PROCESSES = cpu_count() - 2
      pool = Pool(NUMBER_OF_PROCESSES)
      pool.map(Pipeline._pipeline, job_boards)

    except Exception as e:
      logging.error("An exception occurred ::", e)


  @staticmethod
  def _pipeline(job_board):
    date = get_date_yesterday()
    job_board = job_board.replace("'", '"')
    job_board = json.loads(job_board)

    filename = job_board['filename_format'].format(year=date[0], month=date[1],date=date[2])
    url = f"{job_board['url']}{filename}"

    filename = XmlHandler.download(url)
    parser = ETParser(filename)
    parsed_res = parser.parse()
    logging.info(f"Parsed {len(parsed_res)} jobs")
    XmlHandler.delete(filename)

if __name__ == "__main__":
  Pipeline.process()
