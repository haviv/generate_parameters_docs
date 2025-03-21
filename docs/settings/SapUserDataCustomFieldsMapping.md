# Sap User Data Custom Fields Mapping

**Technical Name:** SapUserDataCustomFieldsMapping

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SapUserDataCustomFieldsMapping` parameter is used to map custom fields between source and target within SAP user data. This facilitates the customization and extension of user profiles by aligning additional or external data fields (such as "CountryISO" converted to "Country") with SAP's standard user fields. 

**Business Impact:**

Implementing custom fields mapping allows businesses to enhance data integrity, improve user profile management, and enable a more comprehensive view of user information. This can be particularly significant for global organizations that require the adjustment of user data to meet local compliance regulations or business requirements.

**Technical Impact when configured:**

Once configured, the mapping ensures that external or additional source fields correctly match the target SAP user data fields, thus maintaining data consistency and relevancy. For example, converting "CountryISO" to "Country" standardizes data fields across different systems.

**Examples Scenario:**

- **Converting Country Codes:** A multinational corporation uses ISO country codes in their HR software but needs the full country name in their SAP system for reporting and compliance. Mapping "CountryISO" to "Country" solves this discrepancy.
  
- **Adding Custom Attributes:** A company requires additional user attributes such as "EmployeeDomain" for access control policies. Through custom field mapping, these attributes can be integrated into the SAP user profile from external systems.

**Related Settings:** 

- EmployeeDomainField

**Best Practices:** 

- **Configure when:** there is a need to integrate external user data with SAP user profiles, especially in cases of custom attributes or specific data format requirements.
  
- **Avoid when:** default SAP user fields suffice for the organization's data management and reporting needs, or when the mapping could lead to data integrity issues without proper validation.