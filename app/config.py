import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """App configuration."""

    JOBS = [
        {
            "id": "pipeline_job",
            "func": "pipeline:Pipeline.process",
            "trigger": "cron",
            "hour": "6",
        }
    ]

    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}
    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}
    SCHEDULER_API_ENABLED = True

JOB_BOARD_URL = os.getenv("JOB_BOARD_URL")
JOB_URL = os.getenv("JOB_BOARD_URL")
PORT = int(os.getenv("PORT", 5000))
