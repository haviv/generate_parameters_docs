**Technical Name:** V2_Normal_Records_Columns

**Category:** Reporting

**Default Value:** N/A

**Impact Level:** Medium

**Description:** The V2_Normal_Records_Columns parameter specifies the selection of columns to be displayed in various reporting views within the Pathlock Cloud GRC platform. It enables customization of the information presented, focusing on aspects relevant to the user’s needs.

**Business Impact:** Proper configuration of this parameter ensures that decision-makers have access to critical and relevant information, such as employee changes, login data, local and system times, and messages on system changes. This customization supports effective oversight and management, enhancing the organization's ability to respond to compliance and security risks.

**Technical Impact when configured:**
- Enhances the readability and relevance of reports
- Enables focused analysis on specific data points such as department columns, user groups, and SAP company columns
- Supports targeted audit and compliance efforts by highlighting critical information

**Examples Scenario:** An organization needs to closely monitor employee roles and access rights changes within its ERP system to comply with internal controls and external regulations. By configuring the V2_Normal_Records_Columns to include "ShowEmployeeChangeData" and "ShowRoleTypeColumn", the organization can efficiently generate reports focused on these aspects, facilitating quick reviews and actions when discrepancies are detected.

**Related Settings:** 
- ShowDepartmentColumn
- ShowEmployeeChangeData
- ShowLatLogOn
- ShowLocalTime
- ShowMessageOnSystemChange
- ShowRoleTypeColumn
- ShowSapCompanyColumn
- ShowSystemTime
- ShowUserGroup

**Best Practices:** 
- Configure when: Detailed and specific reporting is required for audit, compliance, or management needs.
- Avoid when: General reporting suffices, or the inclusion of numerous columns could overwhelm the users or dilute the focus of the report.