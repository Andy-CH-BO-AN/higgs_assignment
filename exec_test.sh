python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
pytest
allure generate ./allure-results/ -o ./allure-report/ --clean
deactivate