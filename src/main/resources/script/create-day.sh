#!/bin/bash

# Creates the Scala packages and templated classes for a given day's problem.
#
# TO RUN:
# ```
#create-day.sh <DAY> <CLASS_NAME>
# ```
#
# Where:
#  * **`<DAY>`** is the day to be created (for example `1` or `23`)
#  * **`<CLASS_NAME>`** is the name of the class (and corresponding test class) to be created (for example
#  `MinecartMadness`).

cd $(dirname "$0") || exit

PACKAGE="uk/co/hadoopathome/adventofcode20"
TEMPLATE_DIR="../templates"
PROJECT_ROOT="../../../.."

if [ $# -ne 2 ]; then
  echo "Day and puzzle name must be given as arguments."
  echo "USAGE EXAMPLE: ./create-day.sh 1 MinecraftMadness"
  exit 1
fi

printf -v formatted_day "%02d" "${1}"
day="day${formatted_day}"

class_name=${2}

echo "Creating files for ${day}"

destination_main="${PROJECT_ROOT}/src/main/scala/${PACKAGE}/${day}"
main_class_name="${class_name}.scala"

if [ -d "${destination_main}" ]; then
  echo "Folder for day ${day} already exists, exiting"
  exit 1
fi

echo "Creating dev class ${destination_main}/${main_class_name}"
mkdir "${destination_main}"
cp ${TEMPLATE_DIR}/MainClass.scala "${destination_main}"/"${main_class_name}"

destination_test="${PROJECT_ROOT}/src/test/scala/${PACKAGE}/${day}"
test_class_name="${class_name}Test.scala"
echo "Creating test class ${destination_test}/${test_class_name}"
mkdir "${destination_test}"
cp ${TEMPLATE_DIR}/MainClassTest.scala "${destination_test}"/"${test_class_name}"

destination_resources="${PROJECT_ROOT}/src/test/resources/${day}"
echo "Creating input file ${destination_resources}/input.txt"
mkdir "${destination_resources}"
touch "${destination_resources}"/input.txt

echo "Updating references inside classes"
sed -i -e "s/\${internal_day}/${day}/" -e "s/\${internal_class_name}/${class_name}/" "${destination_main}"/"${main_class_name}"
sed -i -e "s/\${internal_day}/${day}/" -e "s/\${internal_class_name}/${class_name}/" "${destination_test}"/"${test_class_name}"
