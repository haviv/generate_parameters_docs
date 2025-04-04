**Technical Name:** CustomFieldDisplayNameForUserBuildingData

**Category:** Reporting

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:** Enables customization of display names for user-related data fields within the Pathlock Cloud GRC platform's reporting and data matrix functionalities.

**Business Impact:** Allows organizations to tailor the presentation of user data in reports and matrices to better align with internal terminology and reporting standards. This customization enhances the readability and relevance of compliance reports, security audits, and risk assessments.

**Technical Impact when configured:** Configuring this parameter to match an organization's internal naming conventions can significantly improve the clarity of data presentation for end-users. It impacts how user attributes such as creation date, department, and various other user-specific details are labeled in reports generated by the system.

**Examples Scenario:** 

An organization prefers to use the term "Employee ID" instead of the default "SAP UserName" in their user reports. By configuring `CustomFieldDisplayNameForUserBuildingData` to map "SAP UserName" to "Employee ID", all reports and matrices generated will reflect this preference, making the reports more intuitive for their HR department.

**Related Settings:** 

- `ShowCreatedOnColumn`
- `ShowDepartmentColumn`
- `ShowUserInvalidDateColumn`
- `ShowSapCompanyColumn`

**Best Practices:** 

- **Configure when**:
  - The default field names do not align with your organization's internal terminology or reporting requirements.
  - There's a need to enhance report readability and data presentation for specific audience groups within your organization.
  
- **Avoid when**:
  - Default field names are already clear and well-understood across the organization.
  - Customizations might create confusion due to lack of communication with end-users about the changes.