**Show Transaction Application Area**

**Technical Name:** ShowTransactionApplicationArea

**Category:** Reporting

**Default Value:** True

**Impact Level:** Medium

**Description:**

The `ShowTransactionApplicationArea` parameter controls the visibility of specific transaction-related information within reports and user interfaces in the Pathlock Cloud GRC platform. This parameter determines whether additional context about transactions, especially in terms of their application area or their criticality, is displayed to the user.

**Business Impact:**

Enabling this parameter enhances the user's ability to understand the scope and significance of transactions within the system. It can lead to better decision-making by providing additional information that could indicate potential issues or areas requiring closer scrutiny. For organizations managing compliance and risk, the visibility of such information is crucial for identifying high-risk transactions that might warrant further investigation or action.

**Technical Impact when configured:**

When configured to show the transaction application area, additional columns or indicators may be rendered in reports and user interfaces, potentially altering the layout or the amount of information displayed. This can affect the user experience by providing a more detailed view of transactions, including their application area and criticality level, directly impacting how users interpret and interact with reports.

**Examples Scenario:**

An auditor within a financial institution enables the `ShowTransactionApplicationArea` parameter to review transactions processed in the last quarter. By doing so, the auditor can quickly identify high-risk transactions in critical application areas, facilitating a focused review on areas that matter most for compliance and risk assessment.

**Related Settings:**

- ShowTransactionStatusColumn

**Best Practices:** configure when requiring increased transparency and detail in reports for better risk assessment and auditing. Avoid when simplicity and reduced information load are preferred to speed up review processes or when the additional information does not contribute to the desired analysis outcome.