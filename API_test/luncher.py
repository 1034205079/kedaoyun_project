import pytest, os

test_result = "allure_result"
test_report = "allure_report"
pytest.main(["-vs", "../API_test",
             f"--alluredir={test_result}",
             "--clean-alluredir"])

"""制作可视化报告"""
os.system(f"allure generate {test_result} --clean -o {test_report}")
