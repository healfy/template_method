import os
import pytest
import json
from app.core.main import Worker
from app.core.settings import Settings
from app.core.base import SumWithMatrix, Transposition, GetDeternminant


@pytest.mark.parametrize('method, result, handler', [
    ('transpose', [[1, 3], [2, 4]], Transposition),
    ('sum', [[2, 4], [6, 8]], SumWithMatrix),
    ('determinant', -2.0000000000000004, GetDeternminant),
])
def test_worker(method, result, handler):
    file1, file2 = 'test.json', 'dest.json'

    with open(os.path.join(Settings.BASE_DIR, file1), 'w') as f:
        f.write(json.dumps({"matrix": [[1, 2], [3, 4]]}))

    worker = Worker(file1, file2, method)
    worker.run()
    assert worker.handler == handler

    with open(worker.dest, 'r') as f:
        data = json.load(f)
    assert result == data['result']

    os.remove(os.path.join(Settings.BASE_DIR, file2))
    os.remove(os.path.join(Settings.BASE_DIR, file1))
