# Excel Matrix Freeze Pane Row

**Technical Name:** ExcelMatrix_FreezePaneRow

**Category:** Reporting

**Default Value:**

**Impact Level:** Low

**Description:**

This parameter controls the row at which the pane in an Excel matrix will be frozen. This feature is particularly useful in improving the readability of reports by keeping headers visible while scrolling through the data.

**Business Impact:**

Ensuring that report headers remain visible as users scroll through long Excel reports enhances usability and reduces the risk of data misinterpretation. This can lead to more efficient data analysis and better decision-making processes.

**Technical Impact when configured:**

When set, the ExcelMatrix_FreezePaneRow parameter fixes the display of row headers at the top of the Excel window, regardless of the user's vertical scroll position within the document. This ensures that contextual information about the columns is always visible to the user, enhancing the comprehensibility of complex datasets.

**Examples Scenario:**

Consider a scenario where an organization generates monthly compliance reports in Excel format. These reports contain hundreds of rows of audit findings categorized by various risk parameters. By setting the ExcelMatrix_FreezePaneRow parameter, the organization can ensure that the column descriptions (such as "Risk Category", "Finding", "Responsible Party", etc.) remain in view as stakeholders scroll through the data, facilitating a better understanding of the report content.

**Related Settings:**

- PerformManualWorkflowActionsOnDone

**Best Practices:** configure when the Excel reports contain substantial amounts of data that require scrolling, avoid when the Excel report is concise enough to be viewed without scrolling.