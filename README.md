<!-- You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 3 -->
<h2>Documentação Pipeline de Dados e ETL com Apache Airflow</h2>
<h2>Sumário</h2>
<h2>Introdução</h2>
<h3>Pipeline de Dados e ETL - Orquestrando scripts de web scraping e API,
transformando os dados e adicionando a uma planilha.</h3>
<p>
Automação de Web Scraping, API Consumer e acompanhamento de métricas e KPIs.
</p>
<h3>Descrição</h3>
<p>
Este projeto tem como principal objetivo automatizar a extração de informações
sobre aplicativos das lojas Apple App Store e Google Play Store. Ele gera dois
documentos:
</p>
<ol>
<li><strong>Relatório de Avaliações de Usuários</strong>: Contém comentários,
notas e datas das avaliações feitas pelos usuários.
<li><strong>Relatório de Desempenho Geral</strong>: Inclui a nota total do
aplicativo, a quantidade de downloads e o número total de avaliações.
</li>
</ol>
<h3>Autor</h3>
<p>
Marcus Sandi
</p>
<h3>Data de Início e Término</h3>
<ul>
<li>Início: 12/06/2024
<li>Término: em andamento
</li>
</ul>
<h2>Escopo do Projeto</h2>
<h3>Objetivos</h3>
<ul>
<li>Otimizar o tempo de trabalho dos colaboradores envolvidos.
<li>Coletar dados automaticamente de fontes da web e APIs.
<li>Processar e limpar os dados coletados.
<li>Armazenar os dados em planilhas do Google.
<li>Criar dashboards interativos para visualização das métricas.
<li>Automatizar a execução dessas tarefas utilizando Apache Airflow.
<li>Criar um acompanhamento semanal das informações.
<li>Identificar padrões nos dados.
</li>
</ul>
<h3>Requisitos</h3>
<ul>
<li>Automatizar o processo de coleta dos dados dos aplicativos.
<li>Gerar relatórios com os dados extraídos.
<li>Web scraping de dados de pelo menos 3 fontes diferentes.
<li>Consumo de dados da API do iTunes.
<li>Armazenamento dos dados em planilhas do Google.
<li>Desenvolvimento de dashboards em Looker Stúdio.
<li>Orquestração de todas as tarefas utilizando Apache Airflow.
<li>Criar uma base de dados robusta com os dados processados.
</li>
</ul>
<h3>Limitações</h3>
<ul>
<li>Desenvolvimento complexo.
<li>Enfrentamento de diversos bugs e erros.
<li>Limitação da taxa de acesso a algumas APIs.
<li>Bloqueio dos bots de web scraping por alguns sites.
<li>Google Sheets API bloqueia muitas requisições.
</li>
</ul>
<h2>Arquitetura do Sistema</h2>
<h3>Diagrama de Arquitetura</h3>
<h3>
<img src="images/image1.jpg" width="" alt="alt_text" title="image_tooltip">
</h3>
<h3>Descrição dos Componentes</h3>
<ul>
<li><strong>Web Scrapers</strong>: Scripts Python que mapeiam e coletam dados da
App Store e Google Store.
<li><strong>API Consumers</strong>: Scripts Python que consomem dados de APIs.
<li><strong>Data Orchestration: </strong>Parte que orquestra os scripts e define
horários de execução.
<li><strong>Data Processors</strong>: Scripts Python que processam, limpam e
padronizam os dados coletados.
<li><strong>Google</strong> <strong>Sheets</strong> <strong>Updater</strong>:
Scripts Python que atualizam as planilhas do Google com os dados processados.
<li><strong>Dashboards</strong>: Dashboards interativos desenvolvidos em Looker
Studio.
<li><strong>Apache Airflow</strong>: Ferramenta de orquestração que automatiza a
execução de todas as tarefas.
</li>
</ul>
<h2>Configuração do Ambiente</h2>
<h3>Ferramentas e Tecnologias</h3>
<ul>
<li>Python 3.11.7
<li>Apache Airflow 2.15
<li>Docker Compose 3
<li>GSpread 3.6.0
<li>OAuth2 Client 2.32.0
<li>Selenium 4.22.0
<li>Twisted 22.10.0
<li>Scrapy 2.11.2
<li>Web Driver Manager 4.0.1
<li>Google Sheets API
<li>Google Drive API
<li>Looker Studio
</li>
</ul>
<h3>Instruções de Configuração</h3>
<ol>
<li>Clonar repositório:
<ol>
<li>git clone <a href="https://github.com/">https://github.com/</a>(não tem
ainda)
<li>cd airflow
</li>
</ol>
<li>Instalar as dependências:
<ol>
<li>pip install -r requirements.txt
</li>
</ol>
<li>Configurar Docker:
<ol>
<li>docker compose build
<li>docker compose up
</li>
</ol>
</li>
</ol>
<h3>Dependências</h3>
<ul>
<li>Listadas no arquivo<strong> <em>requirements.txt</em></strong>.
<li>Listadas no arquivo <em>dockerfile</em>
<li>Necessário um projeto no Google Cloud.
<li>Necessário arquivo <em>credentials.json</em> com autorização necessária para
acessar a conta do Google.
</li>
</ul>
<h2>Desenvolvimento</h2>
<h3>Estrutura de pastas</h3>
<p>
airflow/
</p>
<p>
├── dags/
</p>
<p>
│   └── automation_scraping.py
</p>
<p>
│   └── etl_data_batch.py
</p>
<p>
├── data/
</p>
<p>
│   ├── api_itunes
</p>
<p>
│   │      └── ids.json
</p>
<p>
│   │      └── api_consumer_itunes.py
</p>
<p>
│   └── webscraping
</p>
<p>
│           ├── functions/
</p>
<p>
│            │         └── web_driver.py
</p>
<p>
│            │         └── format_date.py
</p>
<p>
│            │         └── url_google.py
</p>
<p>
│            │         └── url_apple.py
</p>
<p>
│           ├── spiders/
</p>
<p>
│            │         └── apple_star.py
</p>
<p>
│            │         └── google_star.py
</p>
<p>
│            │         └── google_rating.py
</p>
<p>
│           └── settings.py
</p>
<p>
├── logs/
</p>
<p>
│   └── credentials.json
</p>
<p>
├── requirements.txt
</p>
<p>
├── .env
</p>
<p>
├── dockerfile
</p>
<p>
└── docker-compose.yaml
</p>
<h3>Principais Scripts e Arquivos</h3>
<ul>
<li><strong>docker-compose.yaml</strong>: Arquivo de configuração do Docker com
o Apache Airflow.
<li><strong>dockerfile</strong>: Define a imagem do Docker.
<li><strong>requirements.txt</strong>: Lista todas as dependências necessárias
para o projeto.
<li><strong>settings.py</strong>: Arquivo de configuração do web scraping.
<li><strong>apple_star.py</strong>: Script que realiza o web scraping na loja da
Apple.
<li><strong>google_star.py</strong>: Script que realiza o web scraping na loja
da Google.
<li><strong>google_rating.py</strong>: Script que realiza o web scraping na loja
da Google e pega dados de novos comentários, usuários e notas.
<li><strong>api_consumer_itunes.py</strong>: Script que consome API do iTunes e
retorna dados de novos comentários, usuários e notas.
<li><strong>web_driver.py</strong>: Define as propriedades do web driver
manager, principal arquivo de configuração para o scraping.
<li><strong>format_date.py</strong>: Formata todos os horários que os scrapers
extraem dos sites.
<li><strong>url_google.py</strong>: Lista com todos os URLs dos aplicativos da
Google.
<li><strong>url_apple.py</strong>: Lista com todos os URLs dos aplicativos da
Apple.
<li><strong>automation_scraping.py</strong>: DAG Airflow que faz a orquestração
dos scripts web scraping e API de forma automática e agendada.
<li><strong>etl_data.py</strong>: DAG Airflow que lê os arquivos gerados,
padroniza e lida com dados faltantes, e depois insere os dados na planilha
Google responsável.
</li>
</ul>
<h3>Fluxo de Dados</h3>
<ol>
<li>Apache Airflow orquestra os workflows e gerencia os horários de execução.
<li>Web Scrapers coletam dados dos sites Apple e Google.
<li>API Consumers obtém dados da API do iTunes.
<li>Data Processors processam e limpam os dados coletados.
<li>Google Sheets API insere os dados em planilhas do Google.
<li>Dashboards no Looker Studio consomem os dados das planilhas do Google.
</li>
</ol>
<h2>Orquestração de Tarefas (Apache Airflow)</h2>
<h3>Diagrama de DAGs (Directed Acyclic Graphs)</h3>
<h4>automation_scraping.py</h4>
<p>
<img src="images/image2.png" width="" alt="alt_text" title="image_tooltip">
</p>
<h4>etl_data_batch.py
<img src="images/image3.png" width="" alt="alt_text" title="image_tooltip">
</h4>
<h3>Descrição das DAGS</h3>
<ul>
<li><strong>automation_scraping.py</strong>: Orquestra todas as funções web
scraping e API consumers automaticamente.
<li><strong>etl_data_batch</strong>.<strong>py</strong>: Dag que aplica
transformações e padroniza os dados coletados nas etapas anteriores e insere os
dados nas planilhas responsáveis.
</li>
</ul>
<h3>Descrição das Tasks</h3>
<ul>
<li><strong>check_api</strong>: Task que realiza uma requisição GET para
verificar se está disponível.
<li><strong>task_apple_comments</strong>: Task que chama a função que realiza a
extração dos comentários dos aplicativos Apple.
<li><strong>task_google_rating</strong>: Task que chama a função que realiza a
extração dos comentários dos aplicativos Google.
<li><strong>task_google_star</strong>: Task que chama a função que realiza a
extração das notas dos aplicativos Google.
<li><strong>task_apple_star</strong>: Task que chama a função que realiza a
extração das notas dos aplicativos Apple.
<li><strong>task_apple_comments_etl</strong>: Task que chama a função que
realiza a leitura dos arquivos de comentários Apple necessários para
padronização e insere na planilha.
<li><strong>task_google_comments_etl</strong>: Task que chama a função que
realiza a leitura dos arquivos necessários de comentários Google para
padronização e insere na planilha.
<li><strong>task_google_star_etl</strong>: Task que chama a função que realiza a
leitura dos arquivos necessários de notas Google para padronização e insere na
planilha.
<li><strong>task_apple_star_etl</strong>: Task que chama a função que realiza a
leitura dos arquivos necessários de notas Apple para padronização e insere na
planilha.
<li><strong>send_email_on_start</strong>: Task que envia um email avisando que
iniciou o DAG.
</li>
</ul>
<h3>Descrição das Funções</h3>
<ul>
<li><strong>fetch_API_itunes</strong>: Função que executa o script responsável
por fazer as requisições necessárias dos aplicativos Apple, retornando os
comentários.
<li><strong>fetch_webscraping_google_rating</strong>: Função que executa o
script web scraping de comentários de aplicativos Google.
<li><strong>fetch_webscraping_google_star</strong>: Função que executa o script
web scraping de notas de aplicativos Google.
<li><strong>fetch_webscraping_apple_star</strong>: Função que executa o script
web scraping de notas de aplicativos Apple.
<li><strong>append_to_google_sheets</strong>: Função que recebe parâmetros como
o caminho do arquivo tratado, a planilha que irá receber os dados e a sheet
name, e realiza o “append” dos dados.
</li>
</ul>
<h3>Configurações de Execução</h3>
<h4>	Agendamentos</h4>
<ul>
<li><strong>automation_scraping.py</strong>: Executado semanalmente segunda às
10:00.
<li><strong>etl_data.py</strong>: Executado semanalmente segunda às 11:30
</li>
</ul>
<h2>Automação de Tarefas</h2>
<h3>Web Scraping</h3>
<ul>
<li>Sites alvo: App Store e Google Store dos Aplicativos das Administradoras.
<li>Dados coletados: Comentários de usuários, notas dos aplicativos, downloads,
avaliações totais.
<li>Frequência de coleta: Semanalmente.
</li>
</ul>
<h3>API</h3>
<ul>
<li>Endpoints: <em>https://itunes.apple.com/rss/customerreviews/</em>
<li>Parâmetros:
<ul>
<li>page: Página que será exibida.
<li>id: Id do aplicativo na loja da Apple.
<li>sortby: Parâmetro que ordena o resultado.
<li>cc: País do aplicativo
</li>
</ul>
<li>Exemplos de requisições:
<ul>
<li>response =
<em>requests.get(http://itunes.apple.com/rss/customerreviews/page=1/id=959595889/sortby=mostrecent/json?cc=br)</em>
</li>
</ul>
</li>
</ul>
<h2>Desenvolvimento de Dashboards</h2>
<h3>Ferramentas Utilizadas</h3>
<ul>
<li>Looker Studio
<li>Planilhas Google Sheets.
</li>
</ul>
<h3>Principais Métricas e KPIs</h3>
<ul>
<li>Nota média
<li>Comentários
<li>Avaliações totais
<li>Crescimento downloads
<li>Crescimento avaliações
<li>Variação de crescimento
<li>Variação de notas
<li>Comparação de notas ao longo do tempo
</li>
</ul>
<h3>Design e Layout</h3>
<ul>
<li>Layout com gráficos de barras e linhas para visualização das métricas.
<li>Gráficos de pizza para entender a distribuição por plataforma (apple e
google).
<li>Filtros interativos para segmentação dos dados.
<li>Scorecards com KPIs importantes.
</li>
</ul>
<h3>Links para Dashboards e Planilhas</h3>
<ul>
<li>Dashboard Looker Studio: Link para o dashboard
<li>Planilhas do Google: Link para a planilha
</li>
</ul>
<h2>Manutenção e Atualizações</h2>
<h3>Plano de Manutenção</h3>
<ul>
<li>Revisão semanal dos scripts de scraping e API consumers para garantir a
coleta dos dados.
<li>Atualização e revisão semanal dos dados das planilhas Google.
<li>Acompanhamento das informações do dashboard.
</li>
</ul>
<h3>Histórico de Atualizações</h3>
<ul>
<li>12/06/2024: Início do projeto.
<li>17/06/2024: Primeira versão dos scripts de web scraping.
<li>24/06/2024: Primeira versão do script que consome API.
<li>27/06/2024: Desenvolvimento do dashboard no Looker Studio.
<li>04/07/2024: Integração dos scripts com Apache Airflow.
<li>10/07/2024: Integração com API Google Sheets.
<li>11/07/2024: Testes de performance e dados.
<li>15/07/2024: Primeiro teste automatizado.
</li>
</ul>
<h2>Referências</h2>
<h3>Links úteis</h3>
<ul>
<li><a
href="https://airflow.apache.org/docs/apache-airflow/stable/index.html">Documentação
do Apache Airflow</a>
<li><a href="https://docs.scrapy.org/en/latest/">Documentação do Scrapy</a>
<li><a href="https://www.selenium.dev/pt-br/documentation/">Documentação do
Selenium</a>
<li><a
href="https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html">Documentação
da API iTunes</a>
<li><a
href="https://support.google.com/looker-studio/?hl=en#topic=6267740">Documentação
do Looker Studio</a>
<li><a href="https://docs.python.org/3.11/">Documentação do Python</a>
<li><a
href="https://developers.google.com/sheets/api/reference/rest?hl=pt-br">Documentação
Google Sheets API</a>
<li><a href="https://pypi.org/project/webdriver-manager/">Documentação Web
Driver Manager</a>
</li>
</ul>
<h3>Referências</h3>
<ul>
<li><a
href="https://www.amazon.com.br/Data-Science-para-neg%C3%B3cios-Fawcett/dp/8576089726/ref=asc_df_8576089726/?tag=googleshopp00-20&linkCode=df0&hvadid=379708192683&hvpos=&hvnetw=g&hvrand=4759448562615842793&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197317&hvtargid=pla-398225631558&psc=1&mcid=e728759e9a023c558c8778e270cb325d">Davenport,
T. H., & Harris, J. G. (2017). Data Science para Negócios: Como usar a análise
de dados para ganhar uma vantagem competitiva. Alta Books.</a>
<li><a
href="https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04">Brian
Hogan. (2021, Setembro 29). How To Install and Use Docker on Ubuntu 20.04</a>
<li><a
href="https://www.youtube.com/watch?v=8dTpNajxaH0&ab_channel=AlexTheAnalyst">Alex.
(2023, Julho 11). Scraping Data from a Real Website | Web Scraping in Python</a>
<li><a href="https://hub.docker.com/r/apache/airflow">Docker Hub. (2024). Apache
Airflow Docker Image</a>
<li><a
href="https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html">Apache
Airflow. (2024). Running Airflow in Docker</a>
<li><a
href="https://dev.to/franciscojdsjr/guia-completo-para-usar-o-virtual-environment-venv-no-python-57bo">Franscisco
Júnior. (2023, Outubro 22). Guia Completo para Usar o Virtual Environment (venv)
no Python</a>
<li><a
href="https://www.lucidchart.com/blog/pt/como-fazer-diagramas-de-arquitetura-de-sistema">Lucid
Chart. (2023). Como desenhar cinco tipos de diagrama de arquitetura</a>
<li><a
href="https://medium.com/aimonks/130-data-science-terms-every-data-scientist-should-know-7199a22fc809">Anjolaoluwa
Ajayi. (2024, Janeiro 5). 130+ Data Science Terms Every Data Scientist Should
Know in 2024</a>
<li><a
href="https://developers.google.com/sheets/api/quickstart/python?hl=pt_BR">Google.
(2024). Guia de início rápido do Python</a>
<li><a
href="https://developers.google.com/sheets/api/reference/rest?hl=pt_BR">Google.
(2024). Google Sheets API</a>
<li><a
href="https://airflow.apache.org/docs/apache-airflow/stable/howto/email-config.html">Apache
Airflow. (2024) .How to send email in Apache Airflow</a>

