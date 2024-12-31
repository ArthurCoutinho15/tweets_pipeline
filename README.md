<h1>Pipeline de extração de api tweets</h1>
<h2>Para executar o código siga o passo a passo</h2>
<li> 
    <ul> Entre no ambiente virtual <code>source venv/bin/activate</code> </ul> 
    <ul> Execute  <code> export AIRFLOW_HOME=~/pipeline_tweets/airflow_pipeline </code> em um terminal e no mesmo execute <code>airflow standalone</code></ul> 
    <ul> Execute <code> export AIRFLOW_HOME=~/pipeline_tweets/airflow_pipeline </code> em outro terminal e no mesmo entre na pasta do hook <code>cd airflow_pipeline -> cd hook -> python3 twitter_hook.py</code></ul>
    <ul> Para verificar as conexões existentes <code>airflow connections list</code> </ul>  
</li>

