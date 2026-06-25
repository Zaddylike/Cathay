安裝package
1. pip install -r requirements.txt 
2. npm install allure-commandline (如果要看報告要下載, 不然只能用內建的html report)


運行方法: 
1. python -m pytest ./tests/{{測試腳本}}.py::test_{{測試項目}}
2. python -m pytest ./tests/{{測試腳本}}.py
3. python -m pytest 

報告:
1. 產生在reports, 路徑設定在pytset.ini