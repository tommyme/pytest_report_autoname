from datetime import datetime
import os

def pytest_load_initial_conftests(args):
    today=datetime.now()
    formatted_today=today.strftime('%y_%m_%d__%H_%M_%S')
    for id, i in enumerate(args):
        if "--html" in i:
            # 指定生成html的时候再创建文件夹
            if not os.path.exists("test_report"):
                os.mkdir("test_report")
            args[id] = "--html={}/report-{}.html".format('test_report',formatted_today)
