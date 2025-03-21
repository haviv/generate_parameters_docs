**Technical Name:** TransactionAttribute6ColumnHeader

**Category:** General - UI

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter controls the display of the sixth transaction attribute within the Pathlock GRC platform's user interface, particularly in the context of transaction-related reports and screens. It specifies the column header for the attribute in listings where transaction details are shown.

**Business Impact:** Proper configuration of this parameter ensures that transaction reports and screens display relevant information in a clear and understandable manner, aiding in the efficient monitoring and analysis of transactional data for compliance, audit, and risk management purposes.

**Technical Impact when configured:** When configured, the platform utilizes this parameter to label the corresponding column within transaction-related tables and reports. This facilitates better understanding and interpretation of the data presented, particularly for non-technical users.

**Examples Scenario:**
- **Audit Reporting:** Auditors reviewing transaction logs for irregularities can easily identify the significance of each transaction attribute, enhancing the speed and effectiveness of the audit process.
- **Risk Assessment:** Risk managers can configure this parameter to highlight specific transaction attributes that are relevant to assessing the risk level of certain operations, enabling quicker identification of high-risk transactions.

**Related Settings:**
- `TransactionAttribute2ColumnHeader`: Controls the display name for the second transaction attribute column header.
- `DisplayRoleTypeInWorkflowRoleMapping`: Influences how role types are displayed within workflow role mappings, potentially interacting with transaction attributes when configuring workflows.

**Best Practices:** 
- **Configure when** detailed transaction logging and analysis are required, and when there is a need to make transaction attribute data more accessible to end-users.
- **Avoid when** unnecessary, to prevent cluttering the UI with excess information that could overwhelm users or detract from more critical data points.