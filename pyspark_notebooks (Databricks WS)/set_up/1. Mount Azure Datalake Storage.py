# Databricks notebook source
client_id = dbutils.secrets.get(scope='covid19-scope', key='client-id')
tenant_id = dbutils.secrets.get(scope='covid19-scope', key='tenant-id')
secret_key = dbutils.secrets.get(scope='covid19-scope', key='secret-key')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": secret_key,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
for container_name in ["raw", "processed", "lookup"]:
    dbutils.fs.mount(
    source = f"abfss://{container_name}@covid19prjdls.dfs.core.windows.net/",
    mount_point = f"/mnt/covid19prjdls/{container_name}",
    extra_configs = configs)