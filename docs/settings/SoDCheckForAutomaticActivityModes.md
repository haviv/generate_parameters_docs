# SoD Check For Automatic Activity Modes

**Technical Name:** SoDCheckForAutomaticActivityModes

**Category:** SOD

**Default Value:** None specified

**Impact Level:** High

**Description:**

The 'SoDCheckForAutomaticActivityModes' parameter enables or disables the checking of Segregation of Duties (SoD) conflicts for automatically executed activity modes within the Pathlock Cloud GRC platform. This setting is crucial for organizations that wish to automate certain processes while maintaining strict SoD controls to prevent fraud and errors.

**Business Impact:**

Enabling this parameter ensures that automated processes are continually monitored for potential SoD conflicts, thereby reducing the risk of unauthorized access or fraudulent activities. It supports compliance with internal and external audits by providing a mechanism to review and control automated transactions that could bypass standard SoD checks.

**Technical Impact when configured:**

When configured, the system will include automatically executed activities in the SoD checks, which could impact the overall performance of the SoD check process due to the additional transactions being analyzed. However, it significantly enhances security and compliance by extending SoD controls to cover automated processes.

**Examples Scenario:**

A company has automated the reconciliation and approval of financial transactions to streamline operations. By enabling 'SoDCheckForAutomaticActivityModes', the company can automatically detect if the system grants the same user or role the ability to execute both reconciliation and approval in the automated process, potentially breaching SoD policies.

**Related Settings:** 

Not available based on the provided code references.

**Best Practices:** configure when, avoid when

- **Configure when:** You have numerous automated processes in critical systems where SoD conflicts could lead to significant security or compliance issues.
- **Avoid when:** Your organization has minimal automated activities, or the impact of potential SoD conflicts in automated processes is low, to prevent unnecessary performance impacts on the SoD check process.
