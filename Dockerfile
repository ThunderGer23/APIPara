FROM python:3.9.6

WORKDIR /code

RUN apt-get update
RUN apt-get install -y wget
RUN apt-key del 7fa2af80
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/tensorrt-libs_8.5.3.1-1+cuda11.8_amd64.deb
RUN dpkg -i tensorrt-libs_8.5.3.1-1+cuda11.8_amd64.deb

ENV PYHTONUNBUFFERED=1
RUN export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64

COPY ./ /code
RUN python -m pip install --upgrade pip
RUN pip install -U --no-cache-dir -r /code/requirements.txt

RUN python -m decompress /code/Parafra_Red/pytorch_model.zip /code/Parafra_Red/pytorch_model.bin

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]