import yaml
import os
from pathlib import Path

API_SPEC_PATH = Path("specs/sample-api.yaml")

def validate_schema_definitions(api_spec):
    errors = []

    for path, methods in api_spec.get("paths", {}).items():
        for method, operation in methods.items():
            # Validate 200 response schema
            try:
                schema = operation["responses"]["200"]["content"]["application/json"]["schema"]
                if not schema:
                    errors.append(f"{method.upper()} {path} -> Missing schema in 200 response")
            except KeyError:
                errors.append(f"{method.upper()} {path} -> No 200 response schema found")

            # Optionally validate request body schema
            if "requestBody" in operation:
                try:
                    schema = operation["requestBody"]["content"]["application/json"]["schema"]
                    if not schema:
                        errors.append(f"{method.upper()} {path} -> Missing schema in request body")
                except KeyError:
                    errors.append(f"{method.upper()} {path} -> No request body schema found")

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
