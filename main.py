from flask import Flask
from sqlalchemy import create_engine
from models.base import Base
from services.DepartmentsService import DepartmentService
from services.JobsService import JobsService
from services.HiredEmployeesService import HiredEmployeesService
from controllers.DepartmentsController import init_departments_controller, departments_bp
from controllers.JobsController import init_jobs_controller, jobs_bp
from controllers.HiredEmployeesController import init_hired_employees_controller, hired_employees_bp
from controllers.root import rootpath
import os

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT", "3306")
db_name = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

department_service = DepartmentService(engine)
job_service = JobsService(engine)
hired_employees_service = HiredEmployeesService(engine)

app = Flask(__name__)

init_departments_controller(department_service)
init_jobs_controller(job_service)
init_hired_employees_controller(hired_employees_service)

app.register_blueprint(departments_bp, url_prefix='/departments')
app.register_blueprint(jobs_bp, url_prefix='/jobs')
app.register_blueprint(hired_employees_bp, url_prefix='/hiredemployees')
app.register_blueprint(rootpath)


