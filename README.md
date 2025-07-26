Prebuild Shield - API Validator
Overview
Prebuild Shield is a tool that validates OpenAPI specifications for RESTful APIs. It checks the API schema to make sure everything is in order. This is helpful to catch errors early and make sure the API documentation is correct.

Features:
Validates response schemas for HTTP methods (GET, POST, etc.).

Checks for the presence of request bodies for POST and PUT methods.

Ensures the proper status codes (like 200, 201) are used in the responses.

Setup and Requirements
Before using the tool, make sure you have the following:

Python 3.x installed on your machine.

pip (Python package installer).

How to Use
1. Clone the Repository
First, download the project files by cloning the repository:

bash
Copy
Edit
git clone https://github.com/Steffi-cloud/prebuild-shield.git
2. Install Dependencies
Navigate to the project folder and install the required dependencies by running:

bash
Copy
Edit
cd prebuild-shield
pip install -r requirements.txt
3. Add Your OpenAPI Specification
Place your OpenAPI specification file (like sample-api.yaml) in the specs/ folder.

4. Run the Validator
To validate the API spec, run the following command:

bash
Copy
Edit
python validator.py
This will check your OpenAPI specification and print any issues or errors in the terminal.

GitHub Actions (CI/CD)
This project uses GitHub Actions for automated validation every time you push changes. The workflow automatically runs validation to ensure your OpenAPI spec is correct.

Workflow
Lint OpenAPI: Runs a basic check to ensure the API follows best practices.

Run Python Validation: Checks for missing request bodies and response schemas.

Troubleshooting
If you face any issues, here are some common fixes:

Indentation Errors: Make sure to use consistent indentation (preferably 4 spaces).

Missing Schemas: Check if you have all required schemas in your OpenAPI spec (like User, Product, etc.).

Contributions
Feel free to submit a pull request if you want to add more features or fix any bugs. We'd love your help!





