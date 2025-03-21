# Show CSG

**Technical Name:** ShowCSG

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The ShowCSG parameter is utilized within the Pathlock GRC platform to determine the visibility and configuration of specific columns and data presentation in the system, particularly related to employee and system configurations. It impacts how certain information is displayed and managed within the platform, ensuring that users can customize their view to include essential details relevant to their governance, risk, and compliance (GRC) tasks.

**Business Impact:**

Adjusting the ShowCSG parameter allows organizations to tailor the GRC platform to better fit their internal audit, compliance, and risk management processes. By customizing which information is visible, organizations can streamline workflows, improve the efficiency of compliance checks, and enhance the overall user experience for employees managing GRC tasks.

**Technical Impact when configured:**

When configured, the ShowCSG parameter influences the generation and customization of data fields and columns in various reports and user interfaces. This can include filtering and specifying data related to audits, HR actions, and information types, thereby affecting both the granularity and breadth of information presented to the user.

**Examples Scenario:**

An administrator wishes to customize the visibility of certain audit actions and human resources (HR) information within the platform to simplify compliance checks. By configuring the ShowCSG parameter, they can specify which columns are visible in the user interface, focusing on the most relevant information and improving the efficiency of audit and compliance tasks.

**Related Settings:**

- AuditActionsDesc
- InfoTypeDesc
- DailyEmailFormatedFooter

**Best Practices:** configure when tailoring the platform's data presentation to specific GRC tasks and objectives; avoid when broader, unfiltered data visibility is required for comprehensive risk assessment and compliance checks.