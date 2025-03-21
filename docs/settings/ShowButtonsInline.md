**Technical Name: ShowButtonsInline**

**Category: Reporting**

**Default Value:**

**Impact Level: Medium**

**Description:**

This parameter controls the layout of buttons within the Pathlock Cloud GRC platform's reporting interface, specifically dictating whether buttons related to activities linked to users are displayed in-line within reporting columns.

**Business Impact:**

Configuring this parameter affects the user interface's clarity and efficiency. For instance, displaying buttons inline can streamline user actions such as reviewing, approving, or escalating activities directly from within the report, thereby improving operational efficiency and audit response times.

**Technical Impact when configured:**

When activated, this feature modifies the appearance and functionality of report columns by including actionable buttons directly within the report view. This change facilitates quicker user actions and decisions based on the presented data, potentially influencing the speed and effectiveness of compliance and risk management processes.

**Examples Scenario:**

Consider a scenario where an auditor needs to review and approve a series of user activity/audit logs. With ShowButtonsInline enabled, the auditor can quickly access the necessary action buttons directly next to the relevant data within the report, reducing navigation and enhancing productivity.

**Related Settings:**

- `SAP_ErrorCodesToIgnore`

**Best Practices:** 

- **Configure when:** Streamlining of user actions within reports is needed to enhance decision-making speed and operational efficiency.
  
- **Avoid when:** Minimizing screen clutter is a priority, or if there is a preference for navigating to dedicated screens for each action.