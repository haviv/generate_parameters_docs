# Verify Workflow Actions Not Verified Text

**Technical Name:** VerifyWorkflowActionsNotVerifiedText

**Category:** Workflow Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The VerifyWorkflowActionsNotVerifiedText parameter plays a critical role in configuring the textual messages displayed when workflow actions are not verified. It primarily influences the user experience by providing clear and specific feedback concerning the verification status of actions within a workflow.

**Business Impact:**

Correct configuration of this parameter enhances clarity for end users by presenting them with specific text related to actions that have not been verified. This is particularly significant in environments where actions require verification for compliance, audit trails, or security purposes. Accurate and clear messages can help in quickly identifying unverified actions, thereby expediting the compliance and audit review process.

**Technical Impact when configured:**

When configured, this parameter directly impacts how users interact with the workflow system. It determines the messaging they receive regarding the verification status of their actions. Proper configuration can thus reduce confusion and support a streamlined workflow process, ensuring all necessary actions are verified according to the organization's compliance and governance standards.

**Examples Scenario:**

- In a scenario where users submit documents for approval within the Pathlock platform, if certain actions associated with these documents are not verified, the VerifyWorkflowActionsNotVerifiedText could display a message such as "Document submission pending verification." This informs the user that the submission process is incomplete, prompting necessary follow-up actions.

**Related Settings:**

- AuthorizationReviewTransaction
- FieldSetsEntitiesXmlPath

**Best Practices:** configure when

- it is necessary to clarify the verification status of actions within significant workflows, especially those related to compliance and security. 

avoid when

- default system messages are sufficiently clear for your organization's workflow processes, or when modifications could lead to confusion or misinterpretation of the action's status.