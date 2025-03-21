# Rest Api Drill Down Field Names

**Technical Name:** RestApiDrillDownFieldNames

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter is responsible for defining field names used in generating flat data structures from nested JSON objects within the Pathlock Cloud GRC platform. It is primarily utilized in processes where complex JSON data needs to be simplified for analysis or reporting.

**Business Impact:**

Configuring this parameter can significantly affect how data is extracted and presented in reports, impacting decision-making processes. It enables better insights into GRC-related data by flattening complex, nested JSON structures for more straightforward analysis and reporting.

**Technical Impact when configured:**

Correct configuration ensures that the JSON data extracted from various sources is flattened according to the specified field names. This flattening process facilitates easier data analysis by converting complex nested structures into a simple tabular format, making it more accessible for reporting tools and end-users.

**Examples Scenario:**

A compliance officer needs to generate a report on user roles and permissions extracted from a JSON data source. By setting the RestApiDrillDownFieldNames, they can define which fields should be extracted and how the nested data should be structured in the final report, making it easier to identify potential compliance issues.

**Related Settings:**

- `GetRolesByBusinessRoleTakeDataFromRequest`

**Best Practices:** 

- **Configure when:** You have complex, nested JSON data sources that need to be reported in a simplified, flat format. It's crucial for scenarios requiring clear and concise data presentation for compliance checks, auditing, or any form of risk analysis.
  
- **Avoid when:** The data structure is already simple or when specific nested details are necessary for the context of the report. Over-flattening can sometimes lead to loss of meaningful hierarchy or context in the data.