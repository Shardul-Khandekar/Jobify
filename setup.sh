pip install -r requirements.txt
flag=0
server_name=$(grep "server_name" db.properties|cut -d'=' -f2)
if [ -z $server_name ]
then
  echo "db.properties is not setup properly"
  flag=1
fi

user_name=$(grep "user_name" db.properties|cut -d'=' -f2)
if [ -z $user_name ]
then
  echo "db.properties is not setup properly"
  flag=1
fi

password=$(grep "password" db.properties|cut -d'=' -f2)
if [ -z $password ]
then
  echo "db.properties is not setup properly"
  flag=1
fi

db_name=$(grep "db_name" db.properties|cut -d'=' -f2)
if [ -z $db_name ]
then
  echo "db.properties is not setup properly"
  flag=1
fi

if [ $flag -eq 1 ]
then
  echo "exiting"
  exit
fi
params="{\"server_name\" : \"${server_name}\", \"user_name\":\"${user_name}\", \"password\": \"${password}\", \"db_name\": \"${db_name}\", \"linked_in_pwd\":\"SRIJASGMAILPWD\"}"
echo $params > code/Scraper/parameters.json
echo $params > code/Web_app/parameters.json
echo $params > parameters.json
