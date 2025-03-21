# Generic Sheet Import Name

**Technical Name:** GenericSheetImportName

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Generic Sheet Import Name parameter is used to define the name for importing external tables into the Pathlock Cloud GRC platform. This parameter ensures that only tables with matching names are considered during the import process, facilitating targeted data integration.

**Business Impact:**

Configuring the Generic Sheet Import Name correctly can significantly streamline data import processes, making it easier to integrate external data sources relevant to security, risk, and compliance management. It helps in maintaining the integrity and relevance of imported data, directly impacting decision-making processes and regulatory compliance.

**Technical Impact when configured:**

When the Generic Sheet Import Name is configured, the system will only import tables that match the defined name, thus preventing the accidental importation of irrelevant or unauthorized data. This selective importation aids in maintaining a clean and relevant dataset within the Pathlock Cloud GRC platform.

**Example Scenario:**

Consider a scenario where an organization needs to import risk assessment data from an external spreadsheet named "RiskAssessment2023". By setting the Generic Sheet Import Name to "RiskAssessment2023", the system will specifically target and import only the table with this name, ensuring a focused and relevant data integration.

**Related Settings:**

N/A

**Best Practices:** Configure when you need to import specific tables from external sources into the Pathlock Cloud GRC platform. Avoid configuration unless there is a clear requirement for importing named tables, to prevent unnecessary restrictions on the data import process.