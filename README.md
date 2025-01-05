<h1>Pipeline de extração de api tweets</h1>
<h2>Para executar o código siga o passo a passo</h2>
<li> 
    <ul> Entre no ambiente virtual <code>source venv/bin/activate</code> </ul>
    <ul> Execute toda vez que utilizar o airflow <code> export AIRFLOW_HOME=~/pipeline_tweets/airflow_pipeline </code></ul> 
    <ul> Para rodar o airflow web server Execute <code>airflow standalone</code></ul> 
    <ul> Execute na pasta do hook <code>cd airflow_pipeline -> cd hook -> python3 twitter_hook.py</code></ul>
    <ul> Para verificar as conexões existentes <code>airflow connections list</code> </ul>  
</li>
<h1>Utilização do Apache Spark</h1>
<li>
    <h2>Instale o java 8 no wsl <code>sudo apt-get install openjdk-8-jdk-headless -qq</code></h2>
    <ul>Para instalar o spark dentro do ambiente virtual faça a instalação <code>!pip install pyspark==3.3.1</code></ul>
</li>

