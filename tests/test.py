import pytest
from app.calc import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1,1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1,1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1,0)

    def teardown(self):
        print("Выполнение метода Teardown")

import requests

status = 'avaitable'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
