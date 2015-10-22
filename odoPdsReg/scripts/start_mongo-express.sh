until mongo --eval 'db.stats()'; do
    echo "Waiting for MongoDB"
done
#http://docs.mongodb.org/v2.4/tutorial/add-user-administrator/
mongo admin --eval 'db.addUser( { user: "user", pwd: "pass", roles: [ "userAdminAnyDatabase" ] } )'
cd /mongo-express
node app