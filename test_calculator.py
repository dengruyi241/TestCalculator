import sys

import pytest
import yaml

sys.path.append("./CalculatorCode")
print(sys.path)
from CalculatorCode import Calculator

class TestCalculator:
    @classmethod
    def setup_class(cls):
        print("测试执行开始")
        cls.cal = Calculator.CalculatorMath()

    @classmethod
    def teardown_class(cls):
        print("测试执行结束")

    def setup_method(self):
        print("计算开始")

    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize(["a","b","result"],[(1,1,2),(1000,1000,2000),("c",2,2)])
    def test_add(self,a,b,result):
        assert self.cal.add(a,b) == result

    @pytest.mark.parametrize(["a","b","result"], yaml.safe_load(open("calc.yml", encoding="utf-8")))
    def test_multiply(self,a,b,result):
        assert self.cal.multiply(a,b) == result

    @pytest.mark.parametrize(["a","b","result"],[(1,1,1),(1000,1000,1),(1,0, "除数不能为0")])
    def test_div(self,a,b,result):
        assert self.cal.div(a,b) == result
