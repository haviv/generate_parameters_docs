# Additional Columns In User Search

**Technical Name:** AdditionalColumnsInUserSearch

**Category:** User Management

**Default Value:** NULL

**Impact Level:** Medium

**Description:** 

Allows customization of the columns displayed in user search results within the Pathlock Cloud GRC platform. This parameter enables administrators to include additional, relevant user information beyond the default settings to tailor the results to specific organizational needs.

**Business Impact:**

Enhancing user search functionality with additional columns improves operational efficiency by allowing administrators and auditors to quickly find and access detailed user information. This capability is crucial for maintaining security, supporting compliance reporting, and facilitating thorough audits.

**Technical Impact when configured:**

Configuring this parameter allows the display of customized data fields in user search results. This flexibility can help in pinpointing specific user attributes or associations that are not readily available in the default view, such as department, role, or last login date, thereby streamlining user management and review processes.

**Examples Scenario:**

- **Audit Preparation:** An auditor wishes to review users with access to sensitive financial information. By configuring additional columns to display specific permissions or roles, auditors can efficiently assess user access and ensure compliance with financial regulations.
  
- **Security Review:** A security administrator is performing a quarterly review of user access rights. Including additional columns like 'Last Password Change' or 'Account Status' can help quickly identify potential security risks or non-compliant accounts.

**Related Settings:** 

- EmployeeAutoCompleteDataTemplate

**Best Practices:** 

- **Configure when:** Detailed user information is necessary for audits, security reviews, or compliance checks. Customizing user search results can significantly reduce the time required to locate and analyze user data.
  
- **Avoid when:** Default user information satisfies organizational needs. Over-customization can lead to information overload and reduce administrative efficiency.