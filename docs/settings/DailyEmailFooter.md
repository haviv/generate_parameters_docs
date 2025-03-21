# Events Summary Mail - Footer

**Technical Name:** DailyEmailFooter

**Category:** Reporting

**Default Value:**

**Impact Level:** Low

**Description:**

The Events Summary Mail - Footer parameter allows users to customize the footer content of daily email reports within the Pathlock Cloud GRC platform. This customization enhances report readability and provides a space for additional, context-specific notes or contact information relevant to the report's recipients.

**Business Impact:**

Customizing the email footer can improve communication and clarity for end users who receive these reports. It enables the inclusion of necessary disclaimers, contact details for IT support or security teams, and other organizational messages that reinforce the reports' relevance and actionable insights.

**Technical Impact when configured:**

When the DailyEmailFooter is configured, it directly affects the presentation of the emailed reports, potentially improving user engagement with the content. It does not alter the data within the report but adds a custom message or information at the bottom of the email, which can be critical for ensuring the necessary actions are taken based on the report's findings.

**Examples Scenario:**

For instance, after configuring the DailyEmailFooter to include contact information for the security team, a report highlighting risks associated with certain user activities is sent out. A recipient who notices an anomaly in their activities can immediately reach out to the security team using the provided contact details, speeding up the resolution of potential security issues.

**Related Settings:**

- DailyEmailExcelEventColumnWidth

**Best Practices:** 

- **Configure when:** You want to add specific notes, contact information, or disclaimers to enhance the communication of daily reports.
- **Avoid when:** There is no added value or relevant information to be communicated in the footer. Keeping the email concise might sometimes be more effective.