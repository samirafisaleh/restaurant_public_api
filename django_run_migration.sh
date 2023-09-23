
if [ $# -eq 0 ];
then
    echo "FATAL: No environment arguments supplied."
    echo "INFO: Exiting ...."
    exit 1
fi

if [ "$1" != "dev" -a "$1" != "test" -a "$1" != "stage" -a "$1" != "prod" ]
then
    echo "FATAL: Invalid environment: Choices: dev, test, stage, prod"
    echo "INFO: Exiting ...."
    exit 1
fi

echo "Environment: $1"

cd source/project/
python manage.py makemigrations --settings=settings.settings_$1
python manage.py migrate --settings=settings.settings_$1