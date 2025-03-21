# Automatic Lock User Workflow Action

**Technical Name:** AutomaticLockUserWorkflowActionId

**Category:** User Management

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter configures the ID for the automatic lock user workflow action within Pathlock Cloud GRC platform. When activated, this workflow automatically locks user accounts based on specific criteria such as inactivity or risk assessment outcomes.

**Business Impact:**

Automatically locking user accounts that are inactive or have been assessed as high-risk helps in enforcing security policies, reducing the risk of unauthorized access, and ensuring compliance with various regulatory standards. This process aids in maintaining the integrity and security of the organization's data and systems.

**Technical Impact when configured:**

Once configured, the Automatic Lock User Workflow Action will automatically initiate the locking of user accounts according to the predefined rules set by the administrator. This reduces the need for manual oversight in managing user account statuses, thus improving operational efficiency and security posture.

**Examples Scenario:**

- **Inactivity:** If a user has not logged in for a specified period, indicating potential account abandonment, the workflow will automatically lock the user account to prevent unauthorized use.
  
- **Risk Assessment:** After performing a risk assessment, any user account deemed to pose a high risk (e.g., due to violation of security policies) is automatically locked by the workflow.

**Related Settings:** AutomaticLockUserCommentTemplate

**Best Practices:** 

- **Configure when:** It's crucial to automatically lock user accounts based on certain conditions like prolonged inactivity or after a risk assessment has identified a user account as high-risk. 
- **Avoid when:** There is a need for constant manual review or if the organization's policy requires accounts to remain active despite inactivity or risk assessment outcomes.