Feature: Test
  Scenario:  Test function
    Given I have Mouse for 800 rubles and Keyboard for 1920 rubles
    When I put them into ControlDivices
    Then I expect ControlDivices  to cost 2720 rubles
