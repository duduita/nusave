import json
import pandas as pd
from general_info import GeneralInfo
from statistics import Statistics
from advisor import UserAdvisor


class DataAPI:

    def ReadInstructions(self, instruction: json):
        info = json.load(instruction)
        
