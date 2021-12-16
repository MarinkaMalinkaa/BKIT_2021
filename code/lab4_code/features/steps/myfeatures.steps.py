from behave import *
from tdd_test.TDD_test import *

@given("I have Mouse for 800 rubles and Keyboard for 1920 rubles")
def have_prices(context):
    context.a = TestPartCost()


@when("I put them into ControlDivices")
def ControlDivices_combine(context):
    context.a.test_part_cost_is_working()


@then("I expect ControlDivices  to cost 2720 rubles")
def check_result(context):
    pass