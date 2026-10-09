from sklearn.preprocessing import StandardScaler  # AI signal
from google.cloud import bigquery
TABLE = "murali-test-gcp.ds_4471_eu.t_scored_src"   # provides: this exact dotted FQN (== model consumes)
bq = bigquery.Client()
bq.query(f"""
  CREATE OR REPLACE TABLE `{TABLE}` AS
  SELECT feature_a, feature_b, label FROM `murali-test-gcp.raw.events`;
  CREATE OR REPLACE MODEL `murali-test-gcp.ds_4471_eu.m_8842`
  OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['label']) AS
  SELECT * FROM `{TABLE}`;
""")
