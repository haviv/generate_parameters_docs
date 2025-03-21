**Save Sap Log Into DB**

**Technical Name:** SaveSapLogIntoDB

**Category:** Configuration

**Default Value:** False

**Impact Level:** High

**Description:**

The SaveSapLogIntoDB parameter enables the Pathlock Cloud GRC platform to save SAP log data directly into the database. This configuration is crucial for maintaining a detailed audit trail of SAP system activities.

**Business Impact:**

Enabling this feature ensures that all SAP transaction logs are securely stored and accessible for compliance auditing, investigations, and analysis of user activities. This aids in identifying potential security threats, compliance issues, and operational inefficiencies.

**Technical Impact when configured:**

When enabled, SAP log data is continuously captured and stored in the database, significantly increasing the availability of log information for auditing and monitoring purposes. It may increase database size and require effective management of database resources.

**Examples Scenario:**

To comply with internal auditing requirements and external regulations, an organization decides to enable SaveSapLogIntoDB. By doing so, they are able to provide auditors with comprehensive logs of all SAP transactions, enhancing transparency and accountability.

**Related Settings:**

- ShowEmployeeChangeData

**Best Practices:** configure when comprehensive auditing and monitoring of SAP transactions are required; avoid when database resource limitations are a concern.