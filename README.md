## database 설치

```sh
# 우분투
sudo apt-get install postgresql

# 맥
brew install postgresql
```


## pip, venv 설치

```sh
# 우분투
sudo apt-get install python-pip 

# 리눅스, 맥
easy_install pip  

# 우분투
sudo apt install virtualenv 

# 맥
pip3 install virtualenv virtualenvwrapper 

```


## 소스 클론 및 가상환경 설정

```sh
git clone 

cd backend

python -m venv undefined_env

source undefined_env/bin/activate

pip install -r requirements.txt

cd undefined

python manage.py makemigrations

python manage.py migrate

```

## 실행
```sh
python manage.py runserver
```