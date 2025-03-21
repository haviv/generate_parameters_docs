# Moved Back

**Technical Name:** MovedBack

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Moved Back parameter is used to control the behavior within workflow processes, specifically relating to whether an action should automatically move to the next step or require manual approval. It is primarily involved in scenarios where workflow steps could automatically advance or potentially require a rollback or manual intervention for approval.

**Business Impact:**

Using the Moved Back setting effectively can streamline workflow processes by automating step progression where appropriate, while still enforcing manual checks when necessary. This balance helps maintain workflow efficiency without compromising oversight. Misconfiguration can lead to delays in workflow progression or unwanted automatic progressions, impacting operational efficiency and oversight.

**Technical Impact when configured:**

- **Configured as true**: Enables automatic approval for the next step in a workflow, reducing manual interventions and potentially speeding up the process.
- **Configured as false**: Requires manual approval to move to the next step of the workflow, increasing oversight but potentially slowing down the process.

**Examples Scenario:**

Consider a scenario in an organization's GRC processes where any change in user access rights undergoes a review process. Setting Moved Back to true could automate the approval for changes deemed low risk, thus speeding up the workflow. Conversely, for high-risk access changes, setting Moved Back to false would necessitate a manual review, ensuring adequate scrutiny and reducing risk.

**Related Settings:**

- notifyApproverWhenWorkflowIsFinishedField
- AutomaticApprovalNextStep

**Best Practices:** 

- **Configure when:** There's high confidence in the automated checks and balances within a workflow step, or when aiming to streamline operations where manual approval is deemed unnecessary.
  
- **Avoid when:** Steps involve critical decisions or impacts that necessitate human judgment, oversight, or when the risk of incorrect automatic advancement is deemed too high.