#!/bin/bash
#runstuff

cd robot-framework/ContriboardTesting/
pybot RegTestUsers.txt
pybot Invalid_Login_Test.txt
pybot New_User_Test.txt
pybot Old\ User\ Test.txt
cd .. && cd ContriboardTestScenarios/
cd ScenarioTests/
pybot RegisterUsers.txt
pybot Scenario6.txt
cd ..
pybot Scenario1.rst
pybot Scenario2.rst
pybot Scenario3.rst
pybot Scenario4.rst
pybot Scenario5.rst