# тестовое задание по тестированию

Задача: протестировать API http://bzteltestapi.pythonanywhere.com/ (<-- подробности и методы по этой же ссылке)

Сделано 10 тестов по управлению аккаунтом и 1 для управления контентом. 

Инструкция по развертыванию:
- перейти в консоль
- git clone https://github.com/gorelikspb/pytest_api.git
- рекомендовано создать виртуальное окружение: python3 -m venv /path/to/new/virtual/environment
- pip3 install -r requirements.txt
- **pytest test.py**
- ознакомьтесь с отчетом в консоли. 

Для создания отчета в формате JUnitXML (может быть использовано в Jenkins) - запуск производится в виде:
pytest --junitxml=report.xml test.py 
Подробнее: https://pytest.org/latest/usage.html, раздел 'Creating JUnitXML format files' 

