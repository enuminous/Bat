import json
import pandas as pd
from bat import BATExperiment

df=pd.read_csv("example_data.csv")
exp=BATExperiment(
    time_column="time",
    target_column="future_event",
    feature_columns=["signal_a","signal_b","signal_c"],
    random_state=23,
    material_brier_gain=0.002,
)
print(json.dumps(exp.run(df),indent=2))
