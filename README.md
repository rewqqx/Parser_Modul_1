# Парсер

## Name
Парсер для обработки html страниц, .pdf, .doc, .docx, .djvu

## Installation
### Для обработки html, .pdf, .doc, .docx необходимы следующие библиотеки:

1. [Aspose.words](https://products.aspose.com/words/python-net/)
2. [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

### Для обработки .djvu необходим инструмент [DjVuLibre](https://djvu.sourceforge.net/)
Необходимо установить [DjVuLibre](https://djvu.sourceforge.net/) и в PATH прописать путь до djvused.

## Console

```
> python parser.py
Path to file input: path/to/file.ext
Path to file output: path/to/file.json
```

## Tests

### Requirements
1. hypothesis

### How to Run
1. Убедиться в наличии библиотеки
2. Запустить файл test_hypothesis.py
3. Ожидать результатов

### Test Cases
Суммарно 15 кейсов  
Среди которых пребор значение с помощью hypothesis,  
Проверка заранее заданных кейсов
Проверка отдельных функций

### Test cases short-list

1. Utils (Staff) 
> - clean_ad method
> - clean_text method

2. Pdf
> - test files existence (2)
> - empty content 
> - correct processing

3. Doc
> - files openings
> - doc with blank content
> - doc parsing

4. Djvu
> - sample existance
> - txt parsing result comparison

5. Html
> - given file detecting
> - empty page with empty str comparison

### Bug fix history
0. 7 march (0 / 3 success)  
Тесты вне системы контроля версий, проверка ограниченного функционала

1. 9 march (10 / 12 success)  
Первый полный проход по всем парсерам
Замечен баг, что соответствие файла не удается установить для проверки pdf файла

2. 10 march (12 / 12 success)  
Баг был пофикшен, проблема была в наличии абсолютной ссылке внутри функции

3. 11 march (15 / 15 success)  
Запуск всех тестов, все ошибки почищены. Остались мелкие проблемы: например, наличие абсолютных ссылок в вызовах из файла main

## Authors
Миннигалимов Рамиль <br>
Обухов Кирилл <br>
Сабалевский Сергей <br>



