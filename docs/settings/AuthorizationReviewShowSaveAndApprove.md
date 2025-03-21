# Authorization Review Show Save And Approve

**Technical Name:** AuthorizationReviewShowSaveAndApprove

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

This parameter controls the visibility and functionality of the "Save and Approve" option within the Authorization Review process of the Pathlock Cloud GRC platform. It is designed to streamline the review process by allowing users to save changes and approve them in a single action.

**Business Impact:**

Enabling this feature can significantly expedite the authorization review process, reducing the time required for users to approve and implement security changes. It enhances operational efficiency by simplifying the steps needed for authorization validation and approval, directly impacting the speed at which access and permission adjustments are applied within the organization.

**Technical Impact when configured:**

When this parameter is enabled, users participating in the authorization review process will see an option to "Save and Approve" changes. This combines two actions into one, thereby speeding up the review and approval workflow. It can also influence system load and performance, as it potentially reduces the number of actions and server requests made during authorization reviews.

**Example Scenario:**

Consider a scenario where a financial institution is undergoing a quarterly audit and needs to review and adjust the access rights of numerous users across different departments swiftly. By enabling AuthorizationReviewShowSaveAndApprove, the compliance team can efficiently review changes, apply necessary modifications, and approve them in a streamlined fashion, ensuring access rights are correctly managed in compliance with regulatory requirements without unnecessary delays.

**Related Settings:**

- AuthorizationReviewShowBusinessProcess

**Best Practices:** configure when initiating large-scale authorization reviews or during periods of high compliance activity to streamline workflows. Avoid when detailed, step-by-step review and approval is required for each change to ensure precise control over the authorization process.