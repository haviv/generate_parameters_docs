**Authorization Review Show Partial Approval Icon**

**Technical Name:** AuthorizationReviewShowPartialApprovalIcon

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This parameter controls the display of a partial approval icon during the authorization review process. Its primary function is to visually indicate items within the Pathlock Cloud GRC platform that have received partial approvals from the appropriate stakeholders. This feature enhances the clarity of the approval process by allowing users to quickly identify which items are partially approved, requiring further action.

**Business Impact:**

Implementing this feature can significantly streamline the authorization review process by providing immediate visual cues about the approval status of various items. This can lead to more efficient decision-making, reduced approval times, and improved compliance oversight, thus enhancing the overall security and risk management posture of the organization.

**Technical Impact when configured:**

When enabled, this parameter adds a partial approval icon next to authorization items that have not yet received full approval. This enhances user interface intuitiveness and aids in prioritizing actions for incomplete reviews. It requires proper configuration in the user interface settings of the Pathlock Cloud GRC platform to ensure the icon is displayed correctly and in the appropriate contexts.

**Example Scenario:**

In a scenario where multiple department heads are required to approve access rights for a sensitive system, the Authorization Review Show Partial Approval Icon feature will indicate which requests have been approved by some but not all required approvers. This can help the reviewing compliance officer to quickly identify and address these partial approvals, ensuring no request is inadvertently overlooked.

**Related Settings:**

- AuthorizationReviewPositionChangeNotificationVisible

**Applicable Workflows Actions:** 

Not applicable.

**Best Practices:** 

- **Configure when:** There is a complex multi-tier approval process in place within your organization, where visibility on partial approvals can expedite the review process and decision-making.
- **Avoid when:** The authorization process is linear or does not benefit from the granularity of displaying partial approvals, to keep the interface streamlined and avoid potential confusion.