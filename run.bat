cd core
python setup.py install
cd ..

cd wiki-provider
python setup.py install
cd ..

cd xml-provider
python setup.py install


cd ..\tim02_sokic
python manage.py runserver