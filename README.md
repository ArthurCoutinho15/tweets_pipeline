<h1>Pipeline de extração de api tweets</h1>
    <h2>Utilização Apache Airflow (Ambiente Linux Ubuntu WSL)</h2>
        <ul>
            <li> Utilizando a extensão remote explorer do vscode se conecte ao Ubuntu</li>
        </ul>
        <ul>
            <li>Baixe o python 3.9 <code>sudo apt install python3.9</code></li>
        </ul>
        <ul>
            <li>Instalar o módulo de ambiente virtual python 3.9 <code>sudo apt install python3.9-venv</code></li>
        </ul>
        <ul>
            <li>Criar ambiente virtual <code>python3.9 -m venv venv</code></li>
        </ul>
        <ul>
            <li>Entrar no ambiente virtual <code>source venv/bin/activate<</code></li>
        </ul>
        <ul>
            <li>Instalar biblioteca airflow com constraint <code>pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"</code></li>
        </ul>
    <h2>Para executar o código siga o passo a passo</h2>
        <ul> 
            <li> Entre no ambiente virtual <code>source venv/bin/activate</code> </li>
            <li> Execute toda vez que utilizar o airflow <code> export AIRFLOW_HOME=~/pipeline_tweets/airflow_pipeline </code></li> 
            <li> Para rodar o airflow web server Execute <code>airflow standalone</code></li> 
            <li> Execute na pasta do hook <code>cd airflow_pipeline -> cd hook -> python3 twitter_hook.py</code></li>
            <li> Para verificar as conexões existentes <code>airflow connections list</code> </li>  
        </ul>
<h1>Utilização do Apache Spark</h1>
    <ul>
        <h2>Instale o java 8 no wsl <code>sudo apt-get install openjdk-8-jdk-headless -qq</code></h2>
        <li>Para instalar o spark dentro do ambiente virtual faça a instalação <code>!pip install pyspark==3.3.1</code></li>
        <li>Para instalar o spark submit <code>wget https://archive.apache.org/dist/spark/spark-3.1.3/spark-3.1.3-bin-hadoop3.2.tgz</code></li>
        <li>Extrair arquivo gerado após download do Spark submit <code>tar -xvzf spark-3.1.3-bin-hadoop3.2.tgz</code></li>
        <li>Para executar o script spark é necessário entrar na pasta do arquivo extraido <code>cd spark-3.1.3-bin-hadoop3.2/</code> </li>
        <li>Após isso devemos passar o caminho do script para o executável spark-submit <code>./bin/spark-submit /home/arthur/pipeline_tweets/src/spark/transformation.py </code></li>
        <li>Na mesma linha passar os parâmentros do código (--src, --dest, --process_date) <code>--src /home/arthur/pipeline_tweets/datalake/twitter_datascience --dest /home/arthur/pipeline_tweets/src/spark --process_date 2025-08-15</code></li>
    </ul>

