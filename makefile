run: 
	python src/main.py

calibrate:
	python tools/read_raw_data.py

update:
	python -m pip install --upgrade pip
	pip install -r requirements.txt