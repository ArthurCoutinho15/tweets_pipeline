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
        <li> 
            <ul> Entre no ambiente virtual <code>source venv/bin/activate</code> </ul>
            <ul> Execute toda vez que utilizar o airflow <code> export AIRFLOW_HOME=~/pipeline_tweets/airflow_pipeline </code></ul> 
            <ul> Para rodar o airflow web server Execute <code>airflow standalone</code></ul> 
            <ul> Execute na pasta do hook <code>cd airflow_pipeline -> cd hook -> python3 twitter_hook.py</code></ul>
            <ul> Para verificar as conexões existentes <code>airflow connections list</code> </ul>  
        </li>
<h1>Utilização do Apache Spark</h1>
    <ul>
        <h2>Instale o java 8 no wsl <code>sudo apt-get install openjdk-8-jdk-headless -qq</code></h2>
        <li>Para instalar o spark dentro do ambiente virtual faça a instalação <code>!pip install pyspark==3.3.1</code></li>
    </ul>

