 Pairs Finder

Pairs Finder is a Python script that helps you find pairs of integers in a list that sum up to a target number.

## Installation

You can run this script on your local machine by following these steps:

1. Clone this repository to your local machine using the following command:

git clone https://github.com/your-username/pairs-finder.git

2. Navigate to the project directory:
cd pairs-finder

3. Create a python virtual environment

4. Install the required dependencies:
pip install -r requirements.txt

5. Run the script:
python find_pairs.py

## Usage
1. When you run the script, it will prompt you to provide a list of integer numbers separated by commas. For example:
Welcome to the pairs finder. Please, provide a list of integer numbers separated by a comma: 1, 2, 3, 4, 5

2. If any non-integer values are provided, the script will ask you to try again until a valid list of integers is provided.

3. After successfully providing the list, the script will then prompt you to enter a target integer number. For example:
Please, now provide an integer number: 6

4. The script will then find pairs of numbers in the list that sum up to the target number and display the results:
Here are the pairs that sum 6: [(1, 5), (2, 4)]

## Testing
1. In order to run the tests, please use the command:
pytest

2. One of the test will execute 1000 times the find_pairs function, so it can take a little bit to finish.