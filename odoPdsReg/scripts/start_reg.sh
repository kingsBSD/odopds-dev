sed -i "s/pds.linkedpersonaldata.org/$HOSTADDR:8002/g" /registryEnv/openPDS-RegistryServer/registryServer/settings.py
cd /registryEnv
source ./bin/activate
cd openPDS-RegistryServer/registryServer
mkdir -p /var/www/trustframework/registryEnv/OMS-RegistryServer
#cp /test.db /var/www/trustframework/registryEnv/OMS-RegistryServer
python /init_reg.py
python manage.py runserver 0.0.0.0:8000



