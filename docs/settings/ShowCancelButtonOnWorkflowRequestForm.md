# Show Cancel Button On Workflow Request Form

**Technical Name:** ShowCancelButtonOnWorkflowRequestForm

**Category:** Workflow

**Default Value:**

**Impact Level:** Low

**Description:** This parameter determines whether the cancel button should be displayed on the workflow request form. It enables users to abort the request process if they decide not to proceed.

**Business Impact:** Allowing the cancel button on the workflow request form can improve user experience by providing an easy way to stop the creation or submission process of a request. This can save time for both users and administrators by preventing the need to manually reverse submissions that were made in error.

**Technical Impact when configured:** When enabled, this feature inserts a cancel button in the workflow request form, offering users a straightforward method to halt their request initiation or completion. If disabled, users have no direct means on the form to cancel their action, potentially leading to unintentional submissions.

**Examples Scenario:** A user starts the process of submitting a request for access rights in the Pathlock Cloud GRC platform but realizes they have selected the wrong permissions or entered incorrect information. With the cancel button visible, they can easily stop the process and correct the mistake without submitting the erroneous request.

**Related Settings:** 

**Best Practices:** 
- **Configure when** you aim to enhance user experience by providing flexibility and control over the submission process.
- **Avoid when** the workflow process is critical, and every request initiation must be completed to ensure compliance or security standards.