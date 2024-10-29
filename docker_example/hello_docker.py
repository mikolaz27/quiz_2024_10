import datetime
from time import sleep

import pandas as pd

while True:
    df = pd.DataFrame(
        data={"timestamp": [datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(7)], "col2": [2, 3]}
    )
    print(f"{df}")
    sleep(2)


# docker build -t my_image .

# docker run --rm -it -d --name my_cont  my_image
#  docker exec -it quiz_cont /bin/sh


# docker run --rm -it --name my_cont -p 8010:8008  quiz_image


# docker run --rm -it --name my_cont -p 8010:8000 -v D:\Hillel\quiz_2024_10\quiz_2024_10\src:/quiz/src
# quiz_image ./commands/start_server_dev.sh
