import json
from dataclasses import dataclass
from numpy import ndarray


@dataclass
class Result:
    value: ndarray

    def to_json(self):
        return json.dumps({
            'result': self.value.tolist()
        })
