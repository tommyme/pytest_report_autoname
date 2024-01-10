from datetime import datetime
import os

def pytest_load_initial_conftests(args):
    today=datetime.now()
    formatted_today=today.strftime('%y_%m_%d__%H_%M_%S')
    if not os.path.exists("test_report"):
        os.mkdir("test_report")
    for id, i in enumerate(args):
        if "--html" in i:
            args[id] = "--html={}/report-{}.html".format('test_report',formatted_today)
