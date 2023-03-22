from sqlalchemy import create_engine, text
import os

db_url = os.environ['DB_CONN_STRING']
engine = create_engine(url=db_url,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
  return jobs
