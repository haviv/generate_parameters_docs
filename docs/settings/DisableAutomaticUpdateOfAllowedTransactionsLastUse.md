# Disable Automatic Update Of Allowed Transactions Last Use

**Technical Name:** DisableAutomaticUpdateOfAllowedTransactionsLastUse

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls whether the system will automatically update the 'last use' date of allowed transactions within the system. When disabled, transactions approved or executed by users will not have their 'last use' data automatically refreshed based on activity.

**Business Impact:**

Enabling this parameter will aid in maintaining the integrity and accuracy of audit trails and compliance reporting by ensuring that transactions are not mistakenly flagged as inactive or unused. It can also assist in the identification of potentially obsolete transactions that no longer contribute to business processes, helping organizations to streamline operations and reduce unnecessary access.

**Technical Impact when configured:**

When configured, the automation responsible for updating the record of when a transaction was last used is disabled. This means administrators will need to manually review and update these records or develop alternate mechanisms to track transaction activity.

**Examples Scenario:**

- A financial institution requires accurate records of transaction activity for compliance with regulatory standards. Disabling automatic updates necessitates a manual review process, ensuring only intentional updates are made, thus maintaining precise control over transaction usage data.

**Related Settings:** 

**Best Practices:** configure when usage data accuracy is of paramount importance and manual oversight is required; avoid when continuous, automatic updates are necessary for operational efficiency and compliance reporting.