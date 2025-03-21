# Custom Store Procedure For Employees Data

**Technical Name:** CustomStoreProcedureForEmployeesData

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `CustomStoreProcedureForEmployeesData` parameter allows for the configuration of a custom stored procedure dedicated to managing employees' data within the Pathlock Cloud GRC platform. This customization enables the organization to tailor data retrieval and processing to meet specific internal policies or requirements.

**Business Impact:**

Configuring a custom stored procedure for employees' data can significantly influence operational efficiency and data accuracy. It allows for the streamlined integration of employee data management processes with internal systems, potentially leading to better compliance with regulatory requirements and enhanced security measures.

**Technical Impact when configured:**

When this parameter is configured, the custom stored procedure will override default methods of employee data retrieval and processing. This can affect how data is queried, the performance of data access, and the granularity of information available for reporting and analysis purposes.

**Examples Scenario:**

- An organization needs to integrate Pathlock GRC's employee data management with its internal HR system, which requires specific data transformation not supported by Pathlock's default functionalities. The `CustomStoreProcedureForEmployeesData` parameter can be set to use a tailored procedure that aligns with these needs.
  
- To enhance audit trails and meet stringent compliance requirements, a company modifies the stored procedure to include detailed logging of all data accesses and changes, providing greater transparency and security.

**Related Settings:**

- `CustomFieldTechincalNameForUserBuildingData`: This setting might be relevant if the custom procedure needs to interact with or modify the way buildings are associated with users.

**Best Practices:** 

- **Configure when:** you have specific requirements for employee data processing that cannot be met by the default functionality provided by Pathlock GRC. Implementing a custom procedure can ensure that your organization's unique needs are addressed more accurately and efficiently.
  
- **Avoid when:** there is no clear requirement for custom data processing. Custom configurations require maintenance and can complicate future platform upgrades or changes.