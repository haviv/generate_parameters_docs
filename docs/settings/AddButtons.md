# Add Buttons

**Technical Name:** AddButtons

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AddButtons` parameter plays a critical role within the Pathlock Cloud GRC platform, specifically within the reporting module. This parameter is designed to dynamically add button controls to reports, facilitating specific user interactions directly from report columns. This functionality enhances the interactive capability of reports by linking activities to user actions, making the reports not just informational but actionable.

**Business Impact:**

Implementing the `AddButtons` parameter within reports significantly elevates the operational efficiency by streamlining processes such as audit trails, activity monitoring, and compliance checks. Users can initiate workflows or perform actions directly from the report interface, reducing the time and effort required to navigate through the system for individual record processing.

**Technical Impact when configured:**

Upon configuration, `AddButtons` enriches report columns with buttons that are contextually linked to user or activity records. This can lead to more engaged user interaction with reports, a more intuitive UI/UX for end-users, and a reduction in the steps needed to manage or review specific records.

**Examples Scenario:**

Consider a GRC report designed to monitor user activities within critical systems. By configuring the `AddButtons` parameter, the report can include a "Details" button next to each activity record. Clicking this button would take an auditor directly to a detailed view of the activity without leaving the report, greatly enhancing the audit workflow's efficiency and effectiveness.

**Related Settings:**

- ActivityToUserButtonColumn
- ActionsHistoryTimeIntervalsReport
- ActivityMonitoringReport

**Best Practices:** Configure when you aim to enhance report interactivity and user engagement. Avoid excessive use, which may clutter the report interface and overwhelm the users with options.