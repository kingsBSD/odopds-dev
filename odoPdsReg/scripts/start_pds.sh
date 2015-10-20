cd /pdsEnv
source ./bin/activate
cd openPDS
python /init_pds.py
#cp -r /db /data
python manage.py runserver 0.0.0.0:8002