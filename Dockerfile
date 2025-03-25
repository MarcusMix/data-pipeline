# Use a imagem base do Apache Airflow
FROM apache/airflow:2.5.1

USER root

# Definição das variáveis de ambiente
ENV AIRFLOW_GPL_UNIDECODE=yes
ENV AIRFLOW_HOME=/home/airflow

# Instala as dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libnss3 \
    libxss1 \
    libappindicator1 \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libx11-xcb1 \
    xdg-utils \
    gcc \
    g++ \
    python3-dev \
    libxml2 \
    libxslt1-dev \
    zlib1g-dev \
    --no-install-recommends

# Instalação do Google Chrome
RUN apt-get update && apt-get install -y wget gnupg
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# Instalação do ChromeDriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# Definição das permissões para o Chrome
RUN chmod +x /usr/bin/google-chrome-stable
RUN chmod +x /usr/bin/google-chrome

# Mudar para o usuário airflow
USER airflow

# Instalação do Scrapy e dependências com pip (fazendo isso como root)
RUN pip install scrapy selenium pandas webdriver_manager

# Setando o path pq senão o scrapy não carrega
ENV PATH="/home/airflow/.local/bin:$PATH"
ENV PYTHONPATH="/home/airflow/.local/lib/python3.7/site-packages:$PYTHONPATH"

# Verificar a instalação do Scrapy
RUN scrapy version

# Garantir que o diretório do Airflow tenha as permissões corretas
RUN chmod -R 777 /home/airflow/.local/bin/scrapy
RUN chmod -R 777 /opt/airflow
