from flask import Flask

from flask_apscheduler import APScheduler
from flask_restful import Api
from config import PORT
from jobs.job import JobsResource, JobResource
from jobs.board import JobBoardResource, JobBoardsResource

from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    api = Api(app)
    api.add_resource(JobBoardsResource, '/job-boards/')
    api.add_resource(JobBoardResource, '/job-boards/<job_board_id>')
    api.add_resource(JobsResource, '/jobs/')
    api.add_resource(JobResource, '/job/<job_id>')

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=PORT)

