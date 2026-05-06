from etl.extract import extract
from etl.transform import transform
from etl.load import load
def pipeline():
  data=extract()
  data=transform(data)
  load(data)
