import yaml
import os
from pathlib import Path

API_SPEC_PATH = Path("specs/sample-api.yaml")

def validate_schema_definitions(api_spec):
    errors = []

    for path, methods in api_spec.get("paths", {}).items():
        for method, operation in methods.items():
            method_upper = method.upper()

            # Validate 200 response schema (or 201 for POST)
            # You can customize this as needed
            # Validate expected response status based on HTTP method
         if method_upper == "POST":
            response_statuses = ["201"]
         elif method_upper in ["GET", "PUT", "DELETE"]:
            response_statuses = ["200"]
         else:
            response_statuses = ["200"]  # fallback


            for status_code in response_statuses:
                try:
                    schema = operation["responses"][status_code]["content"]["application/json"]["schema"]
                    if not schema:
                        errors.append(f"{method_upper} {path} -> Missing schema in {status_code} response")
                except KeyError:
                    errors.append(f"{method_upper} {path} -> No {status_code} response schema found")

            # Validate requestBody schema only for POST and PUT
            if method_upper in ["POST", "PUT"]:
                if "requestBody" not in operation:
                    errors.append(f"{method_upper} {path} -> Missing requestBody")
                else:
                    try:
                        schema = operation["requestBody"]["content"]["application/json"]["schema"]
                        if not schema:
                            errors.append(f"{method_upper} {path} -> Missing schema in request body")
                    except KeyError:
                        errors.append(f"{method_upper} {path} -> No request body schema found")

    return errors

def main():
    with open(API_SPEC_PATH, 'r') as f:
        spec = yaml.safe_load(f)

    errors = validate_schema_definitions(spec)

    if errors:
        print("Schema Validation Errors Found:")
        for e in errors:
            print(" ❌", e)
        exit(1)
    else:
        print("✅ All endpoints have valid schema definitions")

if __name__ == "__main__":
    main()
