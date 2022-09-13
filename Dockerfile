# 建立python3.8环境
FROM python:3.8

# 作者徐昭
MAINTAINER xuzhao

# 在容器内环境文件夹
RUN mkdir -p /u01/web/zhique-service

# 设置容器内工作目录
WORKDIR /u01/web/zhique-service

# 将当前目录文件加入到容器工作目录中
ADD . /u01/web/zhique-service

COPY ./docker/pip.conf /root/.pip/pip.conf

RUN pip3 install -r requirements.txt

COPY ./docker/enterpoint.sh /u01/web/zhique-service

RUN chmod 777 /u01/web/zhique-service/enterpoint.sh

ENTRYPOINT ["sh", "/u01/web/zhique-service/enterpoint.sh"]

EXPOSE 8000
